#(©)CodeXBotz
#Recoded By @TopGroupChat



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7439771375:AAHyMLutgLhHLt8yhMDfd-pCEOJaIcVEhjY")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29486311"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ffdc688dc4eee8d2585cb24155188432")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001950756152"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6396921435"))

#Port
PORT = os.environ.get("PORT", "9172")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ucik:ucik@cluster0.0l3r8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "zooya2")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1001689707975"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001962418199"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1001706760136"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hai {mention}\n\nIni adalah bot file sharing\nKamu bisa mendapatkan video melalui link yang saya bagikan..!")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "1707380693 6396921435 6291921516").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", """
SILAHKAN JOIN TERLEBIH DAHULU KE CHANNEL YANG ADA DIBAWAH UNTUK MELIHAT FILE YANG SAYA BAGIKAN

JIKA SUDAH SILAHKAN TEKAN "COBA LAGI"

VVIP PEKOB : @VvipSchool
""")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Tolong jangan mengirimi saya pesan..!"

ADMINS.append(OWNER_ID)
ADMINS.append(6396921435)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
