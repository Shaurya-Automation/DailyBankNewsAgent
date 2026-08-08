# 🏦 Daily Bank News Agent (Telegram)

> **Automated AI Workflow for Real-Time Financial Insights**

A **Python-native** agent that fetches live financial news from **9 major Indian banks**, uses **AI (Llama 3.1)** to filter for actionable insights (interest rates, fraud alerts, offers), and delivers a **clean, readable daily digest** to Telegram.

Built as a portfolio project to demonstrate **AI Workflow Automation** for creators and businesses. No n8n, no Zapier—just pure Python and serverless automation.

---

## 🚀 What It Does
- **Monitors 9 Key Banks:** HDFC, ICICI, Axis, Kotak, IndusInd, IDBI, YES, IDFC, City Union.
- **Smart AI Filtering:** Uses Hugging Face (Llama 3.1) to ignore generic news (charity, branch openings) and highlight only what matters:
  - 💰 **Interest Rate Changes** (FD, Loans)
  - ⚠️ **Fraud & Security Alerts**
  - 🚀 **New Offers & Schemes**
- **Human-Readable Output:** Formats news with emojis, clear headers, and visual separators for easy mobile reading.
- **Zero-Cost Automation:** Runs automatically every day at **8:00 AM IST** via **GitHub Actions** (Serverless).

---

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **AI Engine:** Hugging Face Inference API (Llama 3.1-8B-Instruct)
- **Data Source:** Google News RSS Feeds
- **Delivery:** Telegram Bot API
- **Hosting/Scheduling:** GitHub Actions (Cron)
- **Libraries:** `feedparser`, `requests`, `python-dotenv`

---

## 🏗️ How It Works (Architecture)
**Fetch**: feedparser pulls RSS feeds from Google News for each of the 9 banks.

**Filter & Summarize**: A prompt-engineered LLM call (via Hugging Face) extracts only actionable news and formats it for readability.

**Deliver**: The formatted text is sent via the Telegram Bot API with Markdown support.

**Schedule**: GitHub Actions triggers the script daily at 2:30 UTC (8:00 AM IST) automatically.

---

## 🚀 How to Run Locally

**Clone the repo**:
*Bash*
git clone [https://github.com/Shaurya-Automation/DailyBankNewsAgent]
cd bank-news-agent

**Install dependencies**:
*Bash*
pip install feedparser requests python-dotenv

**Set up environment variables**: 
*Create a .env file in the root directory*:
HF_API_KEY=your_huggingface_token
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id

**Run the script**:
*Bash*
python main.py

---

## 🌐 Deployment

This project is deployed serverlessly using GitHub Actions.

**Trigger**: Daily Cron (30 2 * * *)
**Cost**: $0 (Free tier)
**Reliability**: 99.9% uptime via GitHub's infrastructure

---

## 🎯 Why This Matters

This project solves a real-world problem: *Information Overload*. Instead of scrolling through 10 news apps, users get a *curated, actionable summary* in one place. It demonstrates the power of **AI Agents** to filter noise and deliver value—exactly the kind of workflow I build for YouTube creators to save them time.

---

Built by Shaurya AI Workflow Automation Consultant for Creators | 17 y/o | India