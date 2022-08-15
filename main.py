import logging
from telegram import __version__ as TG_VER
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, Updater


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Send me a photo and I'll use it as your wallpaper 🤩")


async def wallpaper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #Save the photo to a file
    await (await context.bot.get_file(update.message.photo[-1].file_id)).download("./images/image.jpg",)
    await update.message.reply_text("Wallpaper saved!")


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5400373451:AAFfeFB50MDpK4tcIKQLKLqfDwja9_bGdic").build()
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.PHOTO, wallpaper))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()




if __name__ == "__main__":
    main()
