# import telebot
# from telebot.types import *
# bot = telebot.TeleBot("5112589112:AAF6PnLfizdKNrGMMJxhF7Js_Jnj8a-sre0")


# data = { 
#     "user": {},
#     "admin": [],
#     "type": {}

# }


# def get_keyboard():
#     return ReplyKeyboardMarkup(resize_keyboard=True).add(
#         KeyboardButton("🗒Ro'yxatdan o'tish🗒")
#     )


# def inline():
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     btn1 = InlineKeyboardButton('🇺🇿Uz', callback_data='uz')
#     btn2 = InlineKeyboardButton('🇷🇺Pус', callback_data='rus')
#     keyboard.add(btn1,btn2)
#     return keyboard

# @bot.callback_query_handler(func=lambda x: x.data =="uz")
# def Uz(call):
#     if call.data == "uz":
#         bot.send_message(call.message.chat.id,f"{call.from_user.first_name} ro'yxatdan o'ting",reply_markup=get_keyboard())




# def get_inlinekeyboard():
#     keyboard = InlineKeyboardMarkup(row_width=1)
#     first_name = InlineKeyboardButton("📝Ism", callback_data="first_name+1")
#     last_name = InlineKeyboardButton("📝Familiya", callback_data="last_name+1")
#     phone = InlineKeyboardButton('📱Telefon nomer', callback_data="phone+1")
#     return keyboard.add(first_name, last_name, phone)




# def update_type(message):
#     user_id = message.chat.id
#     user_type = data['type'][user_id]
#     text = message.text
#     if user_type == 'phone':
#         if text.startswith("+998") and len(text) == 13 and text[1:].isdigit():
#             data["user"][user_id][user_type] = message.text
#             bot.send_message(user_id, "Sizning kiritgan malumotigiz qabul qilindi")
#         else:
#             bot.send_message(user_id, "Boshqatdan telefon nomerni kiriting")
#             bot.register_next_step_handler(message, update_type)
#     else:
#         if text.isalpha():
#             data["user"][user_id][user_type] = message.text
#             bot.send_message(user_id, "Sizning kiritgan malumotigiz qabul qilindi")
#         else:
#             type = {
#                 "first_name": "Ism",
#                 "last_name": "Familiya"
#             }
#             bot.send_message(user_id, f"Boshqatdan {type[user_type]} kiriting")
#             bot.register_next_step_handler(message, update_type)



# @bot.callback_query_handler(func=lambda x: x.data.split("+")[-1] == "1")
# def update_user_data(call):
#     type_user = call.data.split("+")[0]
#     user_id = call.message.chat.id
#     data['type'][user_id] = type_user
#     type = {
#         "first_name": "📝Ism",
#         "last_name": "📝Familiya",
#         "phone": "📱Telefon nomer"
#     }
#     bot.edit_message_text(
#         f"{type[type_user]} kiriting",
#         call.message.chat.id,
#         call.message.id
#     )
#     bot.register_next_step_handler(call.message, update_type)


# def data_text(message):
#     user_data = data["user"][message.chat.id]
#     print(user_data)
#     if user_data:
#         text = f"Ism: {user_data['first_name']}\n" \
#                f"Familiya: {user_data['last_name']}\n" \
#                f"Telefon nomer: {user_data['phone']}"
#         return text
#     data["user"][message.chat.id] = {
#         "first_name": "-",
#         "last_name": "-",
#         "phone": "-"
#     }
#     return "📝Ism: -\n" \
#            "📝Familiya: -\n" \
#            "📱Telefon nomer: -"


# @bot.message_handler(func=lambda x: x.text == "🗒Ro'yxatdan o'tish🗒")
# def registration(message):
#     text = data_text(message)
#     bot.send_message(message.chat.id, f"{text}", reply_markup=get_inlinekeyboard())






# @bot.message_handler(commands=['start'])
# def start(message):
#     if message.chat.id not in data["user"]:
#         data["user"][message.chat.id] = {}
#     bot.send_message(message.chat.id, f"Assalomu alaykum {message.chat.first_name}\n Tilni tanlang👇🏻👇🏻👇🏻", reply_markup=inline())





# bot.polling()



















# import telebot
# from telebot import types 
# import requests
# bot = telebot.TeleBot('5274342109:AAG5VvUsMSpslWxoi4HMr-h5mXvkMKGJyeU')
# @bot.message_handler(commands=['start'])
# def first_msg(message):
#        maac = types.InlineKeyboardMarkup()
#        vodka = types.InlineKeyboardButton(text='👨‍💻Admin',url='https://t.me/kh4mz4')
#        maac.row_width = 2 
#        maac.add(vodka)
#        bot.send_message(message.chat.id,text=f'*Assalomu Alaykum {message.from_user.first_name}\n- - - - - - - -\n👋Xush kelibsiz Instagramdan Video yuklash uchun\nVideo Link yuboring\n- - - - - - - -\nKanalimiz : https://t.me/ebomediaofficial\n\nBot : @Ovoz_li_bot*',parse_mode='markdown',reply_to_message_id=message.message_id,reply_markup=maac)
# @bot.message_handler(func=lambda m:True)
# def get(message):
#        bot.send_message(message.chat.id,f'<b>iltimos kuting Yuklanmoqda 🚀🚀</b>', parse_mode='html') 
#        msg = message.text 
#        url = requests.get(f'apilinki qoyiladi={msg}').json()['link'] 
#        text = '*Mana Sizning Videongiz\n- - - - - - - -\nKanalimiz : https://t.me/ebomediaofficial\n\nBot : @Ovoz_li_bot*' 
#        bot.send_video(message.chat.id,url,caption=text,parse_mode='markdown')
# bot.polling(True)

