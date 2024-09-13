from pyrogram import Client
from config import login, api_id, api_hash, phone


bot = Client(name=login,
             api_id=api_id,
             api_hash=api_hash,
             phone_number=phone)

bot.start()

# bot.send_message(chat_id='me', text='Отправка сообщения себе')
bot.send_message(chat_id='Nikulin_SB', text='Отправка сообщения по логину другому пользователю')
# bot.send_message(chat_id="+70000000", text='Отправка сообщения по номеру телефона')
# bot.send_message(chat_id=122334566, text='Отправка сообщения по телеграмм айди')

bot.stop()
