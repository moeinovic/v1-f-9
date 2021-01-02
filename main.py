import os
from pyrogram import Client
plugins = dict(root="plugins")
API_ID = os.environ.get('APP_ID')
API_HASH = os.environ.get('APP_HASH')
TOKEN = os.environ.get('TOKEN')
Client("bot", api_id=int(API_ID), api_hash=API_HASH, bot_token=TOKEN, plugins=plugins).run()
