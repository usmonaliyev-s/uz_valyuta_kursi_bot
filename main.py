import os
import requests
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, ConversationHandler, filters
)

# Load token from .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Keyboard buttons
buttons = ReplyKeyboardMarkup(
    [
        ['AQSH dollari', 'Yevro'],
        ['Rossiya rubl', 'Australiya dollari'],
        ['Kanada dollari', 'Xitoy yuani'],
        ['Turkmaniston manati', 'Tojikiston somoni'],
        ['Yaponiya iyenasi', 'Janubiy Koreya voni'],
        ['Dasturchi']
    ],
    resize_keyboard=True
)

# Currency name map
currencies = {
    'USD': 'AQSH dollari',
    'EUR': 'Yevro',
    'RUB': 'Rossiya rubl',
    'AUD': 'Australiya dollari',
    'CAD': 'Kanada dollari',
    'CNY': 'Xitoy yuani',
    'TMT': 'Turkmaniston manati',
    'TJS': 'Tojikiston somoni',
    'JPY': 'Yaponiya iyenasi',
    'KRW': 'Janubiy Koreya voni'
}

# Cache exchange rates at startup
exchange_rates = {}
for code in currencies:
    url = f'https://cbu.uz/oz/arkhiv-kursov-valyut/json/{code}/'
    response = requests.get(url)
    data = response.json()
    exchange_rates[code] = data[0]['Rate']
    date = data[0]['Date']

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        f"<b>Assalomu alaykum, </b><b><a href='tg://user?id={user.id}'>{user.first_name}</a>!</b>\n\n"
        f"Siz bu yerda o'zbek so'mining 10 ta mashhur valyutalarga nisbatan kursini bilishingiz mumkin.",
        reply_markup=buttons
    )
    return 1

# Currency response
async def handle_currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    for code, name in currencies.items():
        if text == name:
            rate = exchange_rates[code]
            await update.message.reply_html(
                f"<b>{name}</b>\n\nBugungi kurs: {rate} so'm\nSana: {date}\n\n",
                reply_markup=buttons
            )
            return

# Dasturchi info
async def programmer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(
        "<b>Dasturchi: Usmonaliyev Salohiddin</b>",
        reply_markup=buttons
    )

# Main function
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [
                MessageHandler(filters.Regex(f"^({'|'.join(currencies.values())})$"), handle_currency),
                MessageHandler(filters.Regex('^Dasturchi$'), programmer)
            ]
        },
        fallbacks=[MessageHandler(filters.TEXT, start)]
    )

    app.add_handler(conv_handler)

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
