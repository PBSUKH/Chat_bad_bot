from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import BOT_USERNAME, OWNER_ID
from pyrogram.types import InlineKeyboardButton as ib
import asyncio
from Badbot import app


START_TEXT = """
❤️ 𝗔𝗜 𝗕𝗢𝗧 🤖

**𝐇ᴇʟʟᴏ ⚘
━━━━━━━━━━━━━━━━━━━━━━━━
𝐈'ᴍ 𝐘ᴏᴜʀ 𝐅ʀɪᴇɴᴅʟʏ 𝐑ᴀɴᴋɪɴɢ 𝐀ɪ 𝐁ᴏᴛ 💬
━━━━━━━━━━━━━━━━━━━━━━━━━
🍃𝐔ʀ 𝐂ᴏᴍᴘᴀɴɪᴏɴ 𝐑ᴀɴᴋɪɴɢ 𝐁ᴏᴛ 𝐘ᴏᴜ 𝐂ᴀɴ 𝐒ʜᴀʀᴇ 𝐎ʀ 𝐓ʜᴏᴜɢʜᴛ 𝐖ɪᴛʜ 𝐌ᴇ 🏆
━━━━━━━━━━━━━━━━━━━━━━
𝐀ɴᴅ 𝐎ᴛʜᴇʀ 𝐀ɴʏ 𝐅ᴇᴀᴛᴜʀᴇs ❤️
━━━━━━━━━━━━━━━━━━━━━━━━━**"""

HELP_TEXT = """
❤️ 𝗔𝗜 𝗕𝗢𝗧 🤖

━━━━━━━━━━━━━━━━━━━━━━━━"""




@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    buttons = [
        [
            InlineKeyboardButton("•─╼⃝𖠁𝐀ᴅᴅ ◈ 𝐌ᴇ ◈ 𝐁ᴀʙʏ𖠁⃝╾─•", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("✯ 𝐒ᴜᴘʀᴏᴛ ✯", url=f"https://t.me/ll_THE_BAD_BOT_ll"),
            InlineKeyboardButton("✯ 𝐎ᴡɴᴇʀ ✯", user_id=OWNER_ID)
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_video(
        video="https://telegra.ph/file/82a0c010f573064a0ce59.mp4",
        caption=START_TEXT,
        reply_markup=reply_markup
    )



@app.on_message(filters.command("help") & filters.private)
async def start(client, message):
    buttons = [
        [
            InlineKeyboardButton("✯ 𝐒ᴜᴘʀᴏᴛ ✯", url=f"https://t.me/ll_THE_BAD_BOT_ll"),
            InlineKeyboardButton("✯ 𝐎ᴡɴᴇʀ ✯", user_id=OWNER_ID)
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_video(
        video="https://telegra.ph/file/82a0c010f573064a0ce59.mp4",
        caption=HELP_TEXT,
        reply_markup=reply_markup
    )
