from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
@Client.on_message(filters.command("start") & filters.private)
async def echo(c, m):
	await c.send_message(m.chat.id, '*Hello My Friend*', parse_mode="MarkDown")
