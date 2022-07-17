# import telebot
# from telebot.types import *
# bot = telebot.TeleBot("5112589112:AAF6PnLfizdKNrGMMJxhF7Js_Jnj8a-sre0")


# data = { 
#     "admin_id": 895752511 ,
#     "user_phone" : [],
#     "user_name" : []
#     }

# def inline():
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     btn1 = InlineKeyboardButton('Uz', callback_data='uz')
#     btn2 = InlineKeyboardButton('Pус', callback_data='rus')
#     keyboard.add(btn1,btn2)
#     return keyboard

# @bot.callback_query_handler(func=lambda x: x.data =="uz")
# def Uz(call):
#     if call.data == "uz":
#         bot.send_message(call.message.chat.id,f"{call.from_user.first_name} ro'yxatdan o'ting",reply_markup=get_keyboard())
# def i_dont_know(message):
#     name = message.text + 1
#     if not(name.isalpha() and len(name)>3):
#         bot.send_message(message.chat.id , "Ism xato kiritildi qaytib kiriting")
#         bot.register_next_step_handler(message,i_dont_know)
#     else :
#         bot.send_message(message.chat.id , "Ro'yxatdan o'tdingiz", reply_markup=get_keyboard())
#     print(name)
    


# def registration(message):
#     text = message.text
#     if not(text[1:].isdigit() and len(text) == 13 and text.startswith("+998")):
#         bot.send_message(message.chat.id , "Siz noto'g'ri raqam kiritdingiz qaytib kiriting")
#         bot.register_next_step_handler(message, registration)
#     else :
#         bot.send_message(message.chat.id , "Ismingizni kiriting")
#         bot.send_message(message.chat.id, "...", reply_markup=ReplyKeyboardRemove())
#         bot.delete_message(message.chat.id,message.id + 3)
#         data["user_phone"] += [text]
#         bot.send_message(data["admin_id"],text)
#     bot.register_next_step_handler(message,i_dont_know)    

# @bot.message_handler(func=lambda x: x.text == "Ro'yxatdan o'tish" )
# def royxat(message):
#     bot.send_message(message.chat.id, "Telefon nomeringizni kiriting.\nMasalan:+998903314455")
#     bot.send_message(message.chat.id, "...", reply_markup=ReplyKeyboardRemove())
#     bot.delete_message(message.chat.id,message.id + 2)
#     bot.register_next_step_handler(message, registration)
    




























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













































# from unicodedata import name
# import telebot
# from telebot.types import *
# bot = telebot.TeleBot("5112589112:AAF6PnLfizdKNrGMMJxhF7Js_Jnj8a-sre0")
# import datetime
# day = datetime.datetime.now().weekday()
# week = ["dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba", "yakshanba"]
# a = week[day:] + week[:day]

# import calendar
# year = int(str((datetime.datetime.now()))[:4])
# month = int(str((datetime.datetime.now()))[5:7])
# calendar_ = calendar.month(year, month).split("\n")
# data = { 
#     "admin_id": 895752511 ,
#     "user_phone" : [],
#     "user_name" : []
#     }
# def i_dont_know(message):
#     name = message.text + 1
#     if not(name.isalpha() and len(name)>3):
#         bot.send_message(message.chat.id , "Ism xato kiritildi qaytib kiriting")
#         bot.register_next_step_handler(message,i_dont_know)
#     else :
#         bot.send_message(message.chat.id , "Ro'yxatdan o'tdingiz")
#     print(name)
    
# def gi_keyboard():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     btn = KeyboardButton("Vaqt band qilish")
#     keyboard.add(btn)
#     return keyboard

# def registration(message):
#     text = message.text
#     if not(text[1:].isdigit() and len(text) == 13 and text.startswith("+998")):
#         bot.send_message(message.chat.id , "Siz noto'g'ri raqam kiritdingiz qaytib kiriting")
#         bot.register_next_step_handler(message, registration)
#     else :
#         bot.send_message(message.chat.id , "Ismingizni kiriting")
#         bot.send_message(message.chat.id, "...", reply_markup=ReplyKeyboardRemove())
#         bot.delete_message(message.chat.id,message.id + 3)
#         data["user_phone"] += [text]
#         bot.send_message(data["admin_id"],text)
#     bot.register_next_step_handler(message,i_dont_know)    

# @bot.message_handler(func=lambda x: x.text == "Ro'yxatdan o'tish" )
# def royxat(message):
#     bot.send_message(message.chat.id, "Telefon nomeringizni kiriting.\nMasalan:+998941255443")
#     bot.send_message(message.chat.id, "...", reply_markup=ReplyKeyboardRemove())
#     bot.delete_message(message.chat.id,message.id + 2)
#     bot.register_next_step_handler(message, registration)
    


# @bot.message_handler(commands='start')
# def send_welcome(message):
# 	bot.send_message(message.chat.id, f"Assalomu alaykum {message.chat.first_name} \nZarangari arenaga vaqt band qilishingiz \nuchun Ro'yxatdan o'tish tugmasi orqali ro'yxatdan o'ting",reply_markup=get_keyboard())
# @bot.message_handler(func=lambda x: x.text == "Vaqt band qilish" )
# def vaqt(message):
#     bot.send_message(message.chat.id, "...", reply_markup=ReplyKeyboardRemove())
#     bot.delete_message(message.chat.id, message.id + 1)
#     bot.send_message(message.chat.id, "       O'yin kunni tanlang       ", reply_markup=vaqt())

# def in_keyboard():
#     keyboard = InlineKeyboardMarkup()
#     month = (calendar_[0].split(" ")[3].lower())
#     day  = (datetime.datetime.now().day) -1
#     for s in a:
#         btn = InlineKeyboardButton(f'{s}\n{day + 1} {month}', callback_data=f"in_keyboard__{s}")
#         day += 1
#         keyboard.add(btn)
#     return keyboard
# def get_keyboard():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = KeyboardButton("Ro'yxatdan o'tish")
#     keyboard.add(btn1)
#     return keyboard



# bot.polling()

































# import telebot
# from telebot.types import *

# bot = telebot.TeleBot("")


# data = {
#     "user": {},
#     "admin": [],
#     "type": {}
# }


# def get_keyboard():
#     return ReplyKeyboardMarkup(resize_keyboard=True).add(
#         KeyboardButton("Ro'yxatdan o'tish")
#     )


# def get_inlinekeyboard():
#     keyboard = InlineKeyboardMarkup(row_width=1)
#     first_name = InlineKeyboardButton("Ism", callback_data="first_name+1")
#     last_name = InlineKeyboardButton("Familiya", callback_data="last_name+1")
#     phone = InlineKeyboardButton('Telefon nomer', callback_data="phone+1")
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
#         "first_name": "Ism",
#         "last_name": "Familiya",
#         "phone": "Telefon nomer"
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
#     return "Ism: -\n" \
#            "Familiya: -\n" \
#            "Telefon nomer: -"


# @bot.message_handler(func=lambda x: x.text == "Ro'yxatdan o'tish")
# def registration(message):
#     text = data_text(message)
#     bot.send_message(message.chat.id, f"{text}", reply_markup=get_inlinekeyboard())


# @bot.message_handler(commands="start")
# def start(message):
#     print(message.chat.id)
#     if message.chat.id in data["admin"]:
#         bot.send_message(message.chat.id, f"salom {message.from_user.first_name}", reply_markup=admin_keyboard())
#     else:
#         if message.chat.id not in data['user']:
#             data["user"][message.chat.id] = {}
#         bot.send_message(message.chat.id, f"salom {message.from_user.first_name}", reply_markup=get_keyboard())


# def admin_keyboard():
#     return ReplyKeyboardMarkup(resize_keyboard=True).add(
#         KeyboardButton("Ro'yxat")
#     )


# bot.polling()