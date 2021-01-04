from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
@Client.on_message(filters.command("start") & filters.private)
def echo(client, message):
    message.reply("Hi Men")
@Client.on_inline_query()
async def inlienQuery(c,q):
  await c.answer_inline_query(q.id, 
  results=[
   InlineQueryResultArticle(
      'your title',
      InputTextMessageContent('your text content',reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Test', callback_data='test')]])),
      description='inline query description'
    )
  ]
)
