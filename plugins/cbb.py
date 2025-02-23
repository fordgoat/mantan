#(©)Codexbotz
#Recoded By @TopGroupChat

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""
𝗣𝗥𝗜𝗖𝗘 𝗟𝗜𝗦𝗧 𝗩𝗩𝗜𝗣 💰

— VVIP INDO : Rp. 50.000,-
— VVIP HIJAB : Rp. 50.000,-
— VVIP ONLYFANS : Rp. 55.000,-
— VVIP CAMPURAN : Rp. 50.00,-
— VVIP JAV HD : Rp. 50.000,-
— VVIP LIVE RECORD : Rp. 50.000,-
— VVIP PELAJAR : Rp. 55.000,-
— VVIP BARAT : Rp. 50.000,-

— VVIP PREMIUM SULTAN : Rp. 150.000,-

PROMO HEMAT 🪙
— Rp. 325.000 TAKE ALL CHANNNEL VVIP NO PREMIUM
— Rp. 450.000 TAKE ALL CHANNEL VVIP + PREMIUM SULTAN

PC @kilashikii
            """,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("TUTUP", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
