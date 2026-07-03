# 🌸 NYRA — Sweet AI Chatbot for Telegram 💕

<p align="center">
  <img src="https://files.catbox.moe/qxxbe3.jpg" width="200" alt="Nyra Bot" />
</p>

<p align="center">
  <em>✨ Your sweet, warm & lovely virtual companion ✨</em>
</p>

---

## 💖 About Nyra

**Nyra** is a warm, loving, and bubbly AI chatbot for Telegram — powered by Google Gemini. She's your sweet virtual best friend who chats with you in your language, reacts with cute animations, and always keeps the conversation positive and full of love! 🌺

She speaks **5 languages** — and her default personality is a sweet Tamil girl who chats in **Tamlish** (Tamil + English mix) 🥰

---

## 🌍 Supported Languages

When you start the bot, choose your favourite language:

| Language | Flag |
|----------|------|
| English | 🇬🇧 |
| Tanglish *(Tamil + English)* | 🇮🇳 |
| Hindi | 🇮🇳 |
| Russian | 🇷🇺 |
| Español *(Colombian)* | 🇨🇴 |

Nyra's entire personality, replies, and messages will switch to your chosen language! You can change it anytime.

---

## ✨ Features

- 🌸 **Sweet AI Chat** — Powered by Gemini 2.5, Nyra replies with a warm, lovely personality
- 🌍 **Multi-Language Support** — English, Tamlish, Hindi, Russian, Colombian Spanish
- 🎀 **Anime Reactions** — `/hug`, `/slap`, `/kiss`, `/pet`, `/punch`, `/kick`, `/snap` with animated GIFs
- 🎲 **Fun Games** — `/dice`, `/dart`, `/basket`, `/football`
- 🌺 **Sweet Welcome Messages** — Warmly greets new group members
- 🛡️ **NSFW Filter** — Keeps chats clean and sweet
- 💬 **Chat Memory** — Remembers conversation context for natural flow
- 📊 **Bot Stats** — Owner can check usage stats
- 📢 **Broadcast** — Owner can send messages to all users/groups

---

## 💬 Commands

| Command | Description |
|---------|-------------|
| `/start` | Start Nyra and choose your language 🌍 |
| `/hug` | Give someone a warm hug 🤗 |
| `/slap` | Playfully slap someone 👋 |
| `/kiss` | Send a sweet kiss 😘 |
| `/pet` | Pat someone on the head 🥰 |
| `/punch` | Throw a punch 🥊 |
| `/kick` | Give a kick 🦵 |
| `/snap` | Snap at someone 💥 |
| `/dice` | Roll a dice 🎲 |
| `/dart` | Throw a dart 🎯 |
| `/basket` | Shoot a basket 🏀 |
| `/football` | Kick a football ⚽ |
| `/clearchat` | Clear your chat history with Nyra 🧹 |
| `/stats` | *(Owner only)* View bot statistics 📊 |
| `/broadcast` | *(Owner only)* Broadcast a message 📢 |

---

## 🔧 Setup & Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Nyra_Chatbot.git
cd Nyra_Chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file in the root folder:

```env
BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_google_gemini_api_key
MONGO_URI=your_mongodb_connection_uri
OWNER_ID=your_telegram_user_id
LOG_CHAT_ID=your_log_channel_id
```

### 4. Run the Bot

```bash
python NYRA/main.py
```

---

## 📁 Project Structure

```
NYRA_bot/
├── NYRA/
│   ├── main.py          # Bot entry point
│   ├── config.py        # Configuration & tokens
│   ├── prompt.py        # Nyra's personality prompts (per language)
│   ├── languages.py     # Language strings & translations
│   └── logger_config.py # Logging config
├── handlers/
│   ├── command_handlers.py  # /start, language select, /broadcast etc.
│   ├── chat_handlers.py     # AI chat, sticker/media handling
│   └── member_handlers.py   # Welcome/leave events
├── utils/
│   ├── db.py            # MongoDB operations + language storage
│   ├── filters.py       # NSFW filter, reply logic
│   └── chat_logger.py   # Chat logging
├── chat_member.py       # Bot add/remove logging
├── gifs.py              # Sticker file IDs
├── requirements.txt
├── Procfile
└── README.md
```

---

## 💞 Credits & Support

> Created with love and sweetness by [**Ƥຮycho_℘ath**](https://t.me/ll_philosophie_ll) 🌸  
> For support, feel free to reach out — I'm always happy to help! 💕

- 💬 [Support Group](https://t.me/+roNC_pDAtQxhNWVl)
- 📢 [Updates Channel](https://t.me/The_Moon_Network)

---

### 🌺 *"Every message is a little moment of warmth — and Nyra is here to make yours bloom."* 🌸

---
