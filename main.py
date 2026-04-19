from src.constants import get_settings
from src.core_logic import start_bot, help_bot, get_player, get_team
from telegram.ext import ApplicationBuilder, CommandHandler

def main():
    settings = get_settings()

    app = ApplicationBuilder().token(settings.telegram_token).build()
    app.add_handler(CommandHandler("start", start_bot))
    app.add_handler(CommandHandler("help", help_bot))
    app.add_handler(CommandHandler("player", get_player))
    app.add_handler(CommandHandler("team", get_team))
    app.run_polling(poll_interval=2)


if __name__ == "__main__":
    main()
