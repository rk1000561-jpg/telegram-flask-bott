from flask import Flask, request
import requests

app = Flask(__name__)

# Yahan apna bot token daalo
BOT_TOKEN = "8637303203:AAFBciNUug-amVUZe8ENHi0Na28MwoSrH6M"

@app.route("/", methods=["GET"])
def home():
    return "Bot Running ✅"

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    if "message" in data:

        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": f"You said: {text}"
            }
        )

    return {"ok": True}

if __name__ == "__main__":
    app.run()
