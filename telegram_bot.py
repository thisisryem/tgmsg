import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
from flask import Flask, request

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get token from environment variable
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8080))
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", f"https://your-app-name.onrender.com")

# Initialize Flask app
app = Flask(__name__)

# Initialize bot application
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: CallbackContext) -> None:
    """Send a message with an inline button when the command /start is issued."""
    # Create the inline keyboard button
    keyboard = [
        [InlineKeyboardButton("Earn", url="http://t.me/TonFunx_bot/earn")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the message with the button
    # Using Markdown V2 formatting for bold text
    message_text = "Earn from now Just by Watching\n*Earn upto 0\\.01\\$ per ads*\nWatch ads and Earn now\\!"
    
    await update.message.reply_text(
        message_text,
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'  # Enable Markdown formatting
    )

@app.route(f"/{TOKEN}", methods=['POST'])
async def webhook_handler():
    """Handle incoming webhook updates"""
    await application.process_update(
        Update.de_json(request.get_json(force=True), application.bot)
    )
    return "OK"

@app.route("/")
def index():
    return "Bot is running!"

def setup_webhook():
    """Set webhook for the bot"""
    webhook_url = f"{WEBHOOK_URL}/{TOKEN}"
    application.bot.set_webhook(webhook_url)
    logger.info(f"Webhook set to {webhook_url}")

def main() -> None:
    """Start the bot with webhook."""
    # Add command handler
    application.add_handler(CommandHandler("start", start))
    
    # Set up webhook and start the Flask server
    setup_webhook()
    app.run(host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    main()
