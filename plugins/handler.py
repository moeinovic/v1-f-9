from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
def echo(client, message):
    message.reply("Hi Men)
