import telebot
from telebot import types
import time

bot = telebot.TeleBot('7248478965:AAGQnuZhUWtadlUpGO6phdhfmmSJby_zPi8') 
ur_hero = {}
ur_name = {}
moment = {}
debugg = {}
@bot.message_handler(commands = ['start'])
def start(message): 
    global moment
    global debugg
    moment[message.chat.id] = 0
    debugg[message.chat.id] = 0
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, а давай посмотрим видео вместе?!')
    video = open('IntroVideo.mp4', 'rb') 
    bot.send_video(message.chat.id, video)
    time.sleep(30)
    hero = types.InlineKeyboardMarkup()
    profi = types.InlineKeyboardButton(text = 'Профи', callback_data='pro')
    einshetein = types.InlineKeyboardButton(text = 'Эйнштейн', callback_data='eins')
    afina = types.InlineKeyboardButton(text = 'Афина', callback_data='afin')
    yoyo = types.InlineKeyboardButton(text = 'Йо-Йо', callback_data='yoyo')
    like = types.InlineKeyboardButton(text = 'Лайк', callback_data='like')
    hero.add(profi, einshetein, afina, yoyo, like)
    bot.send_media_group(message.chat.id,[telebot.types.InputMediaPhoto('https://i.imgur.com/cyl9zEo.jpeg'),telebot.types.InputMediaPhoto('https://i.imgur.com/TvG4CsV.jpeg'),telebot.types.InputMediaPhoto('https://i.imgur.com/PFrT4AC.jpeg'),telebot.types.InputMediaPhoto('https://i.imgur.com/GIt9SLu.jpeg'),telebot.types.InputMediaPhoto('https://i.imgur.com/xoLZLYb.jpeg')])
    bot.send_message(message.chat.id, f'Уверены, что после просмотра всех серий мультфильма, у тебя появится свой любимчик среди героев спецотряда 112. \nКстати, найти их можешь на канале You tube «МЧС детям».\nА пока определись,  с которым из них будешь проходить испытания миссии.', parse_mode='html', reply_markup = hero)
@bot.callback_query_handler(func=lambda call: call.data == 'pro' or call.data == 'eins' or call.data == 'afin' or call.data == 'yoyo' or call.data == 'like')
def hero_choose(call):
    global ur_hero
    bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '')
    match call.data:
        case 'pro': ur_hero[call.message.chat.id] = 'Профи' 
        case 'eins': ur_hero[call.message.chat.id] = 'Эйнштейн'   
        case 'afin': ur_hero[call.message.chat.id] = 'Афина'
        case 'yoyo': ur_hero[call.message.chat.id] = 'Йо-йо'
        case 'like': ur_hero[call.message.chat.id] = 'Лайк'
    bot.send_message(call.message.chat.id, f'{ur_hero[call.message.chat.id]}: Привет, а как тебя зовут?')
    
@bot.callback_query_handler(func=lambda call: call.data == 'sum' or call.data == 'mistake_water')
def sum_task1(call):
    global moment
    moment[call.message.chat.id] = 0
    if call.data == 'mistake_water':
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '')
    water = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = 'Первый', callback_data = 'mistake_water')
    second = types.InlineKeyboardButton(text = 'Второй', callback_data = 'right_water')
    third = types.InlineKeyboardButton(text = 'Третий', callback_data = 'mistake_water')
    fourth = types.InlineKeyboardButton(text = 'Четвёртый', callback_data = 'mistake_water')
    water.add (first, second, third)
    bot.send_media_group(call.message.chat.id,[telebot.types.InputMediaPhoto("https://i.imgur.com/84SYzrj.jpeg"),telebot.types.InputMediaPhoto("https://i.imgur.com/QZkeIS8.jpeg"),telebot.types.InputMediaPhoto("https://i.imgur.com/8VR7M6e.jpeg")])
    bot.send_message(call.message.chat.id,f'Перед тобой три водоёма, на какой из них ты пойдёшь плавать?\nПодумай хорошенько. \nИнтересно, если бы мы добавили вариант: «Тот, что ближе к дому», выбрал бы его?\nЗапомни: даже если озеро или речка видны из твоего окна, но на пляже не дежурят спасатели ОСВОД – это ЗАПРЕЩЕННОЕ место для купания!', reply_markup = water)

@bot.callback_query_handler(func=lambda call: call.data == 'right_water' or call.data == 'mistake_helpers')
def sum_task2(call):
    if call.data == 'mistake_helpers':
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    else:
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ты молодец! Выполняй следующее задание!')
    bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '')
    helpers = types.InlineKeyboardMarkup()
    parents = types.InlineKeyboardButton(text = 'С родителями', callback_data = 'right_helpers')
    alone = types.InlineKeyboardButton(text = 'Один', callback_data = 'mistake_helpers')
    grands = types.InlineKeyboardButton(text = 'С пожилыми людьми', callback_data = 'mistake_helpers')
    friends = types.InlineKeyboardButton(text = 'С друзьями', callback_data = 'mistake_helpers')
    helpers.add(parents, alone, friends, grands)
    bot.send_media_group(call.message.chat.id,[telebot.types.InputMediaPhoto("https://i.imgur.com/Xx826ok.png"),telebot.types.InputMediaPhoto("https://i.imgur.com/o6nkite.png"),telebot.types.InputMediaPhoto("https://i.imgur.com/pkWoN0Z.png"),telebot.types.InputMediaPhoto("https://i.imgur.com/oZ16N1l.jpeg")])
    bot.send_message(call.message.chat.id, f'Если первое задание выполнено правильно, пришло время искать себе компанию для отдыха.\nИли отправишься в одиночку?', reply_markup = helpers)

@bot.callback_query_handler(func=lambda call: call.data == 'right_helpers')
def sum_task2(call):
    bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, отлично! Выполняй следующее задание!')
    video = open('videotask.mp4', 'rb') 
    bot.send_video(call.message.chat.id, video)
    bot.send_message(call.message.chat.id, f'Предлагаю переключить внимание.\nПосмотри отрывок мультфильма, в нём тебе подскажут, на чём опасно плавать.\nПосле просмотра, укажи этот предмет (1 слово). ')

@bot.message_handler(content_types=['text'])
def name(message):
    ur_name[message.chat.id] = message.text
    summer = types.InlineKeyboardButton(text = 'Лето', callback_data = 'sum')
    winter = types.InlineKeyboardButton(text = 'Зима', callback_data = 'win')
    game = types.InlineKeyboardMarkup()
    game.add (summer, winter)
    bot.send_message(message.chat.id, f'Теперь начнём игру, {ur_name[message.chat.id]}. За окном сейчас лето или зима?\nХмм, даже если глубокая осень или ранняя весна – не важно, ведь изучать правила безопасности можно круглогодично.\nМы предлагаем тебе определиться между двумя сезонами. От твоего выбора зависит: мы отправимся на пляжный отдых, либо окажемся рядом с зимним водоёмом.', reply_markup=game)
    bot.register_next_step_handler(message,sum_task3)

@bot.message_handler(content_types=['text'])
def sum_task3(message):
    if message.text == '10' and moment[message.chat.id] == 0:
        bot.send_message(message.chat.id, f'Молодчина! Выполняй следующее задание!')
        ships = types.InlineKeyboardMarkup()
        first = types.InlineKeyboardButton(text = 'Первый', callback_data = 'right_ship')
        second = types.InlineKeyboardButton(text = 'Второй', callback_data = 'mistake_ship')
        third = types.InlineKeyboardButton(text = 'Третий', callback_data = 'mistake_ship')
        fourth = types.InlineKeyboardButton(text = 'Четвертый', callback_data = 'mistake_ship')
        ships.add(first, second, third, fourth)
        bot.send_photo(message.chat.id, "https://i.imgur.com/HfqeuOf.jpeg")
        bot.send_message(message.chat.id, f'Дааа. Ситуация.\nЛайку срочно нужно попасть на противоположный берег.\nПомоги выбрать самый безопасный способ переправы.\nУкажи соответствующую цифру.', reply_markup = ships)
        bot.register_next_step_handler(message,sum_task3)
    else:
        if message.text == 'Матрас' or message.text == 'матрас':
            bot.send_message(message.chat.id, f'{ur_name[message.chat.id]}, ты молодец! Выполняй следующее задание!')
            bot.send_photo(message.chat.id, "https://i.imgur.com/Q30yuUu.jpeg")
            bot.send_message(message.chat.id, f'Отдыхая у водоёма, нужно быть внимательным. А ты обладаешь этим навыком? Предлагаю перейти к следующему заданию. Найди отличия на картинке, впиши их количество.')
            bot.register_next_step_handler(message,sum_task3)
        else:
            if message.text == 'Жилет' or message.text == 'жилет':
                bot.send_message(message.chat.id, f'{ur_name[message.chat.id]}, ты молодец! Выполняй следующее задание!') 
                help = types.InlineKeyboardMarkup()
                first = types.InlineKeyboardButton(text = '45123', callback_data = 'right_help')
                second = types.InlineKeyboardButton(text = '12345', callback_data = 'mistake_help')
                third = types.InlineKeyboardButton(text = '45231', callback_data = 'mistake_help')
                help.add(first, second, third)
                bot.send_photo(message.chat.id, "https://i.imgur.com/7BY8YGZ.jpeg")
                bot.send_message(message.chat.id, f'Заплывать за буйки нельзя! Наверняка ты об этом знаешь. \nПредставь, что отплыл от берега и понимаешь, что сил вернуться обратно уже нет. Как помочь себе? \nДавай разбираться, расставь шаги спасения в правильной последовательности.', reply_markup = help)   
            else:
                if message.text == '6' and moment[message.chat.id] == 1:
                    bot.send_message(message.chat.id, f'{ur_name[message.chat.id]}, ты молодец! Выполняй следующее задание!')
                    bot.send_photo(message.chat.id, 'https://imgur.com/mxmRYvs')
                    bot.send_message(message.chat.id, f'Как я радуюсь твоим правильным ответам!\nНо на этом мы не останавливаемся. \nЛови следующее задание.\nНайди и прочитай! Среди букв одного цвета зашифровано правило поведения на водоеме. Запиши его.')     
                    bot.register_next_step_handler(message,sum_task3)
                else:
                    if message.text == 'Не выходи на лёд водоёма' or message.text == 'не выходи на лёд водоёма':
                        bot.send_message(message.chat.id, f'Супер! Выполняй следующее задание!')
                        bot.send_photo(message.chat.id, 'https://imgur.com/YAmwLDK')
                        bot.send_message(message.chat.id, f'Оказаться в этом месте, которое мы зашифровали в ребусе,\nможет каждый, кто выходит на неокрепший лёд.\nХорошо, если рядом есть люди, чтобы придти на помощь бедолаге!\nРеши ребус. Впиши ответ')                        
                        bot.register_next_step_handler(message,sum_task3)
                    else:
                        if message.text == 'полынья' or message.text == 'Полынья':
                            bot.send_message(message.chat.id, f'Отлично, {ur_name[message.chat.id]}! Выполняй следующее задание!')
                            failur = types.InlineKeyboardMarkup()
                            first = types.InlineKeyboardButton(text = 'Коньки', callback_data = 'right_fail')
                            second = types.InlineKeyboardButton(text = 'Шарф', callback_data = 'mistake_fail')
                            third = types.InlineKeyboardButton(text = 'Лыжи', callback_data = 'mistake_fail')
                            fourth = types.InlineKeyboardButton(text = 'Спасательный круг', callback_data = 'mistake_fail')
                            failur.add(first, second, third, fourth)
                            bot.send_media_group(message.chat.id,[telebot.types.InputMediaPhoto('https://i.imgur.com/A3ZWnYU.png'),telebot.types.InputMediaPhoto('https://i.imgur.com/2d7BRLr.png'),telebot.types.InputMediaPhoto('https://i.imgur.com/yaveQTN.png'),telebot.types.InputMediaPhoto('https://i.imgur.com/XNGPyQG.png')])
                            bot.send_message(message.chat.id, f'Ещё один секретик-советик для тебя.\nЕсли мы заметили, что человек провалился под лёд, сразу звони спасателям!\nПроси о помощи взрослых прохожих.\nТы точно сможешь им подсказать, чем лучше воспользоваться, чтобы помочь тонущему выбраться из полыньи.\nДелай выбор, хорошенько подумав. Укажи лишний предмет. \nУдачи! Я верю в тебя!', reply_markup=failur)        
                        else:
                            bot.send_message(message.chat.id, f'{ur_name[message.chat.id]}, ошибка. Побробуй ещё раз')      
                            if debugg[message.chat.id] == 0:
                                bot.register_next_step_handler(message,sum_task3)

@bot.callback_query_handler(func=lambda call: call.data == 'mistake_ship')
def sum_task4(call):
    bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '')
    bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    ships = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = 'Первый', callback_data = 'right_ship')
    second = types.InlineKeyboardButton(text = 'Второй', callback_data = 'mistake_ship')
    third = types.InlineKeyboardButton(text = 'Третий', callback_data = 'mistake_ship')
    fourth = types.InlineKeyboardButton(text = 'Четвертый', callback_data = 'mistake_ship')
    ships.add(first, second, third, fourth)
    bot.send_photo(call.message.chat.id, "https://i.imgur.com/HfqeuOf.jpeg")
    bot.send_message(call.message.chat.id, f'Дааа. Ситуация.\nЛайку срочно нужно попасть на противоположный берег. \nПомоги выбрать самый безопасный способ переправы.\nУкажи соответствующую цифру.', reply_markup = ships)
    
@bot.callback_query_handler(func=lambda call: call.data == 'right_ship' or call.data == 'mistake_backpack')     
def sum_task5(call):
    bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '')
    if call.data == 'mistake_backpack':
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    else:
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ты молодец! Выполняй следующее задание!') 
    backpack = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = '1234', callback_data = 'mistake_backpack')
    second = types.InlineKeyboardButton(text = '35', callback_data = 'mistake_backpack')
    third = types.InlineKeyboardButton(text = '1235', callback_data = 'right_backpack')
    backpack.add (first, second, third)
    bot.send_media_group(call.message.chat.id,[telebot.types.InputMediaPhoto("https://i.imgur.com/87KHnEw.jpeg"),telebot.types.InputMediaPhoto("https://i.imgur.com/etq0Bii.jpeg"),telebot.types.InputMediaPhoto("https://i.imgur.com/7Lg5UbX.jpeg"),telebot.types.InputMediaPhoto("https://i.imgur.com/NTAMQZE.jpeg"), telebot.types.InputMediaPhoto("https://i.imgur.com/JCnuXGM.jpeg")])
    bot.send_message(call.message.chat.id, f'Давай заглянем в твой рюкзак, те ли ты вещи у тебя с собой в рюкзаке?\nВыбери изображения, которые не навредят твоему отдыху.', reply_markup = backpack) 

@bot.callback_query_handler(func  = lambda call: call.data == 'right_backpack' or call.data == 'mistake_costume')
def sum_task6(call):
    bot.edit_message_reply_markup(call.message.chat.id, message_id= call.message.message_id, reply_markup= '')
    if call.data == 'mistake_costume':
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    else:
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, круто! Выполняй следующее задание!') 
    costume = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = 'Первый', callback_data = 'right_costume')
    second = types.InlineKeyboardButton(text = 'Второй', callback_data = 'mistake_costume')
    third = types.InlineKeyboardButton(text = 'Третий', callback_data = 'mistake_costume')
    fourth = types.InlineKeyboardButton(text = 'Четвёртый', callback_data = 'mistake_costume')
    costume.add(first, second, third, fourth)
    bot.send_media_group(call.message.chat.id,[telebot.types.InputMediaPhoto("https://i.imgur.com/zGPlWGR.jpeg"),telebot.types.InputMediaPhoto("https://i.imgur.com/UPkVFrb.jpeg"),telebot.types.InputMediaPhoto("https://i.imgur.com/itDonM2.jpeg"),telebot.types.InputMediaPhoto("https://i.imgur.com/ZrVk2hm.jpeg")])
    bot.send_message(call.message.chat.id, f'Ты уже почти эксперт, половина заданий позади.\nНу-ка, взгляни, чей костюм лучше всего подходит для плавания?', reply_markup=costume)

@bot.callback_query_handler(func = lambda call: call.data == 'right_costume')
def sum_task7(call):
    bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup= '')
    bot.send_message(call.message.chat.id, f'Супер! Выполняй следующее задание!')
    bot.send_photo(call.message.chat.id, "https://i.imgur.com/X5elkLo.png")
    bot.send_message(call.message.chat.id, f'Этот предмет нужен не только рыбаку, при катании на катамаране или сапборде – это незаменимая вещь. \nРеши ребус и узнаешь, на что я намекаю.')

@bot.callback_query_handler(func = lambda call: call.data == 'mistake_help')
def sum_task8(call):
    bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    bot.edit_message_reply_markup(call.message.chat.id, message_id= call.message.message_id, reply_markup= '')
    help = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = '45123', callback_data = 'right_help')
    second = types.InlineKeyboardButton(text = '12345', callback_data = 'mistake_help')
    third = types.InlineKeyboardButton(text = '45231', callback_data = 'mistake_help')
    help.add(first, second, third)
    bot.send_photo(call.message.chat.id, "https://i.imgur.com/7BY8YGZ.jpeg")
    bot.send_message(call.message.chat.id, f'Заплывать за буйки нельзя! Наверняка ты об этом знаешь. \nПредставь, что отплыл от берега и понимаешь, что сил вернуться обратно уже нет. Как помочь себе? \nДавай разбираться, расставь шаги спасения в правильной последовательности.', reply_markup = help)  

@bot.callback_query_handler(func = lambda call: call.data == 'right_help' or call.data == 'mistake_place')
def sum_task9(call):
    if call.data == 'mistake_place':
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    else:
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ты молодец! Выполняй следующее задание!')    
    bot.edit_message_reply_markup(call.message.chat.id, message_id= call.message.message_id, reply_markup= '')
    place = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = 'Дривяты', callback_data = 'right_place')
    second = types.InlineKeyboardButton(text = 'Туда', callback_data = 'mistake_place')
    third = types.InlineKeyboardButton(text = 'На озеро', callback_data = 'mistake_place')
    place.add (first, second, third)
    bot.send_photo(call.message.chat.id, "https://i.imgur.com/wYEIdX8.jpeg")
    bot.send_message(call.message.chat.id, f'У нас внештатная ситуация.\nКажется, один из отдыхающих тонет. \nСрочно вызываем спасателей по номеру 112!\nНапиши, куда им приехать. ', reply_markup=place)
@bot.callback_query_handler(func = lambda call: call.data == 'right_place' or call.data == 'right_river')
def final(call):
    global debugg
    debugg[call.message.chat.id] = 1
    bot.edit_message_reply_markup(call.message.chat.id, message_id= call.message.message_id, reply_markup= '')
    bot.send_message(call.message.chat.id, f'Круто! Все задания позади! \nЯ в тебе не сомневался! \nВместе мы преодолели верхушку айсберга под названием «Безопасность жизнедеятельности».\nРад, что нам удалось втянуть тебя в наш водоворот знаний.\nЛови сертификат МЧС на память о нашем приключнеии. Распечатай его, впиши имя и вклей фотографию.\nКстати, можешь помочь продвинуть нашу игру через соцсети:\nотмечай её в своих сторис, давай обратную связь, делись ею с друзьями! \nА мы прощаемся, безопасных будней тебе, {ur_name[call.message.chat.id]}!')
    bot.send_photo(call.message.chat.id, 'https://i.imgur.com/xvoKrLv.jpeg')
@bot.callback_query_handler(func = lambda call: call.data == 'win' or call.data == 'mistake_ice')
def win_task1(call):
    if (call.data == 'mistake_ice'):
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')   
    bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '')
    ice = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = 'Серый', callback_data = 'mistake_ice')
    second = types.InlineKeyboardButton(text = 'Голубой', callback_data = 'right_ice')
    third = types.InlineKeyboardButton(text = 'Белый', callback_data = 'mistake_ice')
    fourth = types.InlineKeyboardButton(text = 'Жёлтый', callback_data = 'mistake_ice')
    ice.add (first, second, third, fourth)
    bot.send_photo(call.message.chat.id, 'https://i.imgur.com/BIO0kEb.jpeg')
    bot.send_message(call.message.chat.id, f'Бр-р-р, холодно! \nНадеялся, что ты выберешь лето. \nНу, зима, так зима. \nМы очутились у водоёма, выходить на него при любых обстоятельствах не советую, даже если толщина льда достигла минимально допустимой отметки в 7 сантиметров.\nКстати, ты знал, что оттенок льда указывает на его прочность?\nПомоги Лайку разобраться с этим вопросом, укажи, в какой цвет окрашивается самый прочный лёд?', reply_markup=ice)

@bot.callback_query_handler(func = lambda call: call.data == 'mistake_situation' or call.data == 'right_ice')
def win_task2(call):
    if (call.data == 'mistake_situation'):
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    else:
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ты молодец! Выполняй следующее задание!')     
    bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '')
    situation = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = 'Первый', callback_data = 'mistake_situation')
    second = types.InlineKeyboardButton(text = 'Второй', callback_data = 'mistake_situation')
    third = types.InlineKeyboardButton(text = 'Третий', callback_data = 'mistake_situation')
    fourth = types.InlineKeyboardButton(text = 'Четвёртый', callback_data = 'right_situation')
    situation.add(first, second, third, fourth)
    bot.send_media_group(call.message.chat.id,[telebot.types.InputMediaPhoto("https://i.imgur.com/RZtvlEr.jpeg"),telebot.types.InputMediaPhoto("https://i.imgur.com/moRx468.jpeg"),telebot.types.InputMediaPhoto("https://i.imgur.com/SoaYBaG.jpeg"),telebot.types.InputMediaPhoto("https://i.imgur.com/anztskU.jpeg")])
    bot.send_message(call.message.chat.id, f'Наши герои спецотряда 112 разбежались по своим делам,\nдавай подсмотрим за их развлечениями. \nЧует моё сердце, быть беде! \nПодскажи, кто в безопасности и кому спасателям помогать не надо?', reply_markup=situation)

@bot.callback_query_handler(func = lambda call: call.data == 'right_situation')
def win_task3(call):
    global moment
    bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '')
    moment[call.message.chat.id] = 1
    bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, отлично! Выполняй следующее задание!')  
    bot.send_photo(call.message.chat.id, 'https://imgur.com/UuR9eS3')
    bot.send_message(call.message.chat.id, f'А ты знаешь, что зима – один из самых травмоопасных сезонов?\nОбращай внимание на сосульки на крышах, выбирай безопасные места для катания с горок, избегай переохлаждений! \nКак видишь, нужно быть бдительным.\nДавай проверим твою внимательность, сколько отличий найдёшь на картинке?')

@bot.callback_query_handler(func = lambda call: call.data == 'mistake_fail')
def win_task4(call):
    bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '')
    failur = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = 'Коньки', callback_data = 'right_fail')
    second = types.InlineKeyboardButton(text = 'Шарф', callback_data = 'mistake_fail')
    third = types.InlineKeyboardButton(text = 'Лыжи', callback_data = 'mistake_fail')
    fourth = types.InlineKeyboardButton(text = 'Спасательный круг', callback_data = 'mistake_fail')
    failur.add(first, second, third, fourth)
    bot.send_media_group(call.message.chat.id,[telebot.types.InputMediaPhoto('https://i.imgur.com/A3ZWnYU.png'),telebot.types.InputMediaPhoto('https://i.imgur.com/2d7BRLr.png'),telebot.types.InputMediaPhoto('https://i.imgur.com/yaveQTN.png'),telebot.types.InputMediaPhoto('https://i.imgur.com/XNGPyQG.png')])
    bot.send_message(call.message.chat.id, f'Ещё один секретик-советик для тебя.\nЕсли ты заметил, что человек провалился под лёд, сразу звони спасателям!\nПроси о помощи взрослых прохожих.\nТы точно сможешь им подсказать, чем лучше воспользоваться, чтобы помочь тонущему выбраться из полыньи.\nДелай выбор, хорошенько подумав. Укажи лишний предмет. \nУдачи! Я верю в тебя!', reply_markup = failur)     

@bot.callback_query_handler(func = lambda call: call.data == 'right_fail' or call.data == 'mistake_useless')
def win_task5(call):
    if (call.data == 'mistake_useless'):
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    else:
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ты молодец! Выполняй следующее задание!')     
    bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '') 
    useless = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = '1', callback_data = 'right_useless')
    second = types.InlineKeyboardButton(text = '2', callback_data = 'mistake_useless')
    third = types.InlineKeyboardButton(text = '3', callback_data = 'mistake_useless')
    useless.add(first, second, third)
    bot.send_photo(call.message.chat.id, 'https://i.imgur.com/Y58X59d.jpeg')
    bot.send_message(call.message.chat.id, f'Что мы всё о грустном!\nВедь спасатели лёд не запрещают,\nспасатели предупреждают, что к такому виду отдыха нужно подходить с умом!\nДавай поможем Эйнштейну собраться на рыбалку, не забыв нужных  вещей!\nПосмотри на картинку, сколько бесполезных предметов изображено на картинке?', reply_markup=useless)

@bot.callback_query_handler(func = lambda call: call.data == 'mistake_konki' or call.data == 'right_useless')
def win_task6(call):
    if (call.data == 'mistake_konki'):
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    else:
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, супер! Выполняй следующее задание!')     
    konki = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = 'Первое', callback_data = 'mistake_konki')
    second = types.InlineKeyboardButton(text = 'Второе', callback_data = 'mistake_konki')
    third = types.InlineKeyboardButton(text = 'Третье', callback_data = 'right_konki')
    konki.add(first, second, third)
    bot.send_media_group(call.message.chat.id,[telebot.types.InputMediaPhoto('https://i.imgur.com/amuYbU8.jpeg'),telebot.types.InputMediaPhoto('https://i.imgur.com/u2ppgDA.png'),telebot.types.InputMediaPhoto('https://i.imgur.com/DxsUIaT.jpeg')])
    bot.send_message(call.message.chat.id, f'Мы уже готовы брать тебя в команду спасателей!\nПравда,  если тебе исполнилось 18 лет.\nА пока ты раздумываешь над моим предложением, лови следующее задание.\nПомоги выбрать наиболее безопасное место для катания на коньках.', reply_markup = konki)

@bot.callback_query_handler(func = lambda call: call.data == 'right_konki' or call.data == 'mistake_castle')
def win_task7(call):
    if (call.data == 'mistake_castle'):
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    else:
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, молодчинка! Выполняй следующее задание!')
    castle = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = '12345', callback_data = 'mistake_castle')
    second = types.InlineKeyboardButton(text = '24351', callback_data = 'right_castle')
    third = types.InlineKeyboardButton(text = '52431', callback_data = 'mistake_castle')
    castle.add(first,second,third)
    bot.send_photo(call.message.chat.id, 'https://i.imgur.com/ZxDj9nj.jpeg')
    bot.send_message(call.message.chat.id,f'Ледовый дворец или каток за школой – лучшее место для катания на коньках.\nА те, кто это делает на водоёме, рискует угодить в ледяную ловушку.\nУ попавших туда есть несколько минут, чтобы спастись.\nДавай разбираться. Расставь шаги спасения в правильной последовательности.', reply_markup = castle)

@bot.callback_query_handler(func = lambda call: call.data == 'right_castle' or call.data == 'mistake_river')
def win_task8(call):
    if (call.data == 'mistake_river'):
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ошибка. Побробуй ещё раз')
    else:
        bot.send_message(call.message.chat.id, f'{ur_name[call.message.chat.id]}, ты молодец! Выполняй следующее задание!')
    river = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text = 'р. Кавалерка', callback_data = 'right_river')
    second = types.InlineKeyboardButton(text = 'Сюда', callback_data = 'mistake_river')
    third = types.InlineKeyboardButton(text = 'На речку', callback_data = 'mistake_river')
    river.add(first,second,third)
    bot.send_photo(call.message.chat.id, 'https://i.imgur.com/LccXdzv.jpeg')
    bot.send_message(call.message.chat.id, f'Ты молодец! \nХочу поделиться с тобой историей, которая произошла с моим знакомым.\nОднажды, прогуливаясь по вечернему городу, он услышал крик. Звук был уже таким хриплым, надрывным…\nВаня быстро сориентировался и понял, что следовать нужно к реке, что протекает на окраине парка.\nЧеловек тонет! Но, паниковать нельзя! Быстро схватил телефон и набрал номер 112. \n\nВзгляни на картинку, по какому адресу нужно приезжать спасателям?', reply_markup=river)

bot.polling(non_stop=True)