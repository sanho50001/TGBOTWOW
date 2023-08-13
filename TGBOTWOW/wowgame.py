import random
import time
import datetime
from game.armor import Armor
from game.weapon import Weapon
from game.settings.settings_game import Settings
from game.battle import Battle
from game.loot import Loot
from game.movement import Movement
from game.potion import Potion
from game.tavern import Tavern
from game.tranquility import Tranquility
from telebot import types


class Bot:
    """Класс Бота для работы с телеграммом"""
    def __init__(self, bot_api):
        self.bot_api = bot_api

    def get_bot_api(self):
        return self.bot_api


bot = Bot('6442732736:AAEgEv-hxyaRxeHkDvMH4Ef_tj7ZC02WqTg')

settings = Settings()


class User:
    def __init__(self, id_account):
        self.id_account = id_account
        pass
    pass


class ClassHero:
    def __init__(self):
        self.warrior = 'Warrior'
        self.hunter = 'Hunter'
        self.paladin = 'Paladin'
        self.rogue = 'Rogue'
        self.priest = 'Priest'
        self.shaman = 'Shaman'
        self.mage = 'Mage'
        self.warlock = 'Warlock'
        self.druid = 'Druid'
        self.death_knight = 'Death Knight'


class StartGame:

    def welcom(self, message):
        bot.bot_api.send_message(message.from_user.id, settings.text_on_start_game())

        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup()
        markup_inline = types.InlineKeyboardMarkup()

        # кнопки
        start_game_button = types.KeyboardButton('/startgame')
        creating_hero_button = types.KeyboardButton('/reghero')

        # создание кнопки и добавление туда кнопок.
        markup_reply.add(creating_hero_button, start_game_button)
        markup_inline.add(
            types.InlineKeyboardButton(text='start game', callback_data='startgame'),
            types.InlineKeyboardButton(text='register hero', callback_data='reghero')
        )


class LeftHand(Weapon):
    def __init__(self):
        super().__init__()
        pass
    pass


class RightHand(Weapon):
    def __init__(self):
        super().__init__()
        pass
    pass


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
        self.armor = Armor()
        self.left_hand = LeftHand()
        self.right_hand = RightHand()
        pass
    pass


class Hero(User):
    """Класс Героя"""
    def __init__(self, name_hero, classes):
        super().__init__(id_account='')
        self.name_hero = name_hero
        self.classes = classes
        self.status = 'Online'
        self.health = 100
        self.armor = Armor()
        self.backpack = Backpack()
        self.left_hand = LeftHand()
        self.right_hand = RightHand()
        pass
    pass


class CreatingHero:
    def __init__(self):
        self.name_hero = ''
        self.classes = []

        pass

    def welcom_step_creating_hero(self, message):
        bot.bot_api.send_message(message.from_user.id, 'text')

    def one_step_creating_hero(self, message):
        bot.bot_api.send_message(message.from_user.id, 'text')

        pass
    pass


class Game:
    pass