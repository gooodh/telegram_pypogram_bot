import os

from dotenv import load_dotenv

from pyrogram import Client

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')
login = os.getenv('LOGIN')


bot = Client(name=login, api_id=api_id, api_hash=api_hash, phone_number=phone)
bot.run()

