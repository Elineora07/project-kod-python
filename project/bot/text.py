# def register_text(user_id, data):
#     first_name = data['user'][user_id]['first_name']
#     last_name = data['user'][user_id]['last_name']
#     middle_name = data['user'][user_id]['middle_name']
#     phone = data['user'][user_id]['phone']
#     text = f"Ism: {first_name}\n" \
#            f"Familiya: {last_name}\n" \
#            f"Sharif: {middle_name}\n" \
#            f"Telefon raqam: {phone}"

#     return text





# @bot.message_handler(commands=['start'])
# def start_message(message):
#        bot.send_message(message.chat.id,"Salom rostdan ham Hayot beshavqat (HUMOYUN AKANI GAPI)")
# bot.polling()
# import telebot
# from telebot.types import *
# bot = telebot.TeleBot('5274342109:AAG5VvUsMSpslWxoi4HMr-h5mXvkMKGJyeU')
# @bot.message_handler(commands=['start'])
# def first_msg(message):
#        maac = InlineKeyboardMarkup() 
#        vodka = InlineKeyboardButton(text='👨‍💻Admin',url='https://t.me/kh4mz4') 
#        maac.row_width = 2 
#        maac.add(vodka) 
#        bot.send_message(message.chat.id,text=f'*Assalomu aleykum {message.from_user.first_name}\n- - - - - - - -\n👋Xush kelibsiz Instagramdan Video yuklash uchun\nVideo Link yuboring\n- - - - - - - -\nKanalimiz : https://t.me/ebomediaofficial\n\nBot : @Ovoz_li_bot*',parse_mode='markdown',reply_to_message_id=message.message_id,reply_markup=maac)@bot.message_handler(func=lambda m:True)
#        def get(message): 
#               bot.send_message(message.chat.id,f'<b>Iltimos kuting Yuklanmoqda 🚀🚀</b>', parse_mode='html') 
#        msg = message.text 
#        url = get(f'apilinki qoyiladi={msg}').json()['link'] 
#        text = '*Mana Sizning Videongiz\n- - - - - - - -\nKanalimiz : https://t.me/ebomediaofficial\n\nBot : @Ovoz_li_bot*' 
#        bot.send_video(message.chat.id,url,caption=text,parse_mode='markdown')
#bot.polling(True)













import telebot
from telebot import types 
import requests
bot = telebot.TeleBot('5274342109:AAG5VvUsMSpslWxoi4HMr-h5mXvkMKGJyeU')
@bot.message_handler(commands=['start'])
def first_msg(message):
       maac = types.InlineKeyboardMarkup()
       vodka = types.InlineKeyboardButton(text='👨‍💻Admin',url='https://t.me/kh4mz4')
       maac.row_width = 2 
       maac.add(vodka)
       bot.send_message(message.chat.id,text=f'*Assalomu Alaykum {message.from_user.first_name}\n- - - - - - - -\n👋Xush kelibsiz Instagramdan Video yuklash uchun\nVideo Link yuboring\n- - - - - - - -\nKanalimiz : https://t.me/ebomediaofficial\n\nBot : @Ovoz_li_bot*',parse_mode='markdown',reply_to_message_id=message.message_id,reply_markup=maac)
@bot.message_handler(func=lambda m:True)
def get(message):
       bot.send_message(message.chat.id,f'<b>iltimos kuting Yuklanmoqda 🚀🚀</b>', parse_mode='html') 
       msg = message.text 
       url = requests.get(f'apilinki qoyiladi={msg}').json()['link'] 
       text = '*Mana Sizning Videongiz\n- - - - - - - -\nKanalimiz : https://t.me/ebomediaofficial\n\nBot : @Ovoz_li_bot*' 
       bot.send_video(message.chat.id,url,caption=text,parse_mode='markdown')
bot.polling(True)

