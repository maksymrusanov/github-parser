# GitHub Parser 🚀

**Python-based data collector that fetches GitHub trending repositories daily for analysis and insights.** 
---
## 📌 Overview

**GitHub Parser** is a lightweight Python tool designed to automatically collect data on trending GitHub repositories. It retrieves daily trending project information, helping developers, data analysts, and automation systems to monitor trends, extract metadata, or build insights dashboards.

---

## 🛠️ Features

- Written in Python — easy to customize and extend  
- Trending repository collection  
- Includes basic bot support and handler utilities  
- Docker-ready for easy deployment

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

##  Quick Start

###  Requirements

Make sure you have:

- Python 3.8+  
- `pip` installed

---

### ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/maksymrusanov/github-parser.git
   cd github-parser
   ```
  2. **Configure Environment Variables**
Create a .env file in the root directory and add your bot credentials:
```bash
TELEGRAM_TOKEN=your_telegram_bot_token_here
```
3. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```
4. **Choose Your Run Method**

**Option A: Running with Docker (Recommended)**
This method is the most reliable as it handles all browser drivers and dependencies automatically.
```bash
# Build the image
docker-compose up --build 

# Run the container
docker run -d --name github-trends --env-file .env 
```
Option B: Running Locally

a) **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```
b) **Install dependencies:**
```bash
pip install -r requirements.txt
```
c) **Launch the bot:**
```bash
python bot.py
```
