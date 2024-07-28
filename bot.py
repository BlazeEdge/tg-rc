from telebot import TeleBot, types
from os import system
from config import *

bot = TeleBot(TOKEN, 'markdown')

@bot.message_handler(commands=['start'])
def start_control(message):
    if message.from_user.username == OWNER_NICKNAME:
        markup = types.InlineKeyboardMarkup(row_width=2)
        item = types.InlineKeyboardButton('Ping', callback_data='ping')
        item0 = types.InlineKeyboardButton('Reboot', callback_data='reboot')
        item1 = types.InlineKeyboardButton('Shutdown', callback_data='poweroff')
        markup.add(item,item0,item1)

        bot.send_message(message.chat.id, 'Select the command:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'You don\'t own this PC')

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'ping':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'123ms') # this command is just a joke
        elif call.data == 'reboot':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Reboot...')
            system('systemctl reboot')
        elif call.data == 'poweroff':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Shutdown...')
            system('systemctl poweroff')

bot.infinity_polling()
