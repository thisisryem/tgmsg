import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define a function to handle the /start command
async def start(update: Update, context: CallbackContext) -> None:
    """Send a message with an inline button when the command /start is issued."""
    # Create an inline keyboard with a single button
    keyboard = [
        [InlineKeyboardButton("Earn", url="http://t.me/TonFunx_bot/earn")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send message with inline keyboard
    await update.message.reply_text(
        "Earn from now Just by Watching\n"
        "*Earn upto 0.01$ per ads*\n"
        "Watch ads and Earn now!",
        reply_markup=reply_markup,
        parse_mode='Markdown'  # Enable Markdown for bold text
    )

def main() -> None:
    """Start the bot."""
    # Get the token from environment variables
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("No token provided. Set TELEGRAM_BOT_TOKEN environment variable.")
        return
    
    # Create the Application
    application = Application.builder().token(token).build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
