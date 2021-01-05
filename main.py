import os
from pyrogram import Client, filters
from pyromod import listen
plugins = dict(root="plugins")
API_ID = int(os.environ.get('APIID'))
API_HASH = os.environ.get('APIHASH')
TOKEN = os.environ.get('TOKEN')
app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
@app.on_message(filters.command("start") & filters.private)
async def echo(c, m):
    answer = await app.listen(m.chat.id, timeout=30)
    await app.send_message(m.chat.id, answer.text)

app.run()
