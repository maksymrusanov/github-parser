# GitHub Parser

 **Python-based tool that collects GitHub trending repositories for analysis and insights.**

---

##  Overview

**GitHub Parser** is a lightweight Python project that fetches data from GitHub Trending pages and extracts useful metadata about popular repositories.

It can be used as:
- A data source for analytics or dashboards
- A helper tool for developers tracking trends
- A backend service for bots or automation systems

The project includes a **Telegram bot** interface and is fully **Docker-ready**.

---

##  Features

- Written in **Python**
- Fetches GitHub **Trending repositories**
- Extracts key repository metadata
- Telegram bot integration
- Easy to extend and customize
- Docker & Docker Compose support

---

##  How It Works

At its core, the parser pulls data from GitHub’s trending repositories (e.g., Python, JavaScript, Go) and extracts key metadata such as:

- Repository name
- Owner
- Stars and forks
- Description
- Language
- URL

This makes it a great starting point for analytics, visualizations, or monitoring tools.

---
##  Prerequisites

Before starting, make sure you have:

- **Python 3.10+** (for local runs)
- **Docker** (recommended)
- A **Telegram Bot Token** from [@BotFather](https://t.me/botfather)

---   
##  Quick Start

###  Requirements

Make sure you have:

- Python 3.8+(Docker uses python 3.13 btw)   
- `pip` installed

---

###  Installation


1. **Choose Your Run Method**
**Option A: Running with Docker hub**

```bash
docker run -e TELEGRAM_TOKEN=your_token maksymrusanov/github-trends-bot:arm64
```

**Option B: Running with Docker (Recommended)**

This method is the most reliable as it handles all dependencies automatically.
```bash
# Build the image
docker-compose -p github-trends up --build
```
Option C: Running Locally

1) **Clone the repository:**

   ```bash
   git clone https://github.com/maksymrusanov/github-parser.git
   cd github-parser
   ```
2) **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```
3) **Configure Environment Variables**
Create a .env file in the root directory and add your bot credentials:
```bash
TELEGRAM_TOKEN=your_telegram_bot_token_here
```
4) **Install dependencies:**
```bash
pip install -r requirements.txt
```
5) **Launch the bot:**
```bash
python bot.py
```
