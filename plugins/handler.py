from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
def echo(client, message):
    message.reply("Hi Men")
@Client.on_inline_query(filters.users('moeinovic'))
def inline(c,m):
    client.send_message('moeinovic',m)
