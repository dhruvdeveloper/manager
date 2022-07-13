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
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝙄 𝘼𝙈 𝙒𝙄𝙇𝘿 ✘ 𝘽𝙊𝙏​**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **𝙈𝙔 𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍​ : [ 𝘼𝘼𝙆𝘼𝙎𝙃 «🇮🇳»](https://t.me/aakashx0)** \n\n"
    TEXT += f"» **𝙇𝙄𝘽𝙍𝘼𝙍𝙔 𝙑𝙀𝙍𝙄𝙎𝙊𝙉 :** `{telever}` \n\n"
    TEXT += f"» **𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 𝙑𝙀𝙍𝙎𝙄𝙊𝙉 :** `{tlhver}` \n\n"
    TEXT += f"» **𝙋𝙔𝙍𝙊𝙂𝙍𝘼𝙈 𝙑𝙀𝙍𝙎𝙄𝙊𝙉 :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/wildxbot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/WildXbotsupport"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)

__mod_name__ = "Aʟɪᴠᴇ"


