# 🎮 Telegram Game Hub & Minesweeper Mini App

A professional, high-performance Telegram Mini App (TMA) featuring a fully functional Minesweeper game with 30+ levels, local high-score tracking, and a sleek glassmorphism UI. 

![Telegram](https://img.shields.io/badge/Telegram-Mini--App-blue?logo=telegram)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?logo=python)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-orange?logo=javascript)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **Progressive Difficulty:** 30+ handcrafted and procedurally generated levels.
- **Level Selection System:** Unlock new challenges as you progress; progress is saved in the browser.
- **Modern UI/UX:** Responsive glassmorphism design optimized for Telegram's mobile interface.
- **Haptic Feedback:** Native vibration support for flags and game events (requires Telegram mobile).
- **Pro Bot Controller:** Launch the game via `/start`, `/game`, or the dedicated "Play" menu button.
- **Optimized for Mobile:** Fixed-ratio game board to prevent layout shifting or "shrinking" bugs.

---

## 🛠️ Tech Stack

- **Frontend:** Vanilla HTML5, CSS3 (Advanced Animations), JavaScript (ES6+).
- **Backend:** Python 3.10+, [Aiogram 3.x](https://docs.aiogram.dev/) (Asynchronous Bot API).
- **Deployment:** 
  - **Game Logic:** GitHub Pages (Free, static hosting).
  - **Bot Controller:** Railway / VPS (Python runtime).

---

## 🚀 Deployment Guide

### 1. BotFather Configuration (Telegram)
To make the bot look professional, follow these steps with [@BotFather](https://t.me/botfather):
1. **Create Bot:** Use `/newbot` to get your **API TOKEN**.
2. **Setup Menu Button:** 
   - Send `/setmenubutton` -> Select your bot.
   - Enter your live GitHub Pages URL (e.g., `https://username.github.io/repo-name/`).
   - Set the button title: `🎮 Play Games`.
3. **Set Commands:**
   - Send `/setcommands` -> Select your bot.
   - Paste this list:
     ```text
     start - Launch the Game Center
     game - Select a specific level
     ```

### 2. Frontend Hosting (GitHub Pages)
1. Push your `index.html` to your GitHub repository.
2. Go to **Settings > Pages**.
3. Set **Branch** to `main` and click **Save**.
4. Copy your live URL once it appears (the **BASE_URL**).

### 3. Backend Deployment (Railway.app)
1. Connect your GitHub repository to [Railway](https://railway.app/).
2. Add the following **Environment Variables** in the Railway Dashboard:
   - `BOT_TOKEN`: The token you got from BotFather.
   - `BASE_URL`: Your live GitHub Pages URL (make sure it ends with `/`).
3. Railway will automatically use your `railway.json` and `requirements.txt` to start the bot.

---

## 💻 Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME