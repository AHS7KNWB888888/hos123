from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝙶𝚁𝙾̀𝚄𝙿", url= "https://t.me/O_U_Q1"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="مطور البوت", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𝙶𝚁𝙾̀𝚄𝙿", url=f"https://t.me/O_U_Q1"), 
        ],
        [
            
            InlineKeyboardButton(text="𝑺𝑶𝑼𝑹𝑪𝑬 𝟑 𝐓 𝐛", url=f"https://t.me/O_U_1S") , 
        ],
    ]
    return buttons
