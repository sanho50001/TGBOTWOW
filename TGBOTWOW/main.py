import telebot
import datetime
import wowgame
from game.settings.settingstelegram import CommandsTelegram

# Запуск бота по токену
bot = telebot.TeleBot('5824374073:AAEfAlM2tCZzknjkol1_NKyPnzfaMYI31BE')
print('Бот начал свою работу.')


# Отпределение команд бота
TGBOT = CommandsTelegram(bot)


# Хандлеры для вызова команд

# Хендлер для регистрации
@bot.message_handler(commands=["reg"])
def reg(message):
    bot.send_message(message.from_user.id, 'Начинаем процесс регистрации...')
    started = wowgame.Start()
    started.cret(message.from_user.id)

# Хендлер старта
@bot.message_handler(commands=['start'])
def start(message):
    print(f'Чат ID: {message.chat.id} | {message.from_user.first_name} {message.from_user.last_name}: {message.text}')
    wowgame.StartGame().welcom(message=message)

# хендлер принимающий любой вид текста которые не прошли проверку на команду
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    TGBOT.getTextMessages(message=message)


# Хендлер который перехватывает все инлайн кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    """Функция callback_data перехвата всех вызовов которые возникают при нажатии inline кнопок
    Принимает все вызовы перехватом и проходит по условию, если условие сошлось - переходит дальше по фукнциям
    """
    if call.data == 'startgame':
        wowgame.StartGame()

    elif call.data == 'reghero':
        wowgame.CreatingHero()

    elif call.data == 'settings':
        pass

    elif call.data == 'ru':
        pass

    elif call.data == 'eng':
        pass

    elif call.data == 'history':
        pass



# Вечный пуллинг, чтобы бот принимал всегда сообщения
bot.polling(none_stop=True, interval=0)
print(f'Бот завершил работу в', datetime.datetime.now().strftime('Дата: %Y %m %d Время: %H:%M:%S'))




