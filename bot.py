import telebot
TOKEN = '6362015862:AAH7UqzkJzs8pAoKT_Xvlw69CHGKLs8sMfE' # bot token from @BotFather
from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("👑")
    item2 = types.KeyboardButton("01.07.2023❤️")
    item3 = types.KeyboardButton("💦")
    item4 = types.KeyboardButton("🐺рр-р...")
    item5 = types.KeyboardButton("🤗️")
    item6 = types.KeyboardButton("🌃")
    item7 = types.KeyboardButton("🐺")

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, созданный,чтобы поднять твоё нстроение, когда нет рядом твоего Волчонка !!!❤️💋❤️ .".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
@bot.message_handler(func=lambda msg: msg.text == '🐺👅🐰')
def get_user_photo(message: types.Message):
    bot.send_photo(message.chat.id, "https://i.pinimg.com/originals/14/57/67/145767e104272de2f9d80afdb8083696.png")
@bot.message_handler(func=lambda msg: msg.text == '🌃')
def get_user_photo(message: types.Message):
    bot.send_photo(message.chat.id, "https://disk.yandex.ru/i/vcHVqcMC97Bxbw")
@bot.message_handler(func=lambda msg: msg.text == '🤗')
def get_user_photo(message: types.Message):
    bot.send_photo(message.chat.id, "https://postila.ru/data/7f/89/02/bc/7f8902bc6c1da2b8e8887343459bec33100f20cda30c1cb5b2f1d952a120e3f2.jpg")


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🐺':
            bot.send_message(message.chat.id, text="Я тебя очень сильно люблю😘❤️️")
        elif message.text == '01.07.2023❤️':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да, любимый❤️", callback_data='good')
            item2 = types.InlineKeyboardButton("Нет, Илья", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Заюш , навалим репчины?)', reply_markup=markup)
        elif message.text == '💦':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🤤")
            item2 = types.KeyboardButton("🌟🌟🌟")
            back = types.KeyboardButton("⬅️Назад в меню")
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Малыш, я делаю пистолет Ярыгина🫦', reply_markup=markup)
        elif message.text == '🐺рр-р...':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🐺Ррр")
            item2 = types.KeyboardButton("🐺рр❤️")
            back = types.KeyboardButton("⬅️Назад в меню")
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Укусил за бочок(не больно)😎', reply_markup=markup)
        elif message.text == '💦':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("⬅️Назад в меню")
        elif message.text == '🌟🌟🌟':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, text="🐺👅🐱💦🐰")
            back = types.KeyboardButton("⬅️Назад в меню")
            markup.add(back)
        elif message.text == '🤤':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, text="Зай, я делаю это в робе😏")
            back = types.KeyboardButton("⬅️Назад в меню")
            markup.add(back)
        elif message.text == '🐺Ррр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, text="🐺👃🐺🤚🍑🐺😘👃❤️🐰")
            back = types.KeyboardButton("⬅️Назад в меню")
            markup.add(back)
        elif message.text == '🐺рр❤️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, text="🐺🤚🐱🐰😘🐰🍌✖️2️⃣✖️3️⃣...✖️🔟🐱💦✖️2️⃣✖️3️⃣...✖️🔟🐺👉👌🐰🌪🌟❤️♾️🐰")
            back = types.KeyboardButton("⬅️Назад в меню")
            markup.add(back)
        elif message.text == '🤗️':
            bot.send_message(message.chat.id, text='Иди ко мне, мой котёнок🐱Обнимаю крепко-крепко🫂Целую сильно😚Кусаю за носик🐺👃и целую в лобик❤️')
        elif message.text == '👑':
            bot.send_message(message.chat.id, text='Ты у меня САМАЯ лучшая👸')
        elif message.text == '⬅️Назад в меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("👑")
            item2 = types.KeyboardButton("01.07.2023❤️")
            item3 = types.KeyboardButton("💦")
            item4 = types.KeyboardButton("🐺рр-р...")
            item5 = types.KeyboardButton("🤗️")
            item6 = types.KeyboardButton("🌃")
            item7 = types.KeyboardButton("🐺")
            markup.add(item1, item2, item3, item4, item5, item6, item7)


            bot.send_message(message.chat.id, '⬅️Назад в меню', reply_markup=markup)


        else:
            bot.send_message(message.chat.id, 'К сожелению я не умею отвечать😣')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Лето жизни моего 22-го года.\nНакануне незапланированого выходного.\nОно совсем не предвещало такого исхода,\nНо затусить позволяла погода.\nСлегка размыты планы на вечер, и ладно.\n Найти их никогда не приходилось накладно.\nЯ и не подозреваю о самом главном.\nЧто этой ночью поеду за "кладом")\n Во дворе Цветочной всё проходит как надо.\n Культурно отдыхаем немного непривычным сквадом.\nПодумать не мог, что,возможно,совсем рядом\nНахожусь с тем самым, драгоценным "кладом")\nПогода по классике: жара и тополиный пух.\n Кто-то из нас уже в предвкушении.\n Количество нашего сквада сокращается до двух.\n Тут принимается банальное решение.Тупо поехать в клуб.\n "Антоха, по-любому домой заехать надо.\nПереодеться и дунуть самосада".\nВ голове и мысли нету, правда,\n Что лето 23-го года, и я еду в клуб за "кладом")\n Обстановка для нас в целом привычная.\nЗдесь просто отдыхает народ.\nНаш маршрут проложен весьма логично.\nДвигаемся от бара до танцпола и наоборот.\nЭта тусовка наскучила, атмосфера вообще не берëт.\nВискарь на танцполе выходит быстрее, чем мы его пьëм.\nПо маршруту подходим к бару вдвоëм,\nИ я внезапно вижу её....\nЛюбовь с первого взгляда? Не думаю.\nНо.... Искра, буря, безумие.\nТогда и не знал, что встретился взглядом\nС тем, самым драгоценным "кладом")\nОбычно, я не вёл себя настолько смело,\nНо, как будто, услышал сигнал свыше.\nПоказалось, что она не просто посмотрела.\nНужно пойти и познакомиться поближе.\nДальше смутно помню разговоры о репе.\nПомню, как стрелял её номер и оставил ей свой.\nНо отчётливо помню, как на рассвете,\nЯ разделил с ней её дорогу домой.\nПомню, в то утро я носил её на руках.\nМеня слегка качало, но совсем не было ветра.\nЯ не забуду недоумение от моего поведения в её глазах\nИ те поцелуи в лесу, за торговым центром.\nМне стоило вести себя по человечней, конечно.\nОна постоянно говорила, что я сумасшедший.\nЯ смотрел в глубину её глаз, видел бесконечность.\nГлядя на них, хотелось рассуждать о вечном.\nВсю дорогу я думал о том, какая же она красивая\nМы дошли до её дома, но почему-то прошли его мимо.\nПочему такой расклад, она не объяснила.\n"Не всё так просто, так надо, так необходимо".\nМы прощались с ней долго и очень мило.\nОна меня совсем не хило зацепила.\nЯ проводил ее взглядом из окна автомобиля.\nИ думал о том, какая же она красивая.\nРодная, ты же знаешь.Я тебе сам это сказал.\nКак же сильно я тебя люблю.\nЯ очень сильно люблю тебя, зай.\nСказал, говорю и ещё не раз повторю.\nТогда я не знал о чувствах, которые скоро познаю.\nНе знал, что такие существуют вообще.\nНе знал, что совсем не "клад") моя зая.\nНе знал, что она - моё сокровище...')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id,'Нажми да - это приказ!😠')
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🐺",
                reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                text="Помни, Зайчонок🐰, я ТВОЙ Волчонок\n🐺❤️🐰")
    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)
stop(b'\r', 'Press Enter to exit')
