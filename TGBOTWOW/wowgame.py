import random
import time
import datetime
from game.settings.settingstelegram import CommandsTelegram
from game.armor import Armor
from game.weapon import Weapon
from game.settings.settings_game import settings
from game.battle import Battle
from game.loot import Loot
from game.movement import Movement
from game.potion import Potion
from game.tavern import Tavern
from game.tranquility import Tranquility
from game.db_commands import DataBase
from main import bot
from telebot import types

# Инициализация Базы Данных
db = DataBase()


class User:
    def __init__(self):
        self.id_account = None

    def set_id_account(self, id_account):
        self.id_account = id_account

    def get_id_account(self):
        return self.id_account
    pass

user = User()

# class ClassHero:
#     def __init__(self):
#         self.warrior = 'Warrior'
#         self.hunter = 'Hunter'
#         self.paladin = 'Paladin'
#         self.rogue = 'Rogue'
#         self.priest = 'Priest'
#         self.shaman = 'Shaman'
#         self.mage = 'Mage'
#         self.warlock = 'Warlock'
#         self.druid = 'Druid'
#         self.death_knight = 'Death Knight'
#


class BeginningStart:

    def r2(self, message):
        # exp = db.Get_Hero()
        #
        # bot.send_message(message.from_user.id, settings.text_on_start_game(), reply_markup=markup_reply)
        pass

    def beginning_settings(self, message):

        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup()
        markup_inline = types.InlineKeyboardMarkup()

        # кнопки
        rus_language_button = types.KeyboardButton('Русский')
        english_language_button = types.KeyboardButton('English')

        # создание кнопки и добавление туда кнопок.
        markup_reply.add(rus_language_button, english_language_button)

        # Кнопки с выбором
        markup_inline.add(
            types.InlineKeyboardButton(text='Русский язык', callback_data='ru'),
            types.InlineKeyboardButton(text='English language', callback_data='eng'),
        )
        bot.send_message(user.get_id_account(), settings.text_on_start_game(), reply_markup=markup_reply)
        bot.send_message(user.get_id_account(), 'Commands', reply_markup=markup_inline)


class StartGame:

    def welcom(self, message):


        # Добавляем пользователя в базу данных
        db.Create_User(id_account=message.from_user.id)

        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup()
        markup_inline = types.InlineKeyboardMarkup()

        # кнопки
        start_game_button = types.KeyboardButton('/startgame')
        creating_hero_button = types.KeyboardButton('/reghero')
        settings_button = types.KeyboardButton('/settings')

        # создание кнопки и добавление туда кнопок.
        markup_reply.add(creating_hero_button, start_game_button, settings_button)

        # Если язык пользователем установлен 'english', то берется английская адаптация
        if settings.get_language() == 'english':
            markup_inline.add(
                types.InlineKeyboardButton(text='start game', callback_data='startgame'),
                types.InlineKeyboardButton(text='register hero', callback_data='reghero'),
                types.InlineKeyboardButton(text='settings', callback_data='settings'),
            )

            bot.send_message(user.get_id_account(), settings.text_on_start_game(), reply_markup=markup_reply)
            bot.send_message(user.get_id_account(), 'Commands', reply_markup=markup_inline)
        # Если язык пользователем установлен 'русский', то берется русская адаптация
        else:
            markup_inline.add(
                types.InlineKeyboardButton(text='старт игры', callback_data='startgame'),
                types.InlineKeyboardButton(text='зарегистрировать героя', callback_data='reghero'),
            types.InlineKeyboardButton(text='настройки', callback_data='settings'),
            )
            bot.send_message(user.get_id_account(), settings.text_on_start_game(), reply_markup=markup_reply)
            bot.send_message(user.get_id_account(), 'Комманды', reply_markup=markup_inline)


#
# class LeftHand(Weapon):
#     """Класс левой руки"""
#     def __init__(self):
#         super().__init__()
#         pass
#     pass
#
#
# class RightHand(Weapon):
#     """Класс правой руки"""
#     def __init__(self):
#         super().__init__()
#         pass
#     pass


class Backpack:
    """Класс Сумки у персонажа"""
    def __init__(self):
        self.backpack = []
        pass
    pass


class Zone:
    """Класс Зоны """
    def __init__(self, name_location):
        self.name_location = name_location
        self.name_zone = ''
        self.spot = []
        self.spot_npc = []
        pass
    pass


class NPC:
    """Класс НПС"""
    def __init__(self, name_npc):
        self.name_npc = name_npc
        self.status = 'Alive'
        self.health = 100
        self.loot = {}
        # self.armor = Armor()
        # self.left_hand = LeftHand()
        # self.right_hand = RightHand()
        pass
    pass


class Hero(User):
    """Класс Героя"""
    def __init__(self):
        super().__init__()
        self.name_hero = ''  # имя персонажа
        self.classes = '' #класс героя
        self.status = 'Online'
        self.health = 100
        # self.armor = Armor()
        # self.backpack = Backpack()
        # self.left_hand = LeftHand()
        # self.right_hand = RightHand()

    def set_name_hero(self, name_hero):
        self.name_hero = name_hero

    def set_classes_hero(self, classes):
        self.classes = classes

    def get_name_hero(self):
        return self.name_hero

    def get_classes_hero(self):
        return self.classes


hero = Hero()


class CreatingHero:

    def welcom_step_one_creating_hero(self, message):
        hero.set_name_hero(message.from_user.text)

        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup()
        markup_inline = types.InlineKeyboardMarkup()

        # Если язык пользователем установлен 'english', то берется английская адаптация
        if settings.get_language() == 'english':
            # кнопки eng
            eng_classes_warrior = types.KeyboardButton('Warrior')
            eng_classes_hunter = types.KeyboardButton('Hunter')
            eng_classes_paladin = types.KeyboardButton('Paladin')
            eng_classes_rogue = types.KeyboardButton('Rogue')
            eng_classes_priest = types.KeyboardButton('Priest')
            eng_classes_shaman = types.KeyboardButton('Shaman')
            eng_classes_mage = types.KeyboardButton('Mage')
            eng_classes_warlock = types.KeyboardButton('Warlock')
            eng_classes_druid = types.KeyboardButton('Druid')
            eng_classes_death_knight = types.KeyboardButton('Death Knight')

            # создание кнопки и добавление туда кнопок.
            markup_reply.add(
                eng_classes_warrior,
                eng_classes_hunter,
                eng_classes_paladin,
                eng_classes_rogue,
                eng_classes_priest,
                eng_classes_shaman,
                eng_classes_mage,
                eng_classes_warlock,
                eng_classes_druid,
                eng_classes_death_knight,
            )

            markup_inline.add(
                types.InlineKeyboardButton(text='Warrior', callback_data='warrior'),
                types.InlineKeyboardButton(text='Hunter', callback_data='hunter'),
                types.InlineKeyboardButton(text='Paladin', callback_data='paladin'),
                types.InlineKeyboardButton(text='Rogue', callback_data='rogue'),
                types.InlineKeyboardButton(text='Priest', callback_data='prist'),
                types.InlineKeyboardButton(text='Shaman', callback_data='shaman'),
                types.InlineKeyboardButton(text='Mage', callback_data='mage'),
                types.InlineKeyboardButton(text='Warlock', callback_data='warlock'),
                types.InlineKeyboardButton(text='Druid', callback_data='druid'),
                types.InlineKeyboardButton(text='Death Knight', callback_data='dk'),
            )

            hero.set_name_hero(message.from_user.text)  #Установка имени персонажа
            bot.send_message(user.get_id_account(), settings.text_on_welcom_step_one_creating_hero(), reply_markup=markup_reply)
            bot.send_message(user.get_id_account(), 'Choice class or write', reply_markup=markup_inline)

        # Если язык пользователем установлен 'русский', то берется русская адаптация
        else:
            # кнопки ру
            ru_classes_warrior = types.KeyboardButton('Воин')
            ru_classes_hunter = types.KeyboardButton('Охотник')
            ru_classes_paladin = types.KeyboardButton('Паладин')
            ru_classes_rogue = types.KeyboardButton('Разбойник')
            ru_classes_priest = types.KeyboardButton('Жрец')
            ru_classes_shaman = types.KeyboardButton('Шаман')
            ru_classes_mage = types.KeyboardButton('Маг')
            ru_classes_warlock = types.KeyboardButton('Чернокнижник')
            ru_classes_druid = types.KeyboardButton('Друид')
            ru_classes_death_knight = types.KeyboardButton('Рыцарь Смерти')

            # создание кнопки и добавление туда кнопок.
            markup_reply.add(
                ru_classes_warrior,
                ru_classes_hunter,
                ru_classes_paladin,
                ru_classes_rogue,
                ru_classes_priest,
                ru_classes_shaman,
                ru_classes_mage,
                ru_classes_warlock,
                ru_classes_druid,
                ru_classes_death_knight,
            )

            markup_inline.add(
                types.InlineKeyboardButton(text='Warrior', callback_data='warrior'),
                types.InlineKeyboardButton(text='Hunter', callback_data='hunter'),
                types.InlineKeyboardButton(text='Paladin', callback_data='paladin'),
                types.InlineKeyboardButton(text='Rogue', callback_data='rogue'),
                types.InlineKeyboardButton(text='Priest', callback_data='prist'),
                types.InlineKeyboardButton(text='Shaman', callback_data='shaman'),
                types.InlineKeyboardButton(text='Mage', callback_data='mage'),
                types.InlineKeyboardButton(text='Warlock', callback_data='warlock'),
                types.InlineKeyboardButton(text='Druid', callback_data='druid'),
                types.InlineKeyboardButton(text='Death Knight', callback_data='dk'),
            )

            hero.set_name_hero(message.from_user.text)  # Установка имени персонажа
            bot.send_message(user.get_id_account(),
                             settings.text_on_welcom_step_one_creating_hero(),
                             reply_markup=markup_reply)

            bot.send_message(user.get_id_account(),
                             'Выберите класс героя или напишите его.',
                             reply_markup=markup_inline)

        bot.send_message(user.get_id_account(), 'text')

    def one_step_creating_hero(self, message):
        bot.send_message(user.get_id_account(), 'text')

        pass
    pass


class Game:
    if Battle().battle:
        pass
    else:
        pass

    pass