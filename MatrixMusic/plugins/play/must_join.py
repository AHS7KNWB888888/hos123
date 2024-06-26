from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from MatrixMusic import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/O_U_Q1":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("O_U_Q1", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/O_U_Q1".isalpha():
                link = "https://t.me/O_U_Q1"
            else:
                chat_info = await bot.get_chat("O_U_Q1")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ\n⌯︙قناة البوت: @O_U_Q1 .\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ᯓ 𝑺𝑶𝑼𝑹𝑪𝑬 𝟑 𝐓 𝐛", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat @O_U_Q1 !")
