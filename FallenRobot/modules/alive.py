import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot, SUPPORT_CHAT, OWNER_USERNAME, dispatcher


PHOTO = [
    "https://telegra.ph/file/6a21ea6677342f43b363e.jpg",
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Êá´Êâ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nð ð¼ð {dispatcher.bot.first_name}**\nâââââââââââââââââââ\n\n"
    TEXT += f"Â» **á´Ê á´á´á´ á´Êá´á´á´Êâ : [ð¼ð¼ðð¼ððÂ«ð®ð³Â»](https://t.me/notaakash)** \n\n"
    TEXT += f"Â» **ÊÉªÊÊá´ÊÊ á´ á´ÊsÉªá´É´ :** `{telever}` \n\n"
    TEXT += f"Â» **á´á´Êá´á´Êá´É´ á´ á´ÊsÉªá´É´ :** `{tlhver}` \n\n"
    TEXT += f"Â» **á´ÊÊá´É¢Êá´á´ á´ á´ÊsÉªá´É´ :** `{pyrover}` \nâââââââââââââââââ\n\n"
    BUTTON = [
        [
            Button.url("Êá´Êá´â", f"https://t.me/wildx_bot?start=help"),
            Button.url("sá´á´á´á´Êá´â", f"https://t.me/gfc_support"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


__mod_name__ = "AÊÉªá´ á´"
