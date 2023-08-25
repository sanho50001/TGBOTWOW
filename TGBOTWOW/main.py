import telebot
import datetime
import wowgame
# from wowgame import bigstart
from game.user import User
from game.settings.settingstelegram import CommandsTelegram
from game.settings.settings_game import settings


# Запуск бота по токену
bot = telebot.TeleBot('5824374073:AAEfAlM2tCZzknjkol1_NKyPnzfaMYI31BE')
print('Бот начал свою работу.')


user = User()

# Отпределение команд бота
TGBOT = CommandsTelegram(bot)


# Хандлеры для вызова команд

# Хендлер для регистрации
@bot.message_handler(commands=["reg"])
def reg(message):
    if wowgame:
        user.set_id_account(message.from_user.id)
    bot.send_message(message.from_user.id, 'Начинаем процесс регистрации...')
    started = wowgame.Start()
    started.cret(message.from_user.id)


# Хендлер старта
@bot.message_handler(commands=['start'])
def start(message):
    """Обработчик комманды /start"""

    user.set_id_account(message.from_user.id)
    print(f'Чат ID: {message.chat.id} | {message.from_user.first_name} {message.from_user.last_name}: {message.text}')
    wowgame.StartGame().welcom(message=message)

# хендлер принимающий любой вид текста которые не прошли проверку на команду
@bot.message_handler(commands=['test'])
def get_text_messages(message):
    """Обработчик всех сообщений"""
    if wowgame:
        user.set_id_account(message.from_user.id)
    wowgame.bigstart.r2()



# хендлер принимающий любой вид текста которые не прошли проверку на команду
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """Обработчик всех сообщений"""
    if wowgame:
        user.set_id_account(message.from_user.id)
    TGBOT.getTextMessages(message=message)


# Хендлер который перехватывает все инлайн кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):

    """Функция callback_data перехвата всех вызовов которые возникают при нажатии inline кнопок
    Принимает все вызовы перехватом и проходит по условию, если условие сошлось - переходит дальше по фукнциям
    """
    # Вызов старта игры
    if call.data == 'startgame':
        wowgame.startgame.welcom()

    # Вызов регистрации героя
    elif call.data == 'reghero':
        if settings.get_language() == 'english':
            bot.send_message(wowgame.user.get_id_account(), 'Enter the name of the character')
            bot.register_next_step_handler(call.message,
                                           wowgame.CreatingHero().welcom_step_one_creating_hero(message=call.message.from_user))
        else:
            bot.send_message(wowgame.user.get_id_account(), 'Введите имя персонажа')
            bot.register_next_step_handler(call.message,
                                           wowgame.CreatingHero().welcom_step_one_creating_hero(message=call.message.from_user))
    # Вызов настроек
    elif call.data == 'settings':
        wowgame.BeginningStart().beginning_settings(call.message.from_user)

    # Вызовы языков
    elif call.data == 'ru':
        settings.set_language('русский')
        bot.send_message(wowgame.user.get_id_account(),
                         'Ваши языковые настройки были успешно изменены. Приятной игры!')
    elif call.data == 'eng':
        settings.set_language('english')
        bot.send_message(wowgame.user.get_id_account(),
                         'Your language settings have been successfully changed. Have a nice game!')

    # Вызовы классов
    elif call.data == 'warrior' or 'hunter' or 'paladin'\
            or 'rogue' or 'priest' or 'shaman'\
            or 'mage' or 'warlock' or 'druid' or 'dk':
        wowgame.creatinghero.two_step_creating_hero(message=call.message.from_user)

    elif call.data == 'history':
        pass


# Вечный пуллинг, чтобы бот принимал всегда сообщения
bot.polling(none_stop=True, interval=0)
print(f'Бот завершил работу в', datetime.datetime.now().strftime('Дата: %Y %m %d Время: %H:%M:%S'))




