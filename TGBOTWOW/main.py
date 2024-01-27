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

# Отпределение команд бота
TGBOT = CommandsTelegram(bot)


# Хандлеры для вызова команд

# # Хендлер для регистрации
# @bot.message_handler(commands=["reg"])
# def reg(message):
#     if wowgame:
#         user.set_id_account(message.from_user.id)
#     bot.send_message(message.from_user.id, 'Начинаем процесс регистрации...')
#     started = wowgame.Start()
#     started.cret(message.from_user.id)


# Хендлер старта
@bot.message_handler(commands=['start'])
def start(message):
    """Обработчик комманды /start"""

    wowgame.user.set_id_account(message.from_user.id)
    print(f'Чат ID: {message.chat.id} | {message.from_user.first_name} {message.from_user.last_name}: {message.text}')
    wowgame.StartGame().welcom()


# хендлер принимающий любой вид текста которые не прошли проверку на команду
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """Обработчик всех сообщений"""
    if wowgame:
        wowgame.user.set_id_account(message.from_user.id)
    TGBOT.getTextMessages(message=message)


# Хендлер который перехватывает все инлайн кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):

    """Функция callback_data перехвата всех вызовов которые возникают при нажатии inline кнопок
    Принимает все вызовы перехватом и проходит по условию, если условие сошлось - переходит дальше по фукнциям
    """
    # print(call.data)
    # print(call.message)
    if call.message:
        wowgame.user.set_id_account(call.message.chat.id)
        wowgame.settings.set_last_message_id(call.message.id)
        # Вызов старта игры
        if call.data == 'startgame':
            wowgame.startgame.choice_hero_step_one(message=call.message)

        # Вызов регистрации героя
        elif call.data == 'reghero':
            markup_inline = wowgame.types.InlineKeyboardMarkup()
            markup_inline.add(wowgame.types.InlineKeyboardButton(text=settings.text_menu_button_game_set_name_hero(),
                                                                 callback_data='none'))
            time.sleep(1)
            bot.edit_message_text(chat_id=wowgame.user.get_id_account(), message_id=wowgame.settings.get_last_message_id(),
                                  text=settings.text_menu_button_game_set_name_hero(), reply_markup=markup_inline)
            # wowgame.creatinghero.creatinghero(message=call.message)
            bot.register_next_step_handler(
                call.message,
                wowgame.creatinghero.creatinghero_step_one_creating_hero)

        # Вызов настроек
        elif call.data == 'settings':
            # wowgame.user.set_id_account(call.message.chat.id)
            wowgame.settings_game.beginning_settings()

        elif call.data == 'list_hero':
            # user.set_id_account(call.message.chat.id)
            wowgame.startgame.choice_hero_step_two()

        # Вызовы языков
        elif call.data in ('ru', 'eng'):
            if call.data == 'ru':
                settings.set_language('русский')
            elif call.data == 'eng':
                settings.set_language('english')

            wowgame.settings_game.set_language()

        # Вызовы классов
        elif call.data in (
                'warrior', 'hunter', 'paladin'
                , 'rogue',  'priest',  'shaman'
                , 'mage',  'warlock',  'druid',  'dk'
        ):
            wowgame.hero.hero.set_classes_hero(call.data.capitalize())
            wowgame.creatinghero.creatinghero_two_step_creating_hero()

        elif call.data == 'hit':
            wowgame.battle.hit(hero=wowgame.hero.hero.get_name_hero(), npc=wowgame.npc.get_name_npc())

        elif call.data == 'spell':
            pass
        elif call.data == 'block':
            pass
        elif call.data == 'backpack':
            pass
        elif call.data == 'Up':
            wowgame.movement.movement.set_coord_y(y=0.5)
            wowgame.movement.move(message=call.message)
        elif call.data == 'Down':
            wowgame.movement.movement.set_coord_y(y=(-0.5))
            wowgame.movement.move(message=call.message)
        elif call.data == 'Left':
            wowgame.movement.movement.set_coord_x(x=(-0.5))
            wowgame.movement.move(message=call.message)
        elif call.data == 'Right':
            wowgame.movement.movement.set_coord_x(x=0.5)
            wowgame.movement.move(message=call.message)
        elif call.data in ('Hero') or ('Герой'):
            name_hero = call.data[8:]
            wowgame.startgame.choice_hero_step_three(name_hero=name_hero, message=call.message)
        elif call.data == 'history':
            pass





# Вечный пуллинг, чтобы бот принимал всегда сообщения
bot.polling(none_stop=True, interval=0)
print(f'Бот завершил работу в', datetime.datetime.now().strftime('Дата: %Y %m %d Время: %H:%M:%S'))




