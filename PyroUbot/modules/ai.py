from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴏᴘᴇɴᴀɪ"
__HELP__ = """
<blockquote><b>Bantuan Untuk AI

perintah : <code>{0}ask</code>
    buat pertanyaan contoh <code>{0}ask</code> dimana letak Antartika</b></blockquote>
"""


@PY.UBOT("ask")
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : ask bagaimana membuat donat?"
            )
        else:
            prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji>proccesing....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://widipe.com/gpt4?text={a}')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"{x}\n\n<emoji id=5208727996315220567>✅</emoji>**pertanyaan ini dijawab oleh** {bot.me.mention}"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
      
