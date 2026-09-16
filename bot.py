import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
# Логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
# Получаем токен из переменной окружения Render
TOKEN = os.getenv("BOT_TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /start."""
    await update.message.reply_text(
        "🤖 RU-INVEST AI запущен!\n\n"
        "Я буду аналитическим помощником по российскому рынку.\n\n"
        "Используй /help для просмотра команд."
    )
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /help."""
    await update.message.reply_text(
        "📊 RU-INVEST AI — команды:\n\n"
        "/start — запуск бота\n"
        "/help — помощь\n\n"
        "В следующих версиях добавим анализ рынка, "
        "акций, облигаций и инвестиционные сигналы."
    )
def main():
    """Запуск Telegram-бота."""
    if not TOKEN:
        raise RuntimeError(
            "Не задан BOT_TOKEN. Добавь BOT_TOKEN в Environment Variables Render."
        )
    # Создаём приложение Telegram
    app = Application.builder().token(TOKEN).build()
    # Подключаем команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    logger.info("RU-INVEST AI запускается...")
    # Запускаем бота
    app.run_polling()
if __name__ == "__main__":
    main()