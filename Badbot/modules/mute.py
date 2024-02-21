from Badbot import app ,BOT_USERNAME, SUDO_USER
from pyrogram import filters
from pyrogram.types import ChatPermissions


@app.on_message(filters.command("muteall") & filters.user(SUDO_USER))
async def mute_all(_,msg):
    chat_id=msg.chat.id    
    bot=await app.get_chat_member(chat_id,BOT_USERNAME)
    bot_permission=bot.privileges.can_restrict_members==True    
    if bot_permission:
        async for member in app.get_chat_members(chat_id):       
            try:
                    await app.restrict_chat_member(chat_id, member.user.id,ChatPermissions(can_send_messages=False))
                    await msg.reply_text(f"𝐖ʟᴄ 𝐁ᴀʙʏ 🥺❤️ {member.user.mention}")
                                        
            except Exception:
                pass
    else:
        await msg.reply_text(" 𝐁𝐀𝐁𝐘 𝐘𝐄 𝐊𝐘𝐀 𝐊𝐈𝐀 ")  
                                         
    


