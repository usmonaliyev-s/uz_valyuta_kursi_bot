from telegram import ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters
import requests
import asyncio

buttons = ReplyKeyboardMarkup(
    [['AQSH dollari', 'Yevro'],
     ['Rossiya rubl', 'Australiya dollari'],
     ['Kanada dollari', 'Xitoy yuani'],
     ['Turkmaniston manati', 'Tojikiston somoni'],
     ['Yaponiya iyenasi', 'Janubiy Koreya voni']],
    resize_keyboard=True
)

# Fetch exchange rates from CBU API (you may want to refresh this data periodically in production)
def get_rate(code):
    url = f'https://cbu.uz/oz/arkhiv-kursov-valyut/json/{code}/'
    r = requests.get(url)
    return r.json()[0]['Rate']

exchangerate1 = get_rate('USD')
exchangerate2 = get_rate('EUR')
exchangerate3 = get_rate('RUB')
exchangerate4 = get_rate('AUD')
exchangerate5 = get_rate('CAD')
exchangerate6 = get_rate('CNY')
exchangerate7 = get_rate('TMT')
exchangerate8 = get_rate('TJS')
exchangerate9 = get_rate('JPY')
exchangerate10 = get_rate('KRW')
exchangerate11 = get_rate('KZT')
exchangerate12 = get_rate('KWD')
exchangerate13 = get_rate('MYR')
exchangerate14 = get_rate('IRR')
exchangerate15 = get_rate('AED')
exchangerate16 = 'N/A'  # or define properly
url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/USD/'
r = requests.get(url)
res = r.json()
date = res[0]['Date']

async def start(update, context):
    name = update.message.from_user.first_name
    id_name = update.message.from_user.id
    await update.message.reply_html(
        f"<b>Assalomu alaykum, <a href='tg://user?id={id_name}'>{name}</a>!</b>\n"
        "Siz bu yerda turli xil kurslar haqida bilishingiz mumkin.",
        reply_markup=buttons
    )
    return 1

async def stats1(update, context):
    await update.message.reply_html(
        f'<b>Aqsh dollari</b>\nBugungi kurs - {exchangerate1} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats2(update, context):
    await update.message.reply_html(
        f'<b>Yevro</b>\nBugungi kurs - {exchangerate2} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats3(update, context):
    await update.message.reply_html(
        f'<b>Rossiya rubl</b>\nBugungi kurs - {exchangerate3} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats4(update, context):
    await update.message.reply_html(
        f'<b>Australiya dollari</b>\nBugungi kurs - {exchangerate4} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats5(update, context):
    await update.message.reply_html(
        f'<b>Kanada dollari</b>\nBugungi kurs - {exchangerate5} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats6(update, context):
    await update.message.reply_html(
        f'<b>Xitoy yuani</b>\nBugungi kurs - {exchangerate6} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats7(update, context):
    await update.message.reply_html(
        f'<b>Turkmaniston manati</b>\nBugungi kurs - {exchangerate7} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats8(update, context):
    await update.message.reply_html(
        f'<b>Tojikiston somoni</b>\nBugungi kurs - {exchangerate8} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats9(update, context):
    await update.message.reply_html(
        f'<b>Yaponiya iyenasi</b>\nBugungi kurs - {exchangerate9} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats10(update, context):
    await update.message.reply_html(
        f'<b>Janubiy Koreya voni</b>\nBugungi kurs - {exchangerate10} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats11(update, context):
    await update.message.reply_html(
        f'<b>Qozog`iston tengesi</b>\nBugungi kurs - {exchangerate11} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats12(update, context):
    await update.message.reply_html(
        f'<b>Quvayt dinori</b>\nBugungi kurs - {exchangerate12} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats13(update, context):
    await update.message.reply_html(
        f'<b>Malayziya ringgiti</b>\nBugungi kurs - {exchangerate13} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats14(update, context):
    await update.message.reply_html(
        f'<b>Eron riali</b>\nBugungi kurs - {exchangerate14} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats15(update, context):
    await update.message.reply_html(
        f'<b>BAA dirhami</b>\nBugungi kurs - {exchangerate15} so`m\nSana: {date}'
        , reply_markup=buttons)

async def stats16(update, context):
    await update.message.reply_html(
        f'<b>Singapur dollari</b>\nBugungi kurs - {exchangerate16} so`m\nSana: {date}'
        , reply_markup=buttons)


async def fallback(update, context):
    return await start(update, context)

def main():
    application = ApplicationBuilder().token('7979914433:AAE97-2PIwUZYP8PWYD8sF2VwtQMxH1dB1k').build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [
                MessageHandler(filters.Regex('^(AQSH dollari)$'), stats1),
                MessageHandler(filters.Regex('^(Yevro)$'), stats2),
                MessageHandler(filters.Regex('^(Rossiya rubl)$'), stats3),
                MessageHandler(filters.Regex('^(Australiya dollari)$'), stats4),
                MessageHandler(filters.Regex('^(Kanada dollari)$'), stats5),
                MessageHandler(filters.Regex('^(Xitoy yuani)$'), stats6),
                MessageHandler(filters.Regex('^(Turkmaniston manati)$'), stats7),
                MessageHandler(filters.Regex('^(Tojikiston somoni)$'), stats8),
                MessageHandler(filters.Regex('^(Yaponiya iyenasi)$'), stats9),
                MessageHandler(filters.Regex('^(Janubiy Koreya voni)$'), stats10),
            ]
        },
        fallbacks=[MessageHandler(filters.TEXT & ~filters.COMMAND, fallback)],
    )

    application.add_handler(conv_handler)

    print("Bot started...")
    application.run_polling()

if __name__ == '__main__':
    main()
