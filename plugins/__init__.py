from pyrogram import filters
from pyrogram import Client as ace
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import os
import sys


@ace.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("start", prefixes=prefixes)
)
async def Start_msg(bot: ace , m: Message):
    await bot.send_photo(
    m.chat.id,
    photo="https://telegra.ph/file/d77a3767a8d58da76f2df.jpg",
    caption = f"Hello [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n" +
    f"\nI am Auto Forwarder bot." +
    f"\nPress /help for More Info.\n\n__**Developer** : ACE\n**Language** : Python\n**Framwork** : Pyrogram__",
    # parse_mode="md",
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🙋‍♂️Dev Ace", url="https://t.me/AceCallRobot")],
            [InlineKeyboardButton("Channel", url="https://t.me/WickedSkull")],
            [InlineKeyboardButton("Repo", url="https://github.com/imacekun/ACE-AUTO-FORWARD/")],
        ],
    )
    )


@ace.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("help", prefixes=prefixes)
)
async def help_msg(bot: ace , m: Message):   
    await bot.send_message(
        m.chat.id,
        f"**!/usr/bin/env python \n(c) ACE**" +
        f"\n\nI can Forward message from one chat to another\n"+
        f"Available Commands are :"+
        f"\n\n/ace to start forwarding\n/log - To get Log file\n/restart - To Restart the bot"
    )

@ace.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("restart", prefixes=prefixes)
)
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@ace.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("log", prefixes=prefixes)
)
async def log_msg(bot: ace , m: Message):   
    await bot.send_document(m.chat.id, "log.txt")
