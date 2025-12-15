const express = require("express");
const app = express();

app.get("/", (req, res) => res.send("Bot is running"));
app.get("/chk", (req, res) =>
  res.json({ status: "OK", message: "Bot alive" })
);

const port = process.env.PORT || 3000;
app.listen(port);

