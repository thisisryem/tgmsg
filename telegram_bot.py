import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get the token from environment variable
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

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

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add command handler
    application.add_handler(CommandHandler("start", start))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
