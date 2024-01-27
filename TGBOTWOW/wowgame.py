import random
import time
import datetime
from game.armor import Armor
from game.weapon import Weapon
from game.settings.settings_game import settings
from game.battle import Battle
from game.loot import Loot
from game.movement import Movement
from game.potion import Potion
from game.tavern import Tavern
from game.tranquility import Tranquility
from game.db_commands import database, settings_on_db
from game.hero import Hero
from game.user import user
from game.character_stats import Stats
from game.npc import npc
from game.zone import zone
import game.creatinghero as creathero
# from main import bot
from dotenv import load_dotenv
import os
from telebot import types
import telebot

load_dotenv()
bot = telebot.TeleBot(os.getenv('telebot_token'))


class Heroes:
    def __init__(self):
        self.hero = Hero()
        self.stats = Stats()
        self.health = self.stats.hp

        if self.health or self.hero.health_procent <= 0:
            self.hero.health_status = 'Dead'

        if self.stats.xp >= self.stats.lvl * 200:
            self.stats.xp -= self.stats.lvl * 200
            self.lvl_up()

    def lvl_up(self):
        if self.hero.get_classes_hero() == 'Warrior' or 'Paladin' or 'Death Knight':
            self.stats.main_stats = self.stats.str

        elif self.hero.get_classes_hero() == 'Hunter' or 'Rogue' or 'Druid':
            self.stats.main_stats = self.stats.agi

        elif self.hero.get_classes_hero() == 'Priest' or 'Shaman' or 'Mage' or 'Warlock':
            self.stats.main_stats = self.stats.int

        self.stats.lvl += 1
        self.stats.stats_up()

    def get_health_hero(self):
        return f'Здоровье героя ❤️ {self.health}'

    def get_stats_hero(self):
        if self.stats.energy >= 1:
            return f'Здоровье героя  ❤️ {self.health}\n' \
                   f'Энергия героя ⚡ {self.stats.get_energy()}'
        else:
            return f'Здоровье героя  ❤️ {self.health}\n' \
                   f'Мана героя 💧 {self.stats.get_mana()}' \


class NPC:
    def __init__(self):
        self.npc = npc
        self.stats = Stats()

        self.health = self.stats.hp

        if self.health or self.npc.health_procent <= 0:
            self.npc.status = 'Dead'


class Battles:
    def __init__(self):
        self.battle = Battle()

    def hit(self, hero, npc, spell=None):
        # Удар героя по нпс
        npc.health -= hero.stats.damage
        bot.send_message(user.get_id_account(),
                         str(settings.text_battle(hero.name_hero, npc.name_npc) + hero.stats.damage + '💥'))

        # Если здоровье нпс выше 0, то нпс наносит удар по герою
        if npc.health > 0:
            hero.health -= npc.stats.damage
            bot.send_message(user.get_id_account(),
                             str(settings.text_battle(npc.name_hero, hero.name_npc) + npc.stats.damage + '💥'))

        # else:
        #     pass


class Movemented:

    def __init__(self):
        self.movement = Movement()

    def move(self, message):
        if game.get_game_status() == None:
            game.set_game_status(status='start game')
        if game.get_location() == None:
            game.set_location(location='Dalaran')
        print(game.get_game_status(), game.get_location())
        print('115')
        location = database.location(location=game.get_location())

        zone = database.Zone(coording_x=self.movement.get_coord_x(),
                             coording_y=self.movement.get_coord_y(),
                             location=location)

        if zone:
            bot.send_message(user.get_id_account(), settings.text_on_game_where_is_location_hero() + f'{zone}')
            bot.register_next_step_handler(message, game.game)
        else:
            bot.delete_message(chat_id=user.get_id_account(), message_id=settings.get_last_message_id())
            markup_inline = types.InlineKeyboardMarkup()
            markup_inline.add(
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_left(), callback_data='Left'),
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_up(), callback_data='Up'),
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_down(), callback_data='Down'),
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_right(), callback_data='Right'),
            )
            messages = bot.send_message(user.get_id_account(), settings.text_movement_none_find(), reply_markup=markup_inline)
            settings.set_last_message_id(message_id=messages.message_id)
            # bot.delete_message(chat_id=user.get_id_account(), message_id=settings.get_last_message_id())
            print(zone)





class SettingsGame:
    """Класс настроек"""

    def beginning_settings(self):
        # вызов метода создания кнопки
        markup_inline = types.InlineKeyboardMarkup()
        # Кнопки с выбором
        markup_inline.add(
            types.InlineKeyboardButton(text='Русский язык 🇷🇺', callback_data='ru'),
            types.InlineKeyboardButton(text='English language 🇺🇸', callback_data='eng'),
        )
        bot.edit_message_text(chat_id=user.get_id_account(), message_id=settings.get_last_message_id(),
                              text=settings.text_commands(), reply_markup=markup_inline)
        # bot.send_message(user.get_id_account(), settings.text_commands(), reply_markup=markup_inline)

    def set_language(self):
        markup_inline = types.InlineKeyboardMarkup()
        hide_keyboard = types.ReplyKeyboardRemove()
        markup_inline.add(hide_keyboard)
        time.sleep(0.5)
        messages = bot.edit_message_text(chat_id=user.get_id_account(), message_id=settings.get_last_message_id(),
                                         text=settings.text_on_language_set(), reply_markup=None)
        time.sleep(1)
        bot.delete_message(chat_id=user.get_id_account(), message_id=messages.message_id)
        startgame.welcom()


class StartGame:
    """Старт игры"""
    def __init__(self):
        self.call_func = 0

    def welcom(self):
        """Стартовая страница приветствия"""
        # Добавляем пользователя в базу данных
        database.Create_User(id_account=user.get_id_account())

        # вызов метода создания кнопки
        markup_inline = types.InlineKeyboardMarkup()

        # создание кнопки и добавление туда кнопок.
        markup_inline.add(
            types.InlineKeyboardButton(text=settings.text_menu_button_game_start_game(), callback_data='startgame'),
            types.InlineKeyboardButton(text=settings.text_menu_button_game_register_hero(), callback_data='reghero'),
            types.InlineKeyboardButton(text=settings.text_menu_button_game_settings(), callback_data='settings'),
        )

        if self.call_func <= 0:
            bot.send_message(user.get_id_account(), settings.text_commands(), reply_markup=markup_inline)
            self.call_func += 1
        else:
            bot.edit_message_text(chat_id=user.get_id_account(), message_id=settings.get_last_message_id(),
                                  text=settings.text_commands(), reply_markup=markup_inline)


    def choice_hero_step_one(self, message):
        """Фаза выбора персонажа 1/3"""

        # вызов метода создания кнопки
        markup_inline = types.InlineKeyboardMarkup()

        # создание кнопки и добавление туда кнопок.
        markup_inline.add(
            types.InlineKeyboardButton(text=settings.text_list_hero_button(), callback_data='list_hero'),
        )
        bot.edit_message_text(chat_id=user.get_id_account(), message_id=settings.get_last_message_id(),
                              text=settings.text_commands(), reply_markup=markup_inline)


    def choice_hero_step_two(self):
        """Фаза выбора персонажа 2/3"""
        # вызов метода создания кнопки
        markup_inline = types.InlineKeyboardMarkup()

        text = {}

        # Взятие из базы данных всех персонажей аккаунта
        for numm, dicted in database.get_hero_list():

            name_hero = dicted[settings.text_on_db_name_hero()]
            class_hero = dicted[settings.text_on_db_classes_hero()]
            lvl_hero = dicted[settings.text_on_db_lvl_hero()]

            oper = int(numm) + 1
            if not f'{oper} {settings.text_on_func_choice_hero_step_two_hero()}, {name_hero}' in text:
                text[f'{oper} {settings.text_on_func_choice_hero_step_two_hero()}, {name_hero}'] \
                    = f'{name_hero}, {class_hero}, {lvl_hero}'
            else:
                text[f'{oper} {settings.text_on_func_choice_hero_step_two_hero()}, {name_hero}'] \
                    += f'{name_hero}, {class_hero}, {lvl_hero}'

        # Добавление персонажей в выбор через кнопку
        for hero in text:
            markup_inline.add(types.InlineKeyboardButton(text=f'{text[hero]}', callback_data=f'{hero}', ),)

        messages = bot.edit_message_text(chat_id=user.get_id_account(), message_id=settings.get_last_message_id(),
                                         text=settings.text_choice_action(), reply_markup=markup_inline)
        settings.set_last_message_id(message_id=messages.message_id)

    def choice_hero_step_three(self, name_hero, message):
        """Последняя функция выбора персонажа. 3/3"""
        # Происходит взятие данных персонажа в БД
        heroes = database.get_hero(name_hero=name_hero)
        # Установка значений персонажа после взятия его из БД
        hero.hero.set_classes_hero(heroes.get('class'))
        hero.hero.set_name_hero(heroes.get('name hero'))
        hero.hero.set_id_account_hero(heroes.get('id account'))
        hero.stats.set_lvl(heroes.get('lvl'))
        bot.delete_message(chat_id=user.get_id_account(), message_id=settings.get_last_message_id())
        # Старт игры, переход к функциям игры
        game.game(message=message)

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


class CreatingHero:
    """Класс инициализации создания персонажа"""
    def __init__(self):
        """Инициализация данных"""
        creat_hero.set_bot(bot=bot)
        creat_hero.set_settings(settings=settings)
        creat_hero.set_hero(hero=hero)
        creat_hero.set_types(types=types)
        creat_hero.set_user(user=user)
        creat_hero.set_time(time=time)
        creat_hero.set_startgame(startgame=startgame)
        creat_hero.set_database(database=database)

    def creatinghero_step_one_creating_hero(self, message=None):
        """Первый этап создания персонажа"""
        creat_hero.step_one_creating_hero(message=message)

    def creatinghero_two_step_creating_hero(self, message=None):
        """Второй этап создания персонажа"""
        creat_hero.two_step_creating_hero()


class Game:
    """Класс игры"""

    def __init__(self):
        self.game_status = None
        self.location = None

    def set_game_status(self, status):
        self.game_status = status

    def get_game_status(self):
        return self.game_status

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    # Функция игры.
    def game(self, message):
        # Инициализация кнопок для дальнейших действий
        markup_inline = types.InlineKeyboardMarkup()
        """Функция игры.
        Условия: Если сейчас идет битва, то происходит фаза битвы, иначе фаза ходьбы
        """
        # Если статус битвы == True, то происходит фаза боя, иначе фаза ходьбы
        if battle.battle.get_status_battle():
            # отправка сообщения и команд пользователю
            bot.send_message(user.get_id_account(),
                             settings.text_commands(),
                             reply_markup=markup_inline)

        # Если фаза битвы == False, происходит фаза ходьбы
        else:
            if self.game_status:
                movement.move(message=message)
            elif self.game_status == 'start game':
                pass
            else:
                self.set_game_status(status='start game')
            # создание кнопки и добавление туда кнопок.
            markup_inline.add(
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_left(), callback_data='Left'),
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_up(), callback_data='Up'),
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_down(), callback_data='Down'),
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_right(), callback_data='Right'),
            )
            # отправка сообщения и команд пользователю
            messages = bot.send_message(user.get_id_account(),
                                        settings.text_commands(),
                                        reply_markup=markup_inline)
            settings.set_last_message_id(message_id=messages.message_id)


# Инициализация данных
# step1
startgame = StartGame()
# step2
settings_game = SettingsGame()
# step3
game = Game()
# step4
movement = Movemented()
# step5
battle = Battles()
# step6
hero = Heroes()
# step7
settings_on_db.set_settings(settings)
# step8
creat_hero = creathero.CreatingHero()
# step9
creatinghero = CreatingHero()
