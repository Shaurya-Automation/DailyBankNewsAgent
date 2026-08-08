import feedparser
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- CONFIGURATION ---
HF_API_KEY = os.getenv("HF_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Target Banks
BANKS = [
    "HDFC Bank", "ICICI Bank", "Axis Bank", "Kotak Mahindra Bank",
    "IndusInd Bank", "IDBI Bank", "YES Bank", "IDFC First Bank", "City Union Bank"
]

def get_google_news_rss(bank_name):
    """Fetches Google News RSS for a specific bank."""
    query = f"{bank_name} bank news interest rate FD loan fraud scam offer".replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    return url

def fetch_news():
    """Fetches top 5 stories for each bank and groups them."""
    print("🔍 Fetching live news for 9 banks...")
    grouped_news = {bank: [] for bank in BANKS}
    
    for bank in BANKS:
        rss_url = get_google_news_rss(bank)
        try:
            feed = feedparser.parse(rss_url)
            for entry in feed.entries[:5]:
                # Clean the title
                title = entry.title.replace("BREAKING:", "").replace("NEWS:", "").strip()
                grouped_news[bank].append({
                    "title": title,
                    "link": entry.link,
                    "summary": entry.get('summary', '')[:300]
                })
        except Exception as e:
            print(f"⚠️ Error fetching {bank}: {e}")
    
    # Filter out banks with no news to keep it clean
    return {k: v for k, v in grouped_news.items() if v}

def get_emoji_for_news(title, summary):
    """Assigns an emoji based on keywords."""
    text = (title + " " + summary).lower()
    if any(x in text for x in ["rate", "interest", "fd", "deposit", "loan", "cut", "increase"]):
        return "💰"
    if any(x in text for x in ["fraud", "scam", "alert", "warning", "hack", "security"]):
        return "⚠️"
    if any(x in text for x in ["new", "launch", "offer", "card", "app", "feature"]):
        return "🚀"
    if any(x in text for x in ["profit", "growth", "rise", "up", "record"]):
        return "📈"
    return "📰"

def format_news_for_dad(grouped_news):
    """
    Formats the news into a highly readable, magazine-style layout.
    NO AI needed for formatting. Pure Python logic for structure.
    """
    if not grouped_news:
        return "✅ No major news today.\n\nHave a great day! 🌞"

    today = datetime.now().strftime("%d %B %Y")
    message = f"🏦 **Daily Bank Digest**\n📅 *{today}*\n"
    message += "=" * 30 + "\n\n"

    for bank, news_list in grouped_news.items():
        # Bank Header
        message += f"🏢 **{bank}**\n"
        message += "-" * 20 + "\n"

        # News Items (Max 5 per bank to prevent scrolling fatigue)
        for item in news_list[:5]:
            emoji = get_emoji_for_news(item['title'], item['summary'])
            
            # Clean title: Remove "Live", "Now", "Breaking" if repetitive
            clean_title = item['title'].replace("Live", "").replace("Now", "").strip()
            
            # Format: Emoji • Short Headline
            message += f"{emoji} • {clean_title}\n"
        
        # Visual Separator between banks
        message += "\n" + "=" * 30 + "\n\n"

    message += "💡 *Tip: Tap the link in your news app for full details.*\n"
    return message

def send_telegram(message):
    """Sends the formatted message to Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message[:4096],
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("✅ Message sent to Telegram!")
        return True
    else:
        print(f"❌ Failed: {response.text}")
        return False

def main():
    print("🚀 Starting Daily Bank News Agent...")
    grouped_news = fetch_news()
    
    if not grouped_news:
        print("📭 No news found for today.")
        message = "✅ No major news today.\n\nHave a great day! 🌞"
    else:
        print(f"📰 Found news for {len(grouped_news)} banks. Formatting...")
        message = format_news_for_dad(grouped_news)
    
    send_telegram(message)
    print("✅ Done.")

if __name__ == "__main__":
    main()