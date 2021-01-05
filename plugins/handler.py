from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
@Client.on_message(filters.command("start") & filters.private)
async def echo(c, m):
    answer = await c.ask(m.chat.id, '*Send me your name:*', parse_mode='Markdown')
    await c.send_message(m.chat.id, f'Your name is: {answer.text}')
