const TelegramBot = require("node-telegram-bot-api");
const express = require("express");

const app = express();

const bot = new TelegramBot(process.env.BOT_TOKEN, {
  polling: true
});

bot.on("message", (msg) => {
  const chatId = msg.chat.id;

  if (msg.text && msg.text.startsWith("/chk")) {
    const data = msg.text.replace("/chk", "").trim();

    if (!data) {
      bot.sendMessage(
        chatId,
        "❌ Usage:\n/chk 4242424242424242|12|26|123"
      );
      return;
    }

    bot.sendMessage(
      chatId,
      `💳 Card: ${data}\n✅ Status: LIVE (demo)`
    );
    return;
  }
});
