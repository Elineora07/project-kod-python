
import logging
from xml.dom.minidom import Document
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import video_darsliklar as vid

print("Bot started...")


TOKEN = ""


logging.basicConfig(level = logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)








@dp.message_handler(commands = ['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Salom {0.first_name}\nFirdavsbek Yorkulovning Elektron darsliklar botiga xush kelibsiz!\nAyrim darsliklar topilmagani sababli bot bazadagi boshqa kitoblarni chiqarib yuborishi mumkin.\nBuning uchun uzr soraymiz\nMarhamat Botdan yaxshi maqsadda foydalaning".format(message.from_user), reply_markup= nav.mainMenu)
    await bot.send_message(message.from_user.id, "Botdan foydalanish uchun tezkor komandalar:\n/admin - admin kim\n/help - yordam uchun\n/1 - Otkan kunlar\n/2 - Jinlar bazmi\n/3 - Quyonlar saltanati\n/4 - Sariq devning olimi\nAudio Kitoblar:\n/5 - Shum bola audiosi\n/6 - Me'mor audio hikoya\n/7 - Garov\n/8 - Taras Bulba\n/9 - Shamol yolidagi qabriston\n/10 - Kitob savdosi\n/11 - Yutuq\n/12 - Qurigan daraxt\n/booknomy - Booknomy ingliz tili uchun\n/epub - EPUB o'quvchi dastur\n/avtotest - AvtoTest uchun\n/")



@dp.message_handler(commands = ['avtotest'])
async def command_avtotest(message: types.Message):
	await message.reply_document(document = "https://t.me/apklar_kitob_baza/72")


@dp.message_handler(commands = ['epub'])
async def command_epub(message: types.Message):
	await message.reply_document(document = "https://t.me/apklar_kitob_baza/62")


@dp.message_handler(commands = ['booknomy'])
async def command_13(message: types.Message):
	await message.reply_document(document = "https://t.me/booknomy_baza/4")
	await message.reply_document(document = "https://t.me/booknomy_baza/6")
	await message.reply_document(document = "https://t.me/booknomy_baza/3")
	await message.reply_document(document = "https://t.me/booknomy_baza/2")
	await message.reply_document(document = "https://t.me/booknomy_baza/5")
	await message.reply_document(document = "https://t.me/booknomy_baza/7")
	await message.reply_document(document = "https://t.me/booknomy_baza/8")
	await message.reply_document(document = "https://t.me/booknomy_baza/9")




@dp.message_handler(commands = ['12'])
async def command_12(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/388")





@dp.message_handler(commands = ['11'])
async def command_11(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/386")



@dp.message_handler(commands = ['10'])
async def command_10(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/385")



@dp.message_handler(commands = ['9'])
async def command_9(message: types.Message):
    await message.reply_document(document  ="https://t.me/firdavsbek1551/387")


@dp.message_handler(commands = ['8'])
async def command_8(message: types.Message):
    await message.reply_document(document ="https://t.me/firdavsbek1551/383")







@dp.message_handler(commands = ['7'])
async def command_7(message: types.Message):
    await message.reply_document(document ="https://t.me/firdavsbek1551/381")



@dp.message_handler(commands  =['6'])
async def command_6(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/384")


@dp.message_handler(commands = ['5'])
async def command_5(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/380")


@dp.message_handler(commands = ['admin'])
async def command_admin(message: types.Message):
    await bot.send_message(message.chat.id, "Assalomu alaykum!\nHurmatli foydalanuvchi botimiz admini: Firdavsbek Yorkulov.\nAdmin bilan aloqa:\nTelegram: @Firdavs_Programmer\nWeb-site: firdavsbek07.netlify.app\nBotimizdan foydalanayotganingiz uchun, rahmat.")

@dp.message_handler(commands = ['audio'])
async def command_audio(message: types.Message):
    await bot.send_message(message.from_user.id, "Assalomu alaykum!".format(message.from_user), reply_markup= nav.menuAudioBooks)

@dp.message_handler(commands = ['4'])
async def command_4(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/243")



@dp.message_handler(commands = ['3'])
async def command_3(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/241")




@dp.message_handler(commands = ['2'])
async def command_2(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/244")



@dp.message_handler(commands = ['1'])
async def command_1(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/247")



@dp.message_handler(commands = ['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, "Botdan foydalanish uchun\n/start buyrug'ini bering. Va pastdan chiqgan tugmalardan mosini tanlang.\nCreator: Firdavs Yorkulov\nMurojaat uchun:\nTelegram: @Firdavs_Programmer\nWeb-site: firdavsbek07.netlify.app.")

















@dp.message_handler()
async def bot_message(message: types.Message):
    #await bot.send_message(message.from_user.id, message.text)
    if message.text=="📘Maktab darsliklari📘":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuSinflar)
        
    elif message.text =="🇺🇸Ingliz tili bilimdon🇺🇸":
        await message.reply_document(document ="https://t.me/apklar_kitob_baza/74")
        
    elif message.text =="🇷🇺Rus tili bilimdon🇷🇺":
        await message.reply_document(document ="https://t.me/apklar_kitob_baza/76")
    
    if message.text=="😊 Orqaga":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuSinflar)
    
    if message.text=="💻 Informatika":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuInformatika)
    
    if message.text=="🔙 Back":
        await bot.send_message(message.from_user.id, message.text, reply_markup=vid.menuVideo)

    elif message.text =="🧑‍💻Admin🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bot admini: @Firdavs_Programmer")


    elif message.text == "🚔Avto Test✅":
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/72")


    elif message.text == "🧑‍💻Admin bilan aloqa🧑‍💻":
    	await bot.send_message(message.from_user.id, message.text, reply_markup = nav.btnaloqaMenu)


    elif message.text == "🎧5-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/184")
        await message.reply_document(document = "https://t.me/audios_baza/181")
        await message.reply_document(document = "https://t.me/audios_baza/185")
        await message.reply_document(document = "https://t.me/audios_baza/182")
        await message.reply_document(document = "https://t.me/audios_baza/183")

    elif message.text == "📖6-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/244")
        await message.reply_document(document = "https://t.me/audios_baza/249")
        await message.reply_document(document = "https://t.me/audios_baza/241")
        await message.reply_document(document = "https://t.me/audios_baza/252")
        await message.reply_document(document = "https://t.me/audios_baza/250")
        await message.reply_document(document = "https://t.me/audios_baza/248")
        await message.reply_document(document = "https://t.me/audios_baza/243")
        await message.reply_document(document = "https://t.me/audios_baza/245")
        await message.reply_document(document = "https://t.me/audios_baza/247")
        await message.reply_document(document = "https://t.me/audios_baza/239")
        await message.reply_document(document = "https://t.me/audios_baza/255")
        await message.reply_document(document = "https://t.me/audios_baza/253")
        await message.reply_document(document = "https://t.me/audios_baza/242")
        await message.reply_document(document = "https://t.me/audios_baza/240")
        await message.reply_document(document = "https://t.me/audios_baza/257")
        await message.reply_document(document = "https://t.me/audios_baza/256")
        await message.reply_document(document = "https://t.me/audios_baza/246")



    elif message.text == "📖7-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/259")
        await message.reply_document(document = "https://t.me/audios_baza/263")
        await message.reply_document(document = "https://t.me/audios_baza/261")
        await message.reply_document(document = "https://t.me/audios_baza/260")
        await message.reply_document(document = "https://t.me/audios_baza/264")
        await message.reply_document(document = "https://t.me/audios_baza/262")
        await message.reply_document(document = "https://t.me/audios_baza/265")
        await message.reply_document(document = "https://t.me/audios_baza/266")
        await message.reply_document(document = "https://t.me/audios_baza/268")
        await message.reply_document(document = "https://t.me/audios_baza/269")
        await message.reply_document(document = "https://t.me/audios_baza/267")
        await message.reply_document(document = "https://t.me/audios_baza/270")
        await message.reply_document(document = "https://t.me/audios_baza/272")
        await message.reply_document(document = "https://t.me/audios_baza/271")
        await message.reply_document(document = "https://t.me/audios_baza/273")
        await message.reply_document(document = "https://t.me/audios_baza/276")
        await message.reply_document(document = "https://t.me/audios_baza/274")
        await message.reply_document(document = "https://t.me/audios_baza/277")
        await message.reply_document(document = "https://t.me/audios_baza/275")


    elif message.text =="📖8-sinf🎧":
        await message.reply_document(document = "https://t.me/booknomy_baza/83")
        await message.reply_document(document = "https://t.me/booknomy_baza/86")
        await message.reply_document(document = "https://t.me/booknomy_baza/85")
        await message.reply_document(document = "https://t.me/booknomy_baza/84")
        await message.reply_document(document = "https://t.me/booknomy_baza/87")
        await message.reply_document(document = "https://t.me/booknomy_baza/90")
        await message.reply_document(document = "https://t.me/booknomy_baza/91")
        await message.reply_document(document = "https://t.me/booknomy_baza/92")
        await message.reply_document(document = "https://t.me/booknomy_baza/89")
        await message.reply_document(document = "https://t.me/booknomy_baza/88")
        

    elif message.text =="📖9-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/284")
        await message.reply_document(document = "https://t.me/audios_baza/283")
        await message.reply_document(document = "https://t.me/audios_baza/285")
        await message.reply_document(document = "https://t.me/audios_baza/286")
        await message.reply_document(document = "https://t.me/audios_baza/282")
        await message.reply_document(document = "https://t.me/audios_baza/281")
        await message.reply_document(document = "https://t.me/audios_baza/287")
        await message.reply_document(document = "https://t.me/audios_baza/289")
        await message.reply_document(document = "https://t.me/audios_baza/290")
        await message.reply_document(document = "https://t.me/audios_baza/288")
        
    elif message.text == "📖10-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/294")
        await message.reply_document(document = "https://t.me/audios_baza/299")
        await message.reply_document(document = "https://t.me/audios_baza/293")
        await message.reply_document(document = "https://t.me/audios_baza/301")
        await message.reply_document(document = "https://t.me/audios_baza/297")
        await message.reply_document(document = "https://t.me/audios_baza/296")
        await message.reply_document(document = "https://t.me/audios_baza/295")
        await message.reply_document(document = "https://t.me/audios_baza/292")
        await message.reply_document(document = "https://t.me/audios_baza/300")
        await message.reply_document(document = "https://t.me/audios_baza/298")


    elif message.text =="Fizika":
        await message.reply_document(document = "https://t.me/booknomy_baza/20")
        await message.reply_document(document = "https://t.me/booknomy_baza/21")
        await message.reply_document(document = "https://t.me/booknomy_baza/22")
        await message.reply_document(document = "https://t.me/booknomy_baza/23")
        await message.reply_document(document = "https://t.me/booknomy_baza/24")

    elif message.text == "Kimyo Biologiya":
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/79")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/80")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/83")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/82")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/85")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/81")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/84")


    elif message.text == "📖11-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/303")
        await message.reply_document(document = "https://t.me/audios_baza/308")
        await message.reply_document(document = "https://t.me/audios_baza/307")
        await message.reply_document(document = "https://t.me/audios_baza/305")
        await message.reply_document(document = "https://t.me/audios_baza/312")
        await message.reply_document(document = "https://t.me/audios_baza/306")
        await message.reply_document(document = "https://t.me/audios_baza/304")
        await message.reply_document(document = "https://t.me/audios_baza/310")
        await message.reply_document(document = "https://t.me/audios_baza/317")
        await message.reply_document(document = "https://t.me/audios_baza/313")
        await message.reply_document(document = "https://t.me/audios_baza/315")
        await message.reply_document(document = "https://t.me/audios_baza/311")
        await message.reply_document(document = "https://t.me/audios_baza/314")
        await message.reply_document(document = "https://t.me/audios_baza/316")
        await message.reply_document(document = "https://t.me/audios_baza/309")
        await message.reply_document(document = "https://t.me/audios_baza/321")
        await message.reply_document(document = "https://t.me/audios_baza/319")
        await message.reply_document(document = "https://t.me/audios_baza/318")
    
    elif message.text =="🎧6-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/188")
        await message.reply_document(document = "https://t.me/audios_baza/187")
        await message.reply_document(document = "https://t.me/audios_baza/189")
        await message.reply_document(document = "https://t.me/audios_baza/190")
        await message.reply_document(document = "https://t.me/audios_baza/191")
    
    elif message.text == "🎧7-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/194")
        await message.reply_document(document = "https://t.me/audios_baza/193")

    elif message.text == "🎧8-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/198")
        await message.reply_document(document = "https://t.me/audios_baza/199")
        await message.reply_document(document = "https://t.me/audios_baza/197")

    elif message.text == "🎧9-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/202")
        await message.reply_document(document = "https://t.me/audios_baza/201")



    elif message.text == "🎧10-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/205")
        await message.reply_document(document = "https://t.me/audios_baza/206")
        await message.reply_document(document = "https://t.me/audios_baza/204")
        await message.reply_document(document = "https://t.me/audios_baza/205")


    elif message.text == "🎧11-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/211")
        await message.reply_document(document = "https://t.me/audios_baza/212")
        await message.reply_document(document = "https://t.me/audios_baza/213")
        await message.reply_document(document = "https://t.me/audios_baza/215")
        await message.reply_document(document = "https://t.me/audios_baza/217")
        await message.reply_document(document = "https://t.me/audios_baza/214")
        await message.reply_document(document = "https://t.me/audios_baza/216")
    elif message.text =="📖5-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/220")
        await message.reply_document(document = "https://t.me/audios_baza/221")
        await message.reply_document(document = "https://t.me/audios_baza/222")
        await message.reply_document(document = "https://t.me/audios_baza/219")
        await message.reply_document(document = "https://t.me/audios_baza/223")
        await message.reply_document(document = "https://t.me/audios_baza/224")
        await message.reply_document(document = "https://t.me/audios_baza/227")
        await message.reply_document(document = "https://t.me/audios_baza/226")
        await message.reply_document(document = "https://t.me/audios_baza/228")
        await message.reply_document(document = "https://t.me/audios_baza/225")
        await message.reply_document(document = "")


    elif message.text == "🗣Audio ertaklar":
        await message.reply_document(document = "https://t.me/audios_baza/334")
        await message.reply_document(document = "https://t.me/audios_baza/335")
        await message.reply_document(document = "https://t.me/audios_baza/338")
        await message.reply_document(document = "https://t.me/audios_baza/336")
        await message.reply_document(document = "https://t.me/audios_baza/341")
        await message.reply_document(document = "https://t.me/audios_baza/339")
        await message.reply_document(document = "https://t.me/audios_baza/340")
        await message.reply_document(document = "https://t.me/audios_baza/337")
        await message.reply_document(document = "https://t.me/audios_baza/342")
        await message.reply_document(document = "https://t.me/audios_baza/344")
        await message.reply_document(document = "https://t.me/audios_baza/345")
        await message.reply_document(document = "https://t.me/audios_baza/346")
        await message.reply_document(document = "https://t.me/audios_baza/343")
        await message.reply_document(document = "https://t.me/audios_baza/347")
        await message.reply_document(document = "https://t.me/audios_baza/351")

    elif message.text == "🗣Audio hikoyalar🗣":
        await message.reply_document(document = "https://t.me/audios_baza/356")
        await message.reply_document(document = "https://t.me/audios_baza/357")
        await message.reply_document(document = "https://t.me/audios_baza/355")
        await message.reply_document(document = "https://t.me/audios_baza/358")
        await message.reply_document(document = "https://t.me/audios_baza/360")
        await message.reply_document(document = "https://t.me/audios_baza/359")
        await message.reply_document(document = "https://t.me/audios_baza/363")
        await message.reply_document(document = "https://t.me/audios_baza/361")
        await message.reply_document(document = "https://t.me/audios_baza/362")
        await message.reply_document(document = "https://t.me/audios_baza/366")
        await message.reply_document(document = "https://t.me/audios_baza/364")
        await message.reply_document(document = "https://t.me/audios_baza/365")
        await message.reply_document(document = "https://t.me/audios_baza/368")
        await message.reply_document(document = "https://t.me/audios_baza/367")
        await message.reply_document(document = "https://t.me/audios_baza/373")
        await message.reply_document(document = "https://t.me/audios_baza/374")
        await message.reply_document(document = "https://t.me/audios_baza/370")
        await message.reply_document(document = "https://t.me/audios_baza/372")


    elif message.text == "🧑‍💻Web saytimiz🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bizning Web Saytimiz:\nhttps://firdavsbek07.netlify.app")

    elif message.text == "🧑‍💻Instagram🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bizning Instagram sahifamiz:\nhttps://www.instagram.com/firdavs_python_developer")

    elif message.text =="🧑‍💻Telegram🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bizning Telegram sahifamiz:\nhttps://t.me/Firdavs_Programmer")

    elif message.text =="🧑‍💻Facebook🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bizning Facebook sahifamiz: \nhttps://www.facebook.com/profile.php?id=100077125194410")


    elif message.text =="🧑‍💻GitHub🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bizning GitHub sahifamiz: \nhttps://github.com/firdavsbekyorkulov")


    elif message.text =="📲Kitoblarni o'quvchi dastur📲":
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/64")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/65")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/66")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/67")



    elif message.text == "📖Rus tili✅":
    	await message.reply_document(document ="https://t.me/booknomy_baza/12")
    	await message.reply_document(document ="https://t.me/booknomy_baza/11")


    elif message.text =="📖Koreys tili✅":
    	await message.reply_document(document = "https://t.me/booknomy_baza/15")
    	await message.reply_document(document = "https://t.me/booknomy_baza/14")



    elif message.text =="📖Ona tili audio📖":
    	await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuOnatili)

    elif message.text =="🖋Adabiyot audio🖋":
    	await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuAdabuyotAudio)

    elif message.text =="🕰Tarix audio":
    	await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuTarixAudio)

    elif message.text =="☘️Biologiya audio☘️":
    	await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuBiology)


    elif message.text == "📖Islom Karimov asarlari📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/66")
        await message.reply_document(document = "https://t.me/booknomy_baza/67")
        await message.reply_document(document = "https://t.me/booknomy_baza/69")
        await message.reply_document(document = "https://t.me/booknomy_baza/68")
        await message.reply_document(document = "https://t.me/booknomy_baza/72")
        await message.reply_document(document = "https://t.me/booknomy_baza/70")
        await message.reply_document(document = "https://t.me/booknomy_baza/73")
        await message.reply_document(document = "https://t.me/booknomy_baza/71")
        await message.reply_document(document = "https://t.me/booknomy_baza/75")
        await message.reply_document(document = "https://t.me/booknomy_baza/74")
        

        
    elif message.text == "📖Shavkat Mirziyoyev asarlari📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/77")
        await message.reply_document(document = "https://t.me/booknomy_baza/80")
        await message.reply_document(document = "https://t.me/booknomy_baza/79")
        await message.reply_document(document = "https://t.me/booknomy_baza/81")
        await message.reply_document(document = "https://t.me/booknomy_baza/78")


    elif message.text == "📖Alisher Navoiy asarlari📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/55")
        await message.reply_document(document = "https://t.me/booknomy_baza/57")
        await message.reply_document(document = "https://t.me/booknomy_baza/56")
        await message.reply_document(document = "https://t.me/booknomy_baza/62")
        await message.reply_document(document = "https://t.me/booknomy_baza/61")
        await message.reply_document(document = "https://t.me/booknomy_baza/58")
        await message.reply_document(document = "https://t.me/booknomy_baza/60")
        await message.reply_document(document = "https://t.me/booknomy_baza/64")
        await message.reply_document(document = "https://t.me/booknomy_baza/63")
        await message.reply_document(document = "https://t.me/booknomy_baza/59")



    elif message.text == "📖Sheriyat📖":
        await bot.send_message(message.from_user.id, message.text, reply_markup = nav.btnMenuSheriy)



    elif message.text =="📖Muhammad Yusuf📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/27")
        await message.reply_document(document = "https://t.me/booknomy_baza/32")
        await message.reply_document(document = "https://t.me/booknomy_baza/33")
        await message.reply_document(document = "https://t.me/booknomy_baza/35")
        await message.reply_document(document = "https://t.me/booknomy_baza/28")
        await message.reply_document(document = "https://t.me/booknomy_baza/34")
        await message.reply_document(document = "https://t.me/booknomy_baza/30")
        await message.reply_document(document = "https://t.me/booknomy_baza/31")
        await message.reply_document(document = "https://t.me/booknomy_baza/29")
        await message.reply_document(document = "https://t.me/booknomy_baza/36")


    elif message.text == "📖Erkin Vohidov📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/42")
        await message.reply_document(document = "https://t.me/booknomy_baza/39")
        await message.reply_document(document = "https://t.me/booknomy_baza/38")
        await message.reply_document(document = "https://t.me/booknomy_baza/40")
        await message.reply_document(document = "https://t.me/booknomy_baza/41")
        await message.reply_document(document = "https://t.me/booknomy_baza/45")
        await message.reply_document(document = "https://t.me/booknomy_baza/43")
        await message.reply_document(document = "https://t.me/booknomy_baza/47")
        await message.reply_document(document = "https://t.me/booknomy_baza/44")
        await message.reply_document(document = "https://t.me/booknomy_baza/46")



    elif message.text =="📖Abdulla Oripov📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/50")
        await message.reply_document(document = "https://t.me/booknomy_baza/51")
        await message.reply_document(document = "https://t.me/booknomy_baza/49")
        await message.reply_document(document = "https://t.me/booknomy_baza/53")
        await message.reply_document(document = "https://t.me/booknomy_baza/52")


    elif message.text =="":
        await message.reply_document(document = "")





    elif message.text =="🇺🇿O'zbekiston Milliy Ensiklopediyasi🇺🇿":
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/9")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/10")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/7")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/4")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/15")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/14")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/3")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/5")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/2")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/6")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/8")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/18")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/17")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/13")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/11")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/12")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/19")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/16")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/20")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/24")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/25")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/27")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/28")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/22")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/21")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/29")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/30")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/26")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/23")
    	
    
    elif message.text=="♻️Botni guruhga qo'shish✅":
    	await bot.send_message(message.from_user.id, "Botni guruhga qo'shish uchun: ushbu linkdan foydalaning:\nhttps:telegram.me/Elektron_kutubxona_uz_robot?startgroup=new \nBotni ulashish uchun esa mana bu linkdan foydalaning: \nhttps://t.me/url?url=https://t.me/Elektron_kutubxona_uz_robot?start \nBotimizdan foydalanganingiz uchun rahmat!")


    elif message.text =="📂EPUBni ochish dasturi✅":
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/62")

    elif message.text =="📖Ingliz tili✅":
    	await message.reply_document(document = "https://t.me/booknomy_baza/4")
    	await message.reply_document(document = "https://t.me/booknomy_baza/6")
    	await message.reply_document(document = "https://t.me/booknomy_baza/3")
    	await message.reply_document(document = "https://t.me/booknomy_baza/2")
    	await message.reply_document(document = "https://t.me/booknomy_baza/5")
    	await message.reply_document(document = "https://t.me/booknomy_baza/7")
    	await message.reply_document(document = "https://t.me/booknomy_baza/8")
    	await message.reply_document(document = "https://t.me/booknomy_baza/9")

    elif message.text =="🇺🇸Booknomy":
    	await bot.send_message(message.from_user.id, message.text, reply_markup = nav.menuBooknomy)

    elif message.text =="🇺🇸Lug'atlar":
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/52")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/53")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/54")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/55")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/56")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/57")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/58")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/59")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/60")
    	



    elif message.text == "📐Matematika":
    	await message.reply_document(document = "https://t.me/firdavsbek1551/466")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/469")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/467")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/468")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/465")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/473")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/471")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/470")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/472")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/474")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/481")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/476")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/477")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/479")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/475")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/478")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/480")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/483")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/482")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/484")
    	await message.reply_document(document = "")





    elif message.text == "📲Apk kitoblar📕":
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/2")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/3")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/4")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/5")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/6")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/7")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/8")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/9")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/10")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/11")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/12")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/13")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/14")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/15")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/16")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/17")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/18")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/19")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/20")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/21")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/22")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/23")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/24")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/25")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/26")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/27")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/28")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/29")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/30")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/31")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/32")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/33")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/34")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/35")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/49")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/50")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/51")


    elif message.text =="📚Badiiy adabiyotlar📚":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menubooks)

    elif message.text =="🧑‍💻Bot dasturchisi🧑‍💻":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuDasturchilar)

    elif message.text =="Pdf kitoblar":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuAdabiyotlar)

    elif message.text =="<-Orqaga🔙":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.mainMenu)

    elif message.text =="Audio kitoblar":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuAudioBooks)

    elif message.text =="🔙 orqaga":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menubooks)


    elif message.text == "◀️Bosh menyu▶️":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.mainMenu)
        
    elif message.text == "🤖Bizning Botlarimiz🤖":
        await bot.send_message(message.from_user.id, message.text, reply_markup = nav.menuBots)


    elif message.text =="📹Videodarsliklar📹":
        await bot.send_message(message.from_user.id, message.text, reply_markup=vid.menuVideo)

    elif message.text == "🔢1-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu1sinf)

    elif message.text == "🔢2-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu2sinf)

    elif message.text =="🔢3-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu3sinf)

    elif message.text =="🔢4-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu4sinf)

    elif message.text =="🔢5-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu5sinf)

    elif message.text =="🔢6-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu6sinf)

    elif message.text =="🔢7-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu7sinf)

    elif message.text =="🔢8-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu8sinf)

    elif message.text =="🔢9-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu9sinf)

    elif message.text =="🔢10-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu10sinf)

    elif message.text =="🔢11-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu11sinf)

    

    if message.text=="📖1-sinf Tarbiya📖":
        await message.reply_document(document ="https://t.me/firdavsbek1551/218")

    elif message.text == "📖1-sinf Matematika📖":
        await message.reply_document(document = "https://t.me/firdavsbek1551/227")

    elif message.text == "📖1-sinf Alifbe📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/231")

    elif message.text == "📖1-sinf Yozuv daftari📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/219")

    elif message.text == "📖1-sinf Matematika daftari📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/228")



    elif message.text == "📖1-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/223")

    elif message.text == "📖1-sinf Tabiiy fan📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/232")

    elif message.text == "📖1-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/230")


    elif message.text == "📖1-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/221")

    elif message.text == "📖1-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/220")

    elif message.text == "📖1-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/229")

    elif message.text == "📖1-sinf Musiqa📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/226")

    elif message.text == "📖2-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/211")

    elif message.text == "📖2-sinf Matematika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/205")

    elif message.text == "📖2-sinf oqish📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/209")

    elif message.text == "📖2-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/212")

    elif message.text == "📖2-sinf Matematika daftari📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/206")

    elif message.text == "📖2-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/210")
    
    elif message.text == "📖2-sinf Tabiiy fan📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/204")

    elif message.text == "📖2-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/207")

    elif message.text == "📖2-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/213")

    elif message.text == "📖2-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/214")

    elif message.text == "📖2-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/200")

    elif message.text == "📖3-sinf Tarbiya":
        await message.reply_document(document="https://t.me/firdavsbek1551/197")

    elif message.text == "📖3-sinf Matematika":
        await message.reply_document(document="https://t.me/firdavsbek1551/195")

    
    elif message.text == "📖3-sinf O'qish":
        await message.reply_document(document="https://t.me/firdavsbek1551/193")

    elif message.text == "📖3-sinf Musiqa":
        await message.reply_document(document="https://t.me/firdavsbek1551/196")

    elif message.text == "📖3-sinf rus tili":
        await message.reply_document(document="https://t.me/firdavsbek1551/201")

    elif message.text == "📖3-sinf Ona tili":
        await message.reply_document(document="https://t.me/firdavsbek1551/192")


    elif message.text == "📖3-sinf Tabiiy fan":
        await message.reply_document(document="https://t.me/firdavsbek1551/203")

    elif message.text == "📖3-sinf Ingliz tili":
        await message.reply_document(document="https://t.me/firdavsbek1551/198")

    elif message.text == "📖3-sinf Tasviriy san'at":
        await message.reply_document(document="https://t.me/firdavsbek1551/198")

    elif message.text == "📖3-sinf Texnologiya":
        await message.reply_document(document="https://t.me/firdavsbek1551/201")

    elif message.text == "📖3-sinf Jismoniy Tarbiya":
        await message.reply_document(document="https://t.me/firdavsbek1551/200")

    elif message.text == "📖4-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/178")

    elif message.text == "📖4-sinf Matematika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/181")

    elif message.text == "📖4-sinf O'qish📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/189")

    elif message.text == "📖4-sinf Musiqa📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/182")

    elif message.text == "📖4-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/178")

    elif message.text == "📖4-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/179")

    elif message.text == "📖4-sinf Tabiiy fan📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/186")

    elif message.text == "📖4-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/188")

    elif message.text == "📖4-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/180")

    elif message.text == "📖4-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/183")

    elif message.text == "📖4-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/187")

    elif message.text == "📖5-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/156")

    elif message.text == "📖5-sinf Matematika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/176")

    elif message.text == "📖5-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/161")

    elif message.text == "📖5-sinf Informatika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/163")

    elif message.text == "📖5-sinf Matematika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/176")

    elif message.text == "📖5-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/169")

    elif message.text == "📖5-sinf Adabiyot 1":
        await message.reply_document(document="https://t.me/firdavsbek1551/156")

    elif message.text == "📖5-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/157")

    elif message.text == "📖5-sinf Adabiyot 2📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/165")

    elif message.text == "📖5-sinf Musiqa📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/173")

    elif message.text == "📖5-sinf Tabiiy fan📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/158")

    elif message.text == "📖5-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/164")

    elif message.text == "📖5-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/171")

    elif message.text == "📖5-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/162")

    elif message.text == "📖5-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/168")

    elif message.text == "📖6-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/144")

    elif message.text == "📖6-sinf Matematika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/147")


    elif message.text == "📖6-sinf Botanika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/141")

    elif message.text == "📖6-sinf Adabiyot 1📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/139")

    elif message.text == "📖6-sinf Adabiyot 2📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/140")

    elif message.text == "📖6-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/142")

    elif message.text == "📖6-sinf Tabiiy fan📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/141")

    elif message.text == "📖6-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/145")

    elif message.text == "📖6-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/152")

    elif message.text == "📖6-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/154")

    elif message.text == "📖6-sinf Musiqa📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/148")

    elif message.text == "📖6-sinf Informatika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/144")

    elif message.text == "📖6-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/143")

    elif message.text == "📖6-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/151")

    elif message.text == "📖7-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/119")

    elif message.text == "📖7-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/119")

    elif message.text == "📖7-sinf Adabiyot📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/137")

    elif message.text == "📖7-sinf Zoologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/123")

    elif message.text == "📖7-sinf Algebra📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/134")

    elif message.text == "📖7-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/133")

    elif message.text == "📖7-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/131")

    elif message.text == "📖7-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/130")

    elif message.text == "📖7-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/125")

    elif message.text == "📖7-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/124")

    elif message.text == "📖7-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/128")

    elif message.text == "📖7-sinf Geometriya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/136")

    elif message.text == "📖7-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/129")

    elif message.text == "📖7-sinf O'zb tarix📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/121")

    elif message.text == "📖7-sinf Jahon tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/120")

    elif message.text == "📖8-sinf Algebra📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/100")

    elif message.text == "📖8-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/105")

    elif message.text == "📖8-sinf Informatika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/106")

    elif message.text == "📖8-sinf Adabiyot📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/116")

    elif message.text == "📖8-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/109")

    elif message.text == "📖8-sinf Biologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/114")

    elif message.text == "📖8-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/108")

    elif message.text == "📖8-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/114")

    elif message.text == "📖8-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/114")

    elif message.text == "📖8-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/128")

    elif message.text == "📖8-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/102")

    elif message.text == "📖8-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/110")

    elif message.text == "📖8-sinf chizmachilik📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/101")

    elif message.text == "📖8-sinf Geometriya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/104")

    elif message.text == "📖8-sinf DHA📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/112")

    elif message.text == "📖8-sinf O'zbekiston Tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/111")

    elif message.text == "📖8-sinf Jahon tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/110")

    elif message.text == "📖9-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/96")

    elif message.text == "📖9-sinf Algebra📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/94")

    elif message.text == "📖9-sinf Adabiyot📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/88")

    elif message.text == "📖9-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/85")

    elif message.text == "📖9-sinf O'zbekiton tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/81")

    elif message.text == "📖9-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/80")

    elif message.text == "📖9-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/93")

    elif message.text == "📖9-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/92")

    elif message.text == "📖9-sinf chizmachilik📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/67")

    elif message.text == "📖9-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/82")

    elif message.text == "📖9-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/92")

    elif message.text == "📖9-sinf Biologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/84")

    elif message.text == "📖9-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/76")

    elif message.text == "📖9-sinf DHA📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/91")

    elif message.text == "📖9-sinf Informatika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/96")

    elif message.text == "📖9-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/95")

    elif message.text == "📖9-sinf Geometriya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/87")

    elif message.text == "📖9-sinf Jahon tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/75")

    elif message.text == "📖10-sinf Bilogiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/17")

    elif message.text == "📖10-sinf Algebra📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/22")

    elif message.text == "📖10-sinf Adabiyot📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/28")

    elif message.text == "📖10-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/23")

    elif message.text == "📖10-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/58")

    elif message.text == "📖10-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/26")

    elif message.text == "📖10-sinf Biologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/17")

    elif message.text == "📖10-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/19")

    elif message.text == "📖10-sinf Manaviyat asoslari📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/60")

    elif message.text == "10-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/24")

    elif message.text == "📖10-sinf Din tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/18")

    elif message.text == "📖10-sinf Jahon Tarix📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/20")

    elif message.text == "📖10-sinf Tarix📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/25")

    elif message.text == "📖10-sinf Matematika 2📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/21")

    elif message.text == "📖10-sinf Adabiyot 2📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/27")

    elif message.text == "📖10-sinf DHA📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/55")

    elif message.text == "📖10-sinf chqbt📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/56")

    elif message.text == "📖10-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/57")

    elif message.text == "📖10-sinf Informatika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/59")

    elif message.text == "📖10-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/56")

    elif message.text == "📖11-sinf DHA📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/42")

    elif message.text == "📖11-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/8")

    elif message.text == "📖11-sinf Din Tarix📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/43")

    elif message.text == "📖11-sinf Algebra📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/4")

    elif message.text == "📖11-sinf Adabiyot📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/41")

    elif message.text == "📖11-sinf Jahon tarix📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/3")

    elif message.text == "📖11-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/15")

    elif message.text == "📖11-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/9")

    elif message.text == "📖11-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/13")

    elif message.text == "📖11-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/12")

    elif message.text == "📖11-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/41")

    elif message.text == "📖11-sinf Astronomiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/10")

    elif message.text == "📖11-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/9")

    elif message.text == "📖11-sinf Biologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/11")

    elif message.text == "📖11-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/10")
# ---------->>>>>>>>>>>><<<<<<<<<<< Badiiy Adabiyotlar -------------------->>>>>>>>><<<<<<<<<<
    elif message.text == "📚Sariq devni minib📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/242")

    elif message.text == "📚Mungli ko'zlar📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/240")

    elif message.text == "📚Sariq devning o'limi📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/243")

    elif message.text == "📚O'tkan kunlar📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/247")

    elif message.text == "📚Quyonlar saltanati📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/241")

    elif message.text == "📚Mehrobdan Chayon📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/245")



        # AUDIO

    elif message.text == "Me'mor":
        await message.reply_document(document="https://t.me/firdavsbek1551/384")

    elif message.text == "Taras bulba":
        await message.reply_document(document="https://t.me/firdavsbek1551/383")

    elif message.text == "Erka qizning qismati":
        await message.reply_document(document="https://t.me/firdavsbek1551/382")

    elif message.text == "Garov":
        await message.reply_document(document="https://t.me/firdavsbek1551/381")

    elif message.text == "Shum bola":
        await message.reply_document(document="https://t.me/firdavsbek1551/380")

    elif message.text == "Jinlar bazmi":
        await message.reply_document(document="https://t.me/firdavsbek1551/379")

    elif message.text == "Uloqda":
        await message.reply_document(document="https://t.me/firdavsbek1551/375")

    elif message.text == "Qurigan daraxt":
        await message.reply_document(document="https://t.me/firdavsbek1551/388")

    elif message.text == "Kashfiyot":
        await message.reply_document(document="https://t.me/firdavsbek1551/390")

    elif message.text == "Yutuq":
        await message.reply_document(document="https://t.me/firdavsbek1551/386")

    elif message.text == "Orziqib kutaman ertani":
        await message.reply_document(document="https://t.me/firdavsbek1551/393")

    elif message.text == "G'ayri oddiy ong mo'jizalari":
        await message.reply_document(document="https://t.me/firdavsbek1551/395")

    elif message.text == "Saodatga eltuvchi bilim":
        await message.reply_document(document="https://t.me/firdavsbek1551/396")

    elif message.text == "Daydi qizning daftari":
        await message.reply_document(document="https://t.me/firdavsbek1551/397")

    elif message.text == "Yo'qolgan dunyo":
        await message.reply_document(document="https://t.me/firdavsbek1551/398")

    elif message.text == "Sarvqomat dilbarim":
        await message.reply_document(document="https://t.me/firdavsbek1551/399")

    elif message.text == "To'rt ulus tarixi":
        await message.reply_document(document="https://t.me/firdavsbek1551/400")

    elif message.text == "Soliha ayollar":
        await message.reply_document(document="https://t.me/firdavsbek1551/401")
    
    elif message.text == "Hikmatli latifalar":
        await message.reply_document(document="https://t.me/firdavsbek1551/402")

    elif message.text == "Baxt qasri":
        await message.reply_document(document="https://t.me/firdavsbek1551/403")

    elif message.text == "Sarmoyador":
        await message.reply_document(document="https://t.me/firdavsbek1551/404")

    elif message.text == "Osmondan tushgan pul":
        await message.reply_document(document="https://t.me/firdavsbek1551/405")

    elif message.text == "Donolar suhbati":
        await message.reply_document(document="https://t.me/firdavsbek1551/406")

    elif message.text == "Uch oltin gisht":
        await message.reply_document(document="https://t.me/firdavsbek1551/407")

    elif message.text == "Saylanma":
        await message.reply_document(document="https://t.me/firdavsbek1551/408")

    elif message.text == "Salomatlik sirlari":
        await message.reply_document(document="https://t.me/firdavsbek1551/409")

    elif message.text == "Meshpolvon jangga otlandi":
        await message.reply_document(document="https://t.me/firdavsbek1551/410")

    elif message.text == "Amerika fojiasi":
        await message.reply_document(document="https://t.me/firdavsbek1551/411")

    elif message.text == "Bo'ston ul-orifiyn":
        await message.reply_document(document="https://t.me/firdavsbek1551/412")

    elif message.text == "Shahzoda va Gado":
        await message.reply_document(document="https://t.me/firdavsbek1551/413")

    elif message.text == "Daryolar tutashgan joyda":
        await message.reply_document(document="https://t.me/firdavsbek1551/414")

    elif message.text == "Champo otli ilon":
        await message.reply_document(document="https://t.me/firdavsbek1551/415")

    elif message.text == "Eynshteyn bilan Iblisvachcha":
        await message.reply_document(document="https://t.me/firdavsbek1551/416")

    elif message.text == "Bola Alisher":
        await message.reply_document(document="https://t.me/firdavsbek1551/417")

    elif message.text == "Oq marmar":
        await message.reply_document(document="https://t.me/firdavsbek1551/418")

    elif message.text == "Cho'ri":
        await message.reply_document(document="https://t.me/firdavsbek1551/419")


    elif message.text == "Cho'l burguti":
        await message.reply_document(document="https://t.me/firdavsbek1551/420")

    elif message.text == "Garri Potter va ajal tuhfalari":
        await message.reply_document(document="https://t.me/firdavsbek1551/421")

    elif message.text == "Garri Potter va falsafiy tosh":
        await message.reply_document(document="https://t.me/firdavsbek1551/422")

    elif message.text == "Daftar hoshiyasidagi bitiklar":
        await message.reply_document(document="https://t.me/firdavsbek1551/423")

    elif message.text == "Ichindagi ichindadir":
        await message.reply_document(document="https://t.me/firdavsbek1551/424")

    elif message.text == "Bizning shaharda o'g'ri yo'q":
        await message.reply_document(document="https://t.me/firdavsbek1551/425")

    elif message.text == "Sudxo'rning o'limi":
        await message.reply_document(document="https://t.me/firdavsbek1551/426")

    elif message.text == "Zulmat ichra nur":
        await message.reply_document(document="https://t.me/firdavsbek1551/427")

    elif message.text == "Kech kuz":
        await message.reply_document(document="https://t.me/firdavsbek1551/428")

    elif message.text == "Odamiylik mulki":
        await message.reply_document(document="https://t.me/firdavsbek1551/429")

    elif message.text == "Bo'ri bolalarini qanday o'rgatadi":
        await message.reply_document(document="https://t.me/firdavsbek1551/430")

    elif message.text == "Futbol qiroli":
        await message.reply_document(document="https://t.me/firdavsbek1551/431")

    elif message.text == "Ey farzand":
        await message.reply_document(document="https://t.me/firdavsbek1551/432")

    elif message.text == "Avlodlar dovoni":
        await message.reply_document(document="https://t.me/firdavsbek1551/433")

    elif message.text == "Ajab dunyo":
        await message.reply_document(document="https://t.me/firdavsbek1551/434")

    elif message.text == "Yolg'onchi yor":
        await message.reply_document(document="https://t.me/firdavsbek1551/436")

    elif message.text == "Qiz bolaga tosh otmang":
        await message.reply_document(document="https://t.me/firdavsbek1551/437")

    elif message.text == "Boy bo'lishning 10ta siri":
        await message.reply_document(document="https://t.me/firdavsbek1551/438")


    elif message.text == "Kalila va Dimna":
        await message.reply_document(document="https://t.me/firdavsbek1551/439")

    elif message.text == "Biz millionermiz":
        await message.reply_document(document="https://t.me/firdavsbek1551/440")

    elif message.text == "Don Kristobalning xatosi":
        await message.reply_document(document="https://t.me/firdavsbek1551/441")

    elif message.text == "Daydi qizning daftari":
        await message.reply_document(document="https://t.me/firdavsbek1551/444")

    elif message.text == "Bu dunyoda o'lib bo'lmaydi":
        await message.reply_document(document="https://t.me/firdavsbek1551/445")

    elif message.text == "Kapitan qizi":
        await message.reply_document(document="https://t.me/firdavsbek1551/446")

    elif message.text == "Ona haqida sherlar":
        await message.reply_document(document="https://t.me/firdavsbek1551/447")

    elif message.text == "Pul topishning ulkan siri":
        await message.reply_document(document="https://t.me/firdavsbek1551/448")

    elif message.text == "Devona":
        await message.reply_document(document="https://t.me/firdavsbek1551/449")

    elif message.text == "Besh bolali yigitcha":
        await message.reply_document(document="https://t.me/firdavsbek1551/450")

    elif message.text == "Qo'rqmang onaginam":
        await message.reply_document(document="https://t.me/firdavsbek1551/453")

    elif message.text == "Yo'qolgan Dunyo":
        await message.reply_document(document="https://t.me/firdavsbek1551/454")

    elif message.text == "Boy ota kambag'al ota":
        await message.reply_document(document="https://t.me/firdavsbek1551/455")

    elif message.text == "Oygul bilan Baxtiyor":
        await message.reply_document(document="https://t.me/firdavsbek1551/456")

    elif message.text == "Ikki karra ikki Besh":
        await message.reply_document(document="https://t.me/firdavsbek1551/457")

    elif message.text == "Gulliverning sayohatlari":
        await message.reply_document(document="https://t.me/firdavsbek1551/442")

    elif message.text == "":
        await message.reply_document(document="")

    elif message.text == "":
        await message.reply_document(document="")






if __name__ =="__main__":
    executor.start_polling(dp, skip_updates=True)
    
    
    
    
    
    
    
    
    
    
    