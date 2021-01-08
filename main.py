import os
from pyrogram import Client, filters
from pyromod import listen
plugins = dict(root="plugins")
API_ID = int(os.environ.get('APIID'))
API_HASH = os.environ.get('APIHASH')
TOKEN = os.environ.get('TOKEN')
Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, plugins=plugins).run()
