import random
import asyncio
from pyrogram import filters
from FallenRobot import pbot as FallenRobot

ABOUTOWNER_STRINGS = [
 "MY OWNER IS @aakashok... to know MORE ABOUT HIM CHECK OUT @ABOUT_AAKASH"
  ]
@FallenRobot.on_message(filters.command("owner"))
async def lel(bot, message):
    ran = random.choice(ABOUTOWNER_STRINGS)
    await bot.send_chat_action(message.chat.id, "typing")
    await asyncio.sleep(1.5)
    return await message.reply_text(text=ran)
  
__mod_name__ = "OWNER"

__help__ = """

ABOUT OWNER .
❍ /OWNER *:* ABOUT YOUR FATHER

 """
