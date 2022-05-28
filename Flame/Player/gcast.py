from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from config import SUDO_USERS
from Flame.main import Test, bot as Client

@Client.on_message(filters.command(["gcast", "post", "send"]))
async def broadcast(client, message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("Stɑɤtɩŋʛ Ɓɤøɑɗƈɑst ...")
        if not message.reply_to_message:
            await wtf.edit("Ƥɭɘɑsɘ Ʀɘƥɭy Ƭø ɑ Mɘssɑʛɘ Ƭø Stɑɤt Ɓɤøɑɗƈɑst ...")
            return
        lmao = message.reply_to_message.text
        async for dialog in Client.iter_dialogs():
            try:
                await Client.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"Ɓɤøɑɗƈɑstɩŋʛ \n\nSɘŋt Ƭø: {sent} Ƈɦɑts \nFɑɩɭɘɗ Iŋ: {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"Ɠƈɑst Sʋƈƈɘssfʋɭɭy \n\nSɘŋt Ƭø: {sent} Ƈɦɑts \nFɑɩɭɘɗ Iŋ: {failed} Ƈɦɑts")
