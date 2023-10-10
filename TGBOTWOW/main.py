import telebot
import datetime
import wowgame
import time
# from wowgame import bigstart
from game.user import User
from game.settings.settingstelegram import CommandsTelegram
from game.settings.settings_game import settings
from dotenv import load_dotenv
import os
load_dotenv()
# Запуск бота по токену
bot = telebot.TeleBot(os.getenv('telebot_token'))
print('Бот начал свою работу в', datetime.datetime.now().strftime('Дата: %Y %m %d Время: %H:%M:%S'), '.')


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


# # Хендлер старта
# @bot.message_handler(commands=['start'])
# def start(message):
#     """Обработчик комманды /start"""
#
#     user.set_id_account(message.from_user.id)
#     print(f'Чат ID: {message.chat.id} | {message.from_user.first_name} {message.from_user.last_name}: {message.text}')
#     wowgame.StartGame().welcom(message=message)

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
    print(call.data)
    if call.message:
        # Вызов старта игры
        if call.data == 'startgame':
            wowgame.startgame.choice_hero_step_one()

        # Вызов регистрации героя
        elif call.data == 'reghero':
            time.sleep(1)

            if settings.get_language() == 'english':
                bot.edit_message_text(chat_id=wowgame.user.get_id_account(), message_id=call.message.id, text='Enter the name of the character', )
                time.sleep(1)
                bot.register_next_step_handler(
                    call.message,
                    wowgame.CreatingHero().welcom_step_one_creating_hero)
            else:
                bot.edit_message_text(chat_id=wowgame.user.get_id_account(), message_id=call.message.id, text='Введите имя персонажа')
                time.sleep(1)
                bot.register_next_step_handler(
                    call.message,
                    wowgame.CreatingHero().welcom_step_one_creating_hero)

        # Вызов настроек
        elif call.data == 'settings':
            wowgame.BeginningStart().beginning_settings(call.message.from_user)

        # Вызовы языков
        elif call.data == 'ru':
            settings.set_language('русский')
            os.environ['language'] = settings.get_language()
            bot.send_message(wowgame.user.get_id_account(),
                             'Ваши языковые настройки были успешно изменены. Приятной игры!')

        elif call.data == 'eng':
            settings.set_language('english')
            os.environ['language'] = settings.get_language()
            bot.send_message(wowgame.user.get_id_account(),
                             'Your language settings have been successfully changed. Have a nice game!')

        elif call.data == 'list_hero':
            wowgame.startgame.choice_hero_step_two()

        # Вызовы классов
        elif call.data == (
                'warrior' or 'hunter' or 'paladin'
                or 'rogue' or 'priest' or 'shaman'
                or 'mage' or 'warlock' or 'druid' or 'dk'
        ):
            wowgame.hero.hero.set_classes_hero(call.data)
            wowgame.creatinghero.two_step_creating_hero(message=call.message)

        elif call.data == 'hit':
            wowgame.battle.hit(hero=wowgame.hero.hero.get_name_hero(), npc=wowgame.npc.get_name_npc())

        elif call.data == 'spell':
            pass
        elif call.data == 'block':
            pass
        elif call.data == 'backpack':
            pass
        elif call.data == 'Up':
            wowgame.movement.set_coord_y(0.5)
            wowgame.movement.move()
        elif call.data == 'Down':
            wowgame.movement.set_coord_y(-0.5)
        elif call.data == 'Left':
            wowgame.movement.set_coord_x(-0.5)
        elif call.data == 'Right':
            wowgame.movement.set_coord_x(0.5)


        elif call.data == '1 Hero' or '1 Герой':
            pass
        elif call.data == '2 Hero' or '2 Герой':
            pass
        elif call.data == '3 Hero' or '3 Герой':
            pass
        elif call.data == 'history':
            pass





# Вечный пуллинг, чтобы бот принимал всегда сообщения
bot.polling(none_stop=True, interval=0)
print(f'Бот завершил работу в', datetime.datetime.now().strftime('Дата: %Y %m %d Время: %H:%M:%S'))




