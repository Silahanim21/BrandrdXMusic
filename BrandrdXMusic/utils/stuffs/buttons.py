from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("chat-gpt", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("detaylar", callback_data="mplus HELP_History"),InlineKeyboardButton("akış", callback_data="mplus HELP_Reel")],
    [InlineKeyboardButton("info", callback_data="mplus HELP_Info"),InlineKeyboardButton("ekstra", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("ᴄᴏᴜᴘʟᴇꜱ", callback_data="mplus HELP_Couples"),
    InlineKeyboardButton("astion", callback_data="mplus HELP_Action"),InlineKeyboardButton("arama", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("yazı tipi", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("bot", callback_data="mplus HELP_Bots"),InlineKeyboardButton("Ⓣ-graph", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("kaynak kod", callback_data="mplus HELP_Source"),
    InlineKeyboardButton("türe", callback_data="mplus HELP_TD"),InlineKeyboardButton("qoiz", callback_data="mplus HELP_Quiz")], 
    [InlineKeyboardButton("ᴛᴛs", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("radyo", callback_data="mplus HELP_Radio"),InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("◁", callback_data=f"settings_back_helper"),
     InlineKeyboardButton("↻ geri ↻", callback_data=f"mbot_cb"), 
    InlineKeyboardButton("▷", callback_data=f"managebot123 settings_back_helper"),
    ]]
