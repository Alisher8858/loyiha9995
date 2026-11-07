
import os
import logging
import random
import asyncio

from aiohttp import web
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# Environment Variables
TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

if not TOKEN:
    raise ValueError("BOT_TOKEN Environment Variable topilmadi!")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

samimiy = [
    "<b>💗 MARJONA, BILASANMI?</b>\n\n"
    "Sen dunyodagi eng zo'r do'stsan! 🥹 "
    "Shu paytgacha uchratgan do'stlarim orasida "
    "eng zo'risan. Sen juda chiroyli, samimiy va "
    "go'zal qizsan. Hamma tomondan ideal qizsan! 🌸\n\n"
    "Doim shunday ajoyib bo'lib yur! 🦋❤️",

    "<b>🌷 SEN HAQIQATAN HAM AJOYIBSAN!</b>\n\n"
    "Sening kulishing, samimiyliging va fe'l-atvoring "
    "juda ham yoqimli. Sen bilan do'st bo'lish "
    "haqiqiy omad! 💕 Hech qachon o'zingni "
    "boshqalar bilan solishtirma, sen o'zingcha zo'rsan! 👑",

    "<b>🥹 MARJONA, SEN BETAKTORSAN!</b>\n\n"
    "Senga o'xshagan samimiy va chiroyli insonlar "
    "juda kam uchraydi. Kulganingda yanada chiroyli "
    "bo'lib ketasan! 😍 Doim kulib yur, senga "
    "tabassum juda yarashadi! 💗"
]

tilaklar = [
    "<b>🌸 MARJONA, SENGA TILAGIM...</b>\n\n"
    "Har bir kuning quvonch bilan boshlangan bo'lsin. "
    "Orzularing birin-ketin amalga oshsin. "
    "Ko'zlaring faqat baxtdan porlasin, yuzingdan "
    "tabassum hech qachon arimasin. 🥰\n\n"
    "Hayoting go'zal xotiralar va yaxshi insonlarga "
    "to'la bo'lsin! 💗🦋",

    "<b>💐 ENG CHIROYLI TILAKLARIM SENGA!</b>\n\n"
    "Doimo sog'-salomat, baxtli va omadli bo'l. "
    "Hech qachon xafa bo'lma, barcha niyatlaring "
    "amalga oshsin. Har bir yangi kun senga "
    "yangi quvonch olib kelsin! ❤️✨",

    "<b>🦋 MARJONA, DOIM SHUNDAY KULIB YUR!</b>\n\n"
    "Senga cheksiz baxt, omad, xotirjamlik va "
    "eng go'zal kunlarni tilayman. Atrofingda "
    "doimo seni qadrlaydigan insonlar bo'lsin. "
    "Hayoting doim gullab-yashnasin! 🌷💗"
]

marjona_haqida = [
    "<b>👑 MARJONA — TAKRORLANMAS INSON!</b>\n\n"
    "💎 Go'zallik — o'ziga yarashgan!\n"
    "🌸 Samimiylik — o'ziga xos!\n"
    "🦋 Xarakter — betakror!\n"
    "💗 Tabassum — juda chiroyli!\n"
    "✨ Do'stlik — bebaho!\n\n"
    "<b>Marjona, sen haqiqatan ham o'zgachasan!</b> 🥹",

    "<b>💖 MARJONA HAQIDA 7 TA FAKT</b>\n\n"
    "1. 👑 Takrorlanmas qiz!\n"
    "2. 🌷 Juda chiroyli!\n"
    "3. 💎 Samimiy va mehribon!\n"
    "4. 🦋 O'ziga xos xarakter egasi!\n"
    "5. 😍 Kulishi juda yoqimli!\n"
    "6. 💗 Ajoyib do'st!\n"
    "7. ✨ O'zicha ideal inson!",

    "<b>🥰 MARJONA — ALOHIDA BIR OLAM!</b>\n\n"
    "Sen dunyodagi hamma qizlardan farq qilasan. "
    "Sening o'ziga xosliging, samimiyliging va "
    "go'zalliging seni yanada betakror qiladi.\n\n"
    "<b>Sen kabi inson boshqa takrorlanmaydi!</b> 👑💗"
]


def menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💗 Samimiy so'zlar", callback_data="samimiy")],
        [InlineKeyboardButton("🌸 Tilak", callback_data="tilak")],
        [InlineKeyboardButton("👑 Marjona haqida", callback_data="about")]
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "<b>🌸 ASSALOMU ALAYKUM, MARJONA! 🌸</b>\n\n"
        "💗 Senga atab kichkina sovg'a tayyorlandi.\n\n"
        "Bu yerda seni kutayotgan samimiy so'zlar, "
        "go'zal tilaklar va sen haqingdagi "
        "ajoyib fikrlar bor! 🥹🦋\n\n"
        "<b>O'zingga yoqqan bo'limni tanla:</b> 👇",
        reply_markup=menu(),
        parse_mode=ParseMode.HTML
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "samimiy":
        text = random.choice(samimiy)
    elif query.data == "tilak":
        text = random.choice(tilaklar)
    elif query.data == "about":
        text = random.choice(marjona_haqida)
    else:
        return

    await query.message.reply_text(
        text,
        reply_markup=menu(),
        parse_mode=ParseMode.HTML
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "<b>💗 MARJONA BOT</b>\n\n"
        "/start — Botni boshlash 🌸\n"
        "/help — Yordam 🦋",
        parse_mode=ParseMode.HTML
    )


# Aiohttp web-server
async def home(request):
    return web.Response(
        text="💗 MARJONA BOT ISHLAYAPTI!",
        content_type="text/plain"
    )


async def start_web_server():
    app = web.Application()
    app.router.add_get("/", home)
    app.router.add_get("/health", home)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

    logging.info(f"Web-server {PORT} portda ishga tushdi!")

    return runner


async def main():
    # Telegram bot
    bot = Application.builder().token(TOKEN).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("help", help_command))
    bot.add_handler(CallbackQueryHandler(buttons))

    # Web-server va bot bir vaqtda ishga tushadi
    runner = await start_web_server()

    try:
        await bot.initialize()
        await bot.start()
        await bot.updater.start_polling()

        logging.info("💗 MARJONA BOT ISHLAYAPTI!")

        # Dastur ishlashda davom etadi
        await asyncio.Event().wait()

    finally:
        if bot.updater and bot.updater.running:
            await bot.updater.stop()

        if bot.running:
            await bot.stop()

        await bot.shutdown()
        await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())


