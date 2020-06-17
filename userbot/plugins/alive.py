"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**MY STATUS** \n`JARVIS IS:` **✅ Alive**\n\n"
                     "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n"
                     "`DATABASE STATUS:` **ALL NORMAL! WORKING FINE 🙂**\n`NO PROBLEM FOUND🔥!\n`"
                     "`J.A.R.V.I.S VERSION`: [2.0 JARVIS OS](https://t.me/VIKRAMADITYA1190)\n"
                     f"`MY BOSS`: {DEFAULTUSER}\n\n"
                     "ALWAYS WITH YOU MY BOSS\n\n"
                     "WANT THIS USERBOT\n\n"
                     "[⚡CONTACT 🅅🄸🄺🅁🄰🄼🄰🄳🄸🅃🅈🄰⚡](https://t.me/VIKRAMADITYA1190)") 

