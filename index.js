const TelegramBot = require("");node-telegram-bot-api
const express = require("express");

const app = express();

// Telegram Botconst bot = new TelegramBot(process.env.BOT_TOKEN,{ polling: true });

bot.on("message", (msg) =>{bot.sendMessage(msg.chat.id, "Bot is alive ✅");});

// Health check for Renderapp.get("/", (req, res) => {res.send("Bot running");});

// Serverconst port = process.env.PORT || 3000;
app.listen(port, () => {console.log("Server running on port", port);});

