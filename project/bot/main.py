# import telebot
# from telebot import types
# from telebot.types import *

# bot = telebot.TeleBot("5266261551:AAFmF1WZH6UONiuqMblxbSwsPAGKlRlnRe0")
# @bot.message_handler(commands=["start"])
# def send_welcome(message):
#     username = message.from_user.username
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton(text="🎞Kino🎞")
#     btn2 = types.KeyboardButton(text="🅿️👩🏻‍💻Pycharm🅿️👩🏻‍💻")
#     btn3 = types.KeyboardButton(text="🎧🎵Musiqa🎧🎵")
#     keyboard.add(btn1,btn2,btn3)
#     bot.send_message(message.chat.id,f"Assalomu aleykum. {username}\n 🔊Ovoz_li🔊botimizga \n 🎉🎉Xush kelibsiz!!!🎉🎉!!! \n Sizni qiziqtirgan tugmani tanlang:",reply_markup=keyboard)


# @bot.message_handler(content_types=["text"])
# def start_text(message):
#     if message.text =="🎞Kino🎞":
#         keyboard = types.InlineKeyboardMarkup()
#         url1 = types.InlineKeyboardButton(text="Liga Adjustise 2021",url="https://t.me/Tudum_Netflix/247")
#         url2 = types.InlineKeyboardButton(text="Liga Adjustise 2017",url="https://t.me/Tudum_Netflix/245")
#         url3 = types.InlineKeyboardButton(text="Forsag 9",url="https://t.me/Tudum_Netflix/242")
#         url4 = types.InlineKeyboardButton(text="Infinity",url="https://t.me/Tudum_Netflix/234")
#         url5 = types.InlineKeyboardButton(text="⬅⬅Menyuga qaytish",callback_data = "⬅⬅Orqaga")
#         keyboard.add(url1,url2,url3,url4,url5)
        
#         bot.send_message(message.chat.id,"Filmingizni tanlang:",reply_markup=keyboard)
    

#     if message.text =="🅿️👩🏻‍💻Pycharm🅿️👩🏻‍💻":
#         keyboard = types.InlineKeyboardMarkup()
#         key_yes = types.InlineKeyboardButton(text="Yes",callback_data='yes')
#         keyboard.add(key_yes)
#         key_no = types.InlineKeyboardButton(text="No",callback_data='no')
#         keyboard.add(key_no)

#         question = f"PyCharm-ni o'rnatmoqchimisiz?"
#         bot.send_message(message.from_user.id,text = question, reply_markup = keyboard)
        
        
               
#     if message.text =="🎧🎵Musiqa🎧🎵":
#         keyboard = types.InlineKeyboardMarkup()
#         url1 = types.InlineKeyboardButton(text="Bir necha musiqa",url="https://t.me/vkm_bot")
#         url2 = types.InlineKeyboardButton(text="Uzbek musiqalari",url="https://t.me/Uzbek_zakaz_music_qo_shiqlar")
#         url3 = types.InlineKeyboardButton(text="Arab musiqalari",url="https://t.me/bass_muzikil999")
#         url4 = types.InlineKeyboardButton(text="Rus musiqalari",url="https://t.me/russianmuiscnews")
#         url5 = types.InlineKeyboardButton(text="⬅⬅Menyuga qaytish",callback_data = "⬅⬅Orqaga")
#         keyboard.add(url1,url2,url3,url4,url5)
    
#         bot.send_message(message.chat.id,"Musiqangizni tanlang:",reply_markup=keyboard)


# @bot.callback_query_handler(func=lambda call:True)
# def get_call(call):
#     username = call.message.from_user.username
#     if call.data == "Orqaga":
#         send_welcome(call.message)

#     if call.data== "yes": 
#         bot.send_message(call.message.chat.id,"https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows")
#     elif call.data== "no": 
#         bot.send_message(call.message.chat.id,f"Yana {username}, da ko'rishguncha..!!!✋🏻✋🏻✋🏻")
#         bot.register_next_step_handler(call.message,send_welcome)

# bot.polling()








# import telebot
# from telebot.types import *
# 
# 
# bot = telebot.TeleBot("5113084134:AAE1Pm_3YzMYEwu0jKVEVUukLVzs4tEwLBs")
# 
# 
# 
# data = {
    # "user": {},
    # "admin": [],
    # "type": {}
    # 
# }
# 
# 
# 
# def get_keyboard():
    # return ReplyKeyboardMarkup(resize_keyboard=True).add(
        # KeyboardButton("Ro'yxatdan o'tish")
    # )
    # 
# 
# def get_inlinekeybord():
    # keyboard = InlineKeyboardButton(row_width=1)
    # first_name = InlineKeyboardButton("Ism", callback_data ="first_name+1")
    # last_name = InlineKeyboardButton("Familiya", callback_data="last_name+1")
    # phone = InlineKeyboardButton('Telefon nomer', callback_data="phone+1")
    # return keyboard.add(first_name, last_name, phone)
# 
# 
# def update_type(message):
    # user_id = message.chat.id
    # user_type = data['type'][user_id]
    # text = message.text
    # if user_type == 'phone':
        # if text.startswith("+998") and len(text) == 13 and text[1:].isdigit():
            # data["user"][user_id][user_type] = message.text
            # bot.send_message(user_id, "Sizning kiritgan malumotingiz qabul qilindi")
        # else:
            # bot.send_message(user_id, "Boshqatdan telefon nomerni  kiriting")
            # bot.register_next_step_handler(message, update_type)
    # else:
        # if text.isalpha():
            # data['user'][user_id][user_type] = message.text
            # bot.send_message(user_id, "Sizning kiritgan malumotingiz qabul qilindi")
        # else:
            # type = {
                # "first_name": "Ism",
                # "last_name": "Familiya"
                # 
            # }
            # bot.send_message(user_id, f"Boshqatdan {type[user_type]} kiriting")
            # bot.register_next_step_handler(message, update_type)
# 
# @bot.callback_query_handler(func=lambda x: x.data.split("+")[-1] == "1")
# def update_user_data(call):
    # type_user = call.data.split("+")[0]
    # user_id = call.meassage.chat.id
    # data['type'][user_id] = type_user
    # type ={
        # "first_name": "Ism",
        # "last_name": "Familiya",
        # "phone": "Telefon nomer"
    # }
    # bot.edit_message_text(
        # f"{type[type_user]} kiriting",
        # call.message.chat.id,
        # call.message.id
    # )
    # 
    # bot.register_next_step_handler(call.message, update_type)
# 
# def data_text(message):
    # user_data = data["user"][message.chat.id]
    # if user_data:
        # text = f"Ism: {user_data['first_name']}\n" \
            #    f"Familiya: {user_data['last_name']}\n" \
            #    f"Telefon nomer: {user_data['phone']}\n"
        # return text
    # data["user"][message.chat.id] = {
        # "first_name": "-",
        # "last_name": "-",
        # "phone": "-"
    # }
    # return "Ism: -\n" \
        #    "Familiya: -\n" \
        #    "Telefon nomer: -"
# 
# @bot.message_handler(func=lambda x: x.text == "Ro'yxatdan o'tish")
# def registration(message):
    # text = data_text(message)
    # bot.send_message(message.chat.id, f"{text}", reply_markup=get_inlinekeybord())
    # 
# @bot.message_handler(commands="start")
# def start(message):
    # if message.chat.id not in data['user']:
        # data["user"][message.chat.id] = {}
    # bot.send_message(message.chat.id, f"salom {message.from_user.first_name}", reply_markup=get_keyboard())
# 
# bot.polling()
 

# Sinf ishi

# n = 12
# def ebo(n):
    # if n == 0:
        # return 0 
    # return n + ebo(n-1)
# print(ebo(12))


# a = int(input('son kiriting: '))
# def ebo(n):
    # if n == 0:
        # return 1
    # return n * ebo(n-1)
# 
# print(ebo(a))






# 
# def ebo():
    # print(123)
    # return ebo()
# 
# 
# print(ebo())


# n = 12
# def ebo(n):
    # if n == 0:
        # return 0 
    # return n + ebo(n-1)
# print(ebo(12))





# def dunyo(n):
    # return n
# 
# print(dunyo(123))






# def media(f):
    # def team():
        # s = f()
        # return s[::-1]
    # return team
# @media 
# def ebo():
    # return "salom"
# 
# 
# print(ebo()) 


# Recursiya--------> Funksiyani ichida funksiya ishlatishga aytiladi

#Decoratsiya-------> Print bilan Return orasidagi narsa. |
# Returndan Decoratorga jo'natadi.Decorator ishlab, ishlab printga jo'natadi.



# Decorator

# def media(f):
    # def team():
        # s = f()
        # return s[::-1]
    # return team
# @media 
# def ebo():
    # return "salom"
# 
# 
# 
# @media 
# def world():
    # return "dunyo"
# 
# 
# print(ebo()) 
# print(world())






        




# import telebot
# from telebot.types import *


# bot = telebot.TeleBot("5113084134:AAE1Pm_3YzMYEwu0jKVEVUukLVzs4tEwLBs")



# data = {
#     "user": {},
#     "admin": [895752511],
#     "type": {}
    
# }



# def get_keyboard():
#     return ReplyKeyboardMarkup(resize_keyboard=True).add(
#         KeyboardButton("Ro'yxatdan o'tish")
#     )
    

# def get_inlinekeybord():
#     keyboard = InlineKeyboardButton(row_width=1)
#     first_name = InlineKeyboardButton("Ism", callback_data ="first_name+1")
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
#             bot.send_message(user_id, "Sizning kiritgan malumotingiz qabul qilindi")
#         else:
#             bot.send_message(user_id, "Boshqatdan telefon nomerni  kiriting")
#             bot.register_next_step_handler(message, update_type)
#     else:
#         if text.isalpha():
#             data['user'][user_id][user_type] = message.text
#             bot.send_message(user_id, "Sizning kiritgan malumotingiz qabul qilindi")
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
#     user_id = call.meassage.chat.id
#     data['type'][user_id] = type_user
#     type ={
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
#     if user_data:
#         text = f"Ism: {user_data['first_name']}\n" \
#                f"Familiya: {user_data['last_name']}\n" \
#                f"Telefon nomer: {user_data['phone']}\n"
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
#     bot.send_message(message.chat.id, f"{text}", reply_markup=get_inlinekeybord())
    
# @bot.message_handler(commands="start")
# def start(message):
#     print(message.chat.id)
#     if message.chat.id in data["admin"]:
#         bot.send_message(message.chat.id, f"salom {message.from_user.first_name}", reply_markup=admin_keyboard())
        
#     else:
#         if message.chat.id not in data['user']:
#             data["user"][message.chat.id] = {}
#     bot.send_message(message.chat.id, f"salom {message.from_user.first_name}", reply_markup=get_keyboard())




# def admin_keyboard():
#     return ReplyKeyboardMarkup(resize_keyboard=True).add(
#         KeyboardButton("Ro'yxat")
#     )


# bot.polling()










#    29.01.2021 yil
# Mavzu : OOP



# from math import *
# def shar_yuzi(r):
#     return 4 * pi * r ** 2


# def shar_hajmi(r):
#     return 4 / 3 * pi * r ** 3

# def kub_yuzi(a):
#     return 6 * a ** 3

# def kub_hajmi(a):
#     return a ** 3

# print(shar_yuzi(4), shar_hajmi(4))

# from math import *
# class Shar:
#     def __init__(self, r):
#         self.r = r
        
#     def yuza(self):
#         return 4 * pi  * self.r ** 2

#     def hajm(self):
#         return 4 / 3 * pi * self.r ** 3
    
#     def radius(self):
#         return self.r
    

# shar1 = Shar(4)
# shar2 = Shar(8)
# shar3 = Shar(29)

# print(shar1.yuza(), shar2.yuza(), shar3.hajm())
# print(shar1.hajm(), shar2.hajm(), shar3.hajm())


# from math import *
# class Tort:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
        
        
#     def yuza(self):
#         return self.a * self.b
    
#     def perimetr(self):
#         return 2 * (self.a + self.b) 
    
#     def diogonal(self):
#         return sqrt((self.a + self.b) ** 2 - 2 * self.a * self.b) 


# tort1 = Tort(12, 3)
# tort2 = Tort(2, 4)
# tort3 = Tort(5, 1)

# print(tort1.yuza(), tort2.diogonal(), tort3.perimetr())



# class Paralelipiped :
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def yuza(self):
#         return 2 * (self.a * self.b + self.c + self.b * self.c)
    
#     def hajm(self):
#         return self.a * self.b * self.c
    
    
#     def asos_perimetri(self):
#         return 2  *  (self.a + self.b)
        
        
#     def perimetr(self):
#         return 4 * (self.a + self.b)
        
# paralelipiped = Paralelipiped(5, 5, 9)
# paralelipiped = Paralelipiped(2, 9, 7)
# paralelipiped = Paralelipiped(3, 7, 6)

# print(paralelipiped.yuza(), paralelipiped.hajm(), paralelipiped.asos_perimetri())

# UYGA VAZIFA  ////// CANCULATOR 




# from math import *

# class Hisoblash:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
        
        
#     def kopaytirirish(self):
#         return self.a * self.b
    
    
#     def bolish(self):
#         return self.a / self.b
    
    
#     def qoshish(self):
#         return self.a + self.b
    
    
#     def ayirish(self):
#         return self.a - self.b
    
    
#     def darajaga_kotarish(self):
#         return (self.a) ** 2,  (self.b) ** 2
    
    
#     def ildiz(self):
#         return sqrt(self.a ), sqrt(self.b) 


# hisoblash = Hisoblash(64, 25)


# print(hisoblash.kopaytirirish(), hisoblash.bolish())
# print(hisoblash.qoshish(), hisoblash.ayirish())
# print(hisoblash.darajaga_kotarish(), hisoblash.ildiz())







#  ----------------1 --- FEVRAL---------
# ----------------OOP--------2--DARS



# class HolMeva:
#     def daraxt(self):
#         return True
#     def yesa_boladi(self):
#         return True
    
# class QuruqMeva:
#     def daraxt(self):
#            return True
#     def yesa_boladi(self):
#         return True


# hm = HolMeva()
# qm = QuruqMeva()

# print(qm.daraxt(), hm.daraxt())



# class Meva:
#     def daraxt(self):
#            return True
#     def yesa_boladi(self):
#         return True

# class HolMeva(Meva):
#     pass


# class QuruqMeva(Meva):
#     pass


# hm = HolMeva()
# qm = QuruqMeva()

# print(qm.daraxt(), hm.daraxt())
    


#   ____ADD____ METODHOGA MISOL

# class distance:
#     def __init__(self, x=None,y=None):
#         self.ft=x
#         self.inch=y
#     def __add__(self,x):
#         temp=distance()
#         temp.ft=self.ft+x.ft
#         temp.inch=self.inch+x.inch
#         if temp.inch>=12:
#             temp.ft+=1
#             temp.inch-=12
#             return temp
#     def __str__(self):
#         return 'ft:'+str(self.ft)+' in: '+str(self.inch)
    


# d1=distance(3,10)
# d2=distance(4,4)
# print("d1= {} d2={}".format(d1, d2))
# d3=d1+d2
# print(d3)





# ____STR____ METOGHOD GA MISOL 



# class Employee:
#     def __init__(self):
#         self.name='Swati'
#         self.salary=10000
#     def __str__(self):
#         return 'name='+self.name+' salary=$'+str(self.salary)

# e1=Employee()
# print(e1) 





# ____GE___ METHOD GA MISOL


# class distance:
#     def __init__(self, x=None,y=None):
#         self.ft=x
#         self.inch=y
#     def __ge__(self, x):
#         val1=self.ft*12+self.inch
#         val2=x.ft*12+x.inch
#         if val1>=val2:
#             return True
#         else:
#             return False

# d1=distance(2,1)
# d2=distance(4,10)

# print(d1>=d2)






#  03/02/20222-yil
# MAVZU: OOP-(3- DARS)





# class Meva:
#     def __init__(self):
#         self.qiymat = 44
        
# class HM(Meva):
#     def chiqim(self):
#         return self.qiymat 

# class QM(Meva):
#     pass

# print(HM(). chiqim())




# class Meva:
#     def __init__(self):
#         self.qiymat = 44
        
# class HM(Meva):
#     @property
#     def chiqim(self):
#         return self.qiymat 

# class QM(Meva):
#     pass

# print(HM(). chiqim)




# class Meva:
#     def __init__(self):
#         self.qiymat = 44
        
# class HM(Meva):
#     a = 75
#     @property
#     def chiqim(self):
#         return self.qiymat 

# class QM(Meva):
#     pass

# print(HM(). a)





# class Meva:
#     def __init__(self):
#         self.qiymat = 44
        
# class HM(Meva):
#     a = 75
#     @property
#     def chiqim(self):
#         return self.qiymat 

# class QM(Meva):
#     pass

# print(HM(). chiqim)





# class Meva:
#     def __init__(self):
#         self.a = 44
        
# class HM(Meva):
#     @property
#     def ab(self):
#         return self.a 

# class QM(Meva):
#     pass

# print(HM(). ab)





# class Meva:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
      

#     def qoshish(self):
#         return self.a + self.b


# class HM(Meva):
#     pass


# hm = HM(1, 5)


# print(hm.qoshish())




# class Meva:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
      

#     def qoshish(self):
#         return self.a + self.b


# class HM(Meva):
#     pass


# hm = HM(1, 5)
# hm.a = 2

# print(hm.qoshish())



# class Meva:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
      

#     def qoshish(self):
#         return self.a + self.b


# class HM(Meva):
#     @property
#     def shaxa(self):
#         return self.a
    
    
#     @shaxa.setter
#     def shaxa(self):
#         return self.a


# hm = HM(1, 5)


# print(hm.shaxa)




# class Meva:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
      

#     def qoshish(self):
#         return self.a + self.b


# class HM(Meva):
#     @property
#     def shaxa(self):
#         return self.a
    
    
#     @shaxa.setter
#     def shaxa(self):
#         return self.a


# hm = HM(1, 5)
# hm.a = "salom"

# print(hm.shaxa)













# class Meva:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
      

#     def qoshish(self):
#         return self.a + self.b


# class HM(Meva):
#     def qoshish(self):
#         return self.a


# hm = HM(5, 5)


# print(hm.qoshish())








# class Geek:
#     def __init__(self, age = 0):
#          self._age = age
      
   
#     def get_age(self):
#         return self._age
      
    
#     def set_age(self, x):
#         self._age = x
  
# raj = Geek()
  

# raj.set_age(21)
  

# print(raj.get_age())
  
# print(raj._age)




# class Geeks:
#      def __init__(self):
#           self._age = 0
       
    
#      def get_age(self):
#          print("getter method called")
#          return self._age
       
     
#      def set_age(self, a):
#          print("setter method called")
#          self._age = a
  
     
#      def del_age(self):
#          del self._age
     
#      age = property(get_age, set_age, del_age) 
  
# mark = Geeks()
  
# mark.age = 10
  
# print(mark.age)



# class Geeks:
#      def __init__(self):
#           self._age = 0
       
    
#      @property
#      def age(self):
#          print("getter method called")
#          return self._age
       
     
#      @age.setter
#      def age(self, a):
#          if(a < 18):
#             raise ValueError("Sorry you age is below eligibility criteria")
#          print("setter method called")
#          self._age = a
  
# mark = Geeks()
  
# mark.age = 19
  
# print(mark.age)









# UYGA VAZIFA MATH 

# from math import *

# class Hisoblash:
#     def __init__(self, a, b, c, h, d1, d2, r, R):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.h = h
#         self.d1 = d1
#         self.d2 = d2
#         self.r = r
#         self.R = R
    
#     def kopaytirirish(self):
#         return self.a * self.b
    
    
#     def bolish(self):
#         return self.a / self.b
    
    
#     def qoshish(self):
#         return self.a + self.b
    
    
#     def ayirish(self):
#         return self.a - self.b
    
    
#     def darajaga_kotarish(self):
#         return (self.a) ** 2,  (self.b) ** 2
    
    
#     def ildiz(self):
#         return sqrt(self.a ), sqrt(self.b)
    
#     def sinus(self):
#         return  self.a / self.c, self.b / self.c
#     # Burchak qarshisida yotgan katetning gipotenuzaga nisbatiga shu burchakning Sinusi deyiladi
    
#     def kosinus(self):
#         return self.b / self.c,  self.a / self.c
#     # Burchaaka yopishgan katetning gipotenuzaga nisbati shu burchakning Kosinusi deyiladi
    
#     def tangens(self):
#         return self.a / self.b, self.b / self.a
#     # Burchak qarshisida yotgan katetning yopishgan katetga nisbatiga  shu burchakning Tangensi deyiladi
    
#     def kotangens(self):
#         return self.b / self.a, self.a / self.b
#     # Burchak yonida yotgan katetning qarshisida yotgan katetga nisbatiga shu burchakning  Kotangensi deyiladi
    


# class MHisobla(Hisoblash):
#     pass


# class Geometriya(Hisoblash):
#     pass

#     def kvadratni_yuzi(self):
#         return self.a ** 2
    
#     def togri_tortburchakni_yuzi(self):
#         return self.a * self.b 
    
#     def parallelogramni_yuzi(self):
#         return self.a * self.h
    
#     def uchburchak_yuzi(self):
#         return 1/2 * (self.a * self.h)
    
#     def rombni_yuzi(self):
#         return 1/2 * (self.d1 * self.d2)
    
#     def trapetsiyani_yuzi(self):
#         return (self.a + self.b) / 2 * self.h
    
#     def pifagor(self):
#         return (self.a ** 2) + (self.b ** 2)


#     def shar_yuza(self):
#         return 4 * pi  * self.r ** 2
    
#     def shar_hajm(self):
#         return 4 / 3 * pi * self.r ** 3
    
#     def radius(self):
#         return self.r
    
#     def doiraning_yuzi(self):
#         return pi * self.R ** 2
        
   
    
    
    
    

# hisoblash = Hisoblash(64, 25, 5, 2, 2, 4, 5, 3)
# geometriya = Geometriya(64, 25,5, 2, 2, 4, 5, 3)
# # print(hisoblash.kopaytirirish(), hisoblash.bolish(), hisoblash.qoshish(), hisoblash.ayirish(), hisoblash.darajaga_kotarish(), hisoblash.ildiz())
# # print(hisoblash.sinus(),hisoblash.kosinus(), hisoblash.tangens(), hisoblash.kotangens())
# # print(hisoblash.kvadratni_yuzi(), hisoblash.togri_tortburchakni_yuzi(), hisoblash.parallelogramni_yuzi(), hisoblash.uchburchak_yuzi())
# # print(hisoblash.rombni_yuzi(), hisoblash.trapetsiyani_yuzi(), hisoblash.pifagor(), hisoblash.shar_yuza())
# # print(hisoblash.shar_hajm(), hisoblash.radius(), hisoblash.doiraning_yuzi())
# print(hisoblash.ayirish(), geometriya.uchburchak_yuzi())


# print(type(list()))

# class MYList:
#     def __init__(self, value):
#         self.value = value
        
        
#     def _len_(self):
#         return 10
    
#     def __getiem__(self, key):
#         return self.value[key]
    
#     def _init__(self, key):
#         del self.value[key]

# my = MYList([1,2,3,4,5])
# exam = [1,2,3,4,5]
 
 


# LEN

# class MYList:
#     def __len__(self, len):
#         self.len = len
#         def len(text):
#             n = 0
#             for s in text:
#                     n += 1
#             return n
# print(len(input("matn: ")))



# class MyCustomList(list):

#     def __getitem__(self, index):
#         if index == 0:
#             raise ValueError
#         index = index - 1
#         return list.__getitem__(self, index)

#     def __setitem__(self, index, value):
#         if index == 0:
#             raise ValueError
#         index = index - 1
#         return list.__setitem__(self, index, value)

#     def __delitem__(self, key):
#         key = key - 1
#         return list.__delitem__(self, key)


# list_one = MyCustomList([1,2,3,4,5])
# print(list_one)




    
# class MyCustomList(list):

#     def __getitem__(self, index):
#         if index == 0:
#             raise ValueError
#         index = index - 1
#         return list.__getitem__(self, index)

#     def __setitem__(self, index, value):
#         if index == 0:
#             raise ValueError
#         index = index - 1
#         return list.__setitem__(self, index, value)

#     def __delitem__(self, key):
#         key = key - 1
#         return list.__delitem__(self, key)







# class AvtoSalon:
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []
        
#     def __repr__(self):
#         return f"{self.name} avtosaloni"
    
#     def __len__(self):
#         return len(self.avtolar)
    
#     def __getitem__(self,index):
#         return self.avtolar[index]
    
# print(salon1[0])

