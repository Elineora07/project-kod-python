import keyword
import telebot

from telebot.types import *

bot = telebot.TeleBot("5274342109:AAG5VvUsMSpslWxoi4HMr-h5mXvkMKGJyeU")



def start_register_keyboard(data):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Ro'yxatdan o'tish")
    return keyboard.add(btn)

bot.polling()