from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import requests


buttons = ReplyKeyboardMarkup([['AQSH dollari', 'Yevro'], ['Rossiya rubl', 'Australiya dollari'], ['Kanada dollari', 'Xitoy yuani'], ['Turkmaniston manati', 'Tojikiston somoni'], ['Yaponiya iyenasi', 'Janubiy Koreya voni'], ['Dasturchi']], resize_keyboard=True)
url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/USD/'
r_usd = requests.get(url)
exchangerate1 = r_usd.json()[0]['Rate']

url2 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/EUR/'
r_eur = requests.get(url2)
exchangerate2 = r_eur.json()[0]['Rate']

url3 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/RUB/'
r_rub = requests.get(url3)
exchangerate3 = r_rub.json()[0]['Rate']

url4 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/AUD/'
r_aud = requests.get(url4)
exchangerate4 = r_aud.json()[0]['Rate']

url5 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/CAD/'
r_cad = requests.get(url5)
exchangerate5 = r_cad.json()[0]['Rate']

url6 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/CNY/'
r_cny = requests.get(url6)
exchangerate6 = r_cny.json()[0]['Rate']

url7 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/TMT/'
r_tmt = requests.get(url7)
exchangerate7 = r_tmt.json()[0]['Rate']

url9 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/KZT/'
r_jpy = requests.get(url9)
exchangerate9 = r_jpy.json()[0]['Rate']

url8 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/TJS/'
r_tjs = requests.get(url8)
exchangerate8 = r_tjs.json()[0]['Rate']

url9 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/JPY/'
r_jpy = requests.get(url9)
exchangerate9 = r_jpy.json()[0]['Rate']

url10 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/KRW/'
r_krw = requests.get(url10)
exchangerate10 = r_krw.json()[0]['Rate']

url11 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/KZT/'
r_kzt = requests.get(url11)
exchangerate11 = r_kzt.json()[0]['Rate']

url12 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/KWD/'
r_kwd = requests.get(url12)
exchangerate12 = r_kwd.json()[0]['Rate']

url13 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/MYR/'
r_myr = requests.get(url13)
exchangerate13 = r_myr.json()[0]['Rate']

url14 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/IRR/'
r_irr = requests.get(url14)
exchangerate14 = r_irr.json()[0]['Rate']

url15 = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/AED/'
r_aed = requests.get(url15)
exchangerate15 = r_aed.json()[0]['Rate']

url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/USD/'
r = requests.get(url)
res = r.json()
date = res[0]['Date']

def start(update, context):
    name = update.message.from_user.first_name
    username = update.message.from_user.last_name
    id_name = update.message.from_user.id
    update.message.reply_html(
    f"<b>Assalomu aleykum, </b><b><a href='tg://user?id={id_name}'>{name}</a>!</b>\n \nSiz bu yerda o`zbek so`mining 10 ta kursga nisbatini bilishingiz mumkin.", reply_markup=buttons)
    return 1

def stats1(update, context):
    update.message.reply_html(
        f'<b>Aqsh dollari</b>\n \nBugungi kurs - {exchangerate1} so`m\nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats2(update, context):
    update.message.reply_html(
        f'<b>Yevro</b>\n \nBugungi kurs - {exchangerate2} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)
    
def stats3(update, context):
    update.message.reply_html(
        f'<b>Rossiya rubl</b>\n \nBugungi kurs - {exchangerate3} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats4(update, context):
    update.message.reply_html(
        f'<b>Australiya dollari</b>\n \nBugungi kurs - {exchangerate4} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats5(update, context):
    update.message.reply_html(
        f'<b>Kanada dollari</b>\n \nBugungi kurs - {exchangerate5} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)
    
def stats6(update, context):
    update.message.reply_html(
        f'<b>Xitoy yuani</b>\n \nBugungi kurs - {exchangerate6} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats7(update, context):
    update.message.reply_html(
        f'<b>Turkmaniston manati</b>\n \nBugungi kurs - {exchangerate7} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats8(update, context):
    update.message.reply_html(
        f'<b>Tojikiston somoni</b>\n \nBugungi kurs - {exchangerate8} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)
    
def stats9(update, context):
    update.message.reply_html(
        f'<b>Yaponiya iyenasi</b>\n \nBugungi kurs - {exchangerate9} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats10(update, context):
    update.message.reply_html(
        f'<b>Janubiy Koreya voni</b>\n \nBugungi kurs - {exchangerate10} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats11(update, context):
    update.message.reply_html(
        f'<b>Qozog`iston tengesi</b>\n \nBugungi kurs - {exchangerate11} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats12(update, context):
    update.message.reply_html(
        f'<b>Quvayt dinori</b>\n \nBugungi kurs - {exchangerate12} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats13(update, context):
    update.message.reply_html(
        f'<b>Malayziya ringgiti</b>\n \nBugungi kurs - {exchangerate13} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats14(update, context):
    update.message.reply_html(
        f'<b>Eron riali</b>\n \nBugungi kurs - {exchangerate14} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats15(update, context):
    update.message.reply_html(
        f'<b>BAA dirhami</b>\n \nBugungi kurs - {exchangerate15} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def stats16(update, context):
    update.message.reply_html(
        f'<b>Singapur dollari</b>\n \nBugungi kurs - {exchangerate16} so`m \nSana: {date}\n\n<a href="https://t.me/ableprogrammer">Dasturchi</a>',reply_markup=buttons)

def programmer(update, context):
    update.message.reply_html(f"<b>Dastuchi: Usmonaliyev Salohiddin</b> \nFarg\'ona viloyati 1-aniq va ijtimoiy fanlarga ixtisoslashtirilgan maktab-internatining 7-sinf o\'quvchisi.\n<a href='https://ableprogrammer.github.io'>👨‍💻 Dasturchi</a>", reply_markup=buttons)
updater = Updater('5282860580:AAFs6m5Jve7PVWKQp0dtAJ9ufqvRNENqXTg', use_context=True)
conv_handler = ConversationHandler(
    entry_points = [CommandHandler('start', start)],
    states={
        1: [MessageHandler(Filters.regex('^(AQSH dollari)$'), stats1),
            MessageHandler(Filters.regex('^(Yevro)$'), stats2),
            MessageHandler(Filters.regex('^(Rossiya rubl)$'), stats3),
            MessageHandler(Filters.regex('^(Australiya dollari)$'), stats4),
            MessageHandler(Filters.regex('^(Kanada dollari)$'), stats5),
            MessageHandler(Filters.regex('^(Xitoy yuani)$'), stats6),
            MessageHandler(Filters.regex('^(Turkmaniston manati)$'), stats7),
            MessageHandler(Filters.regex('^(Tojikiston somoni)$'), stats8),
            MessageHandler(Filters.regex('^(Yaponiya iyenasi)$'), stats9),
            MessageHandler(Filters.regex('^(Janubiy Koreya voni)$'), stats10),

            MessageHandler(Filters.regex('^(Dasturchi)$'), programmer),
            ]
    },
    fallbacks=[MessageHandler(Filters.text, start)]
)

updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
