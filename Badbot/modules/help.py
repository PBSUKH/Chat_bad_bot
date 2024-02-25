from pyrogram import filters
from Badbot import app, BOT_USERNAME
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Badbot.core.strings import (music_txt, ai_txt, bass_txt, youtube_txt, 
misc_txt, broadcast_txt, checker_txt, devs_txt, instagram_txt, spical_txt, sukh_txt)


# ------------------------------------------------------------------------------- #
start_txt = """
❤️ ʜᴇʟᴘ ᴍᴇɴᴜ sʜɪᴢᴜ ʙᴏᴛ 🤖"""
# ------------------------------------------------------------------------------- #

button = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✯ 𝐇ᴇʟᴘ ✯", callback_data="help_"),    
        ]
])



help_txt = """
❤️ ʜᴇʟᴘ ᴍᴇɴᴜ sʜɪᴢᴜ ʙᴏᴛ 🤖
"""



# ------------------------------------------------------------------------------- #

chizuru_buttons = [              
                [
                    InlineKeyboardButton("✯ ᴍᴜsɪᴄ ✯", callback_data="music_"),   
                    InlineKeyboardButton("✯ ᴀɪ ✯", callback_data="ai_")
                    ],
                [
                    InlineKeyboardButton("✯ ʙᴀss ✯", callback_data="bass_"),
                    InlineKeyboardButton("✯ ʏᴏᴜᴛᴜʙᴇ ✯", callback_data="youtube_")
                ],
                [
                    InlineKeyboardButton("✯ ᴍɪsᴄ ✯", callback_data="misc_"),
                    InlineKeyboardButton("✯ ʙʀᴏᴀᴅᴄᴀsᴛ ✯", callback_data="broadcast_")
                ],
                [
                    InlineKeyboardButton("✯ ᴄʜᴇᴄᴋᴇʀ ✯", callback_data="checker_"),   
                    InlineKeyboardButton("✯ ʙᴀᴅ ✯", callback_data="devs_")
                ],
                [
                    InlineKeyboardButton("✯ ɪɴsᴛᴀɢʀᴀᴍ ✯", callback_data="instagram_"),
                    InlineKeyboardButton("✯ ᴡʜɪsᴘᴇʀ ✯", callback_data="sukh_")
                ],
               [
                       InlineKeyboardButton("✯ sʜɪᴢᴜ ʙᴏᴛ ✯", callback_data="spical_")
               ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home_"),
                    InlineKeyboardButton("⟲ ᴄʟᴏꜱᴇ ⟳", callback_data="close_data")
                ]
                ]


back_buttons  = [[
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_"),                    
                ]]






@app.on_message(filters.command("help"))
async def start(_,message):
  await message.reply_photo("https://telegra.ph/file/0dc614ca84cd66d235352.jpg",
                            caption=start_txt.format(message.from_user.mention),reply_markup=button)



@app.on_callback_query()
async def cb_handler(client, query):
    if query.data=="home_":
        buttons = [
            [
                                InlineKeyboardButton("✯ 𝐇ᴇʟᴘ ✯", callback_data="help_")
            ]    
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                start_txt.format(query.from_user.mention),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
                


# ------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------- #
    elif query.data=="help_":        
        reply_markup = InlineKeyboardMarkup(chizuru_buttons)
        try:
            await query.edit_message_text(
                help_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
    elif query.data=="music_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                music_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="ai_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                ai_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="bass_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                bass_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="youtube_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                youtube_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
        
    elif query.data=="misc_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                misc_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


        
    elif query.data=="broadcast_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                broadcast_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="checker_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                checker_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
    elif query.data=="devs_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                devs_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass        



    elif query.data=="instagram_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                instagram_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

elif query.data=="sukh_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                sukh_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass 
            
            
elif query.data=="spical_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                spical_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass 

    
# ------------------------------------------------------------------------------- #

    elif query.data=="maintainer_":
            await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)

  
# ------------------------------------------------------------------------------- #
 
    elif query.data=="close_data":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

                    
