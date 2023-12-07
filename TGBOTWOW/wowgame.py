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
# from main import bot
from dotenv import load_dotenv
import os
from telebot import types
import telebot


load_dotenv()
bot = telebot.TeleBot(os.getenv('telebot_token'))
# user = User()


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


hero = Heroes()


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

battle = Battles()


class Movemented:
    def __init__(self):
        self.movement = Movement()

    def move(self):
        x = database.Zone(self.movement.get_coord_x(), self.movement.get_coord_y())
        if x == None:
            bot.send_message(user.get_id_account(), 'Вы ничего не нашли')


movement = Movemented()


class BeginningStart:

    def r2(self):

        bot.send_message(user.get_id_account(), '<span style="color:blue">foo</span>')


    def beginning_settings(self, message):

        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_inline = types.InlineKeyboardMarkup()

        # кнопки
        rus_language_button = types.KeyboardButton('Русский 🇷🇺')
        english_language_button = types.KeyboardButton('English 🇺🇸')

        # создание кнопки и добавление туда кнопок.
        markup_reply.row(rus_language_button, english_language_button)

        # Кнопки с выбором
        markup_inline.add(
            types.InlineKeyboardButton(text='Русский язык 🇷🇺', callback_data='ru'),
            types.InlineKeyboardButton(text='English language 🇺🇸', callback_data='eng'),
        )
        bot.send_message(user.get_id_account(), settings.text_games(), reply_markup=markup_reply)
        bot.send_message(user.get_id_account(), settings.text_commands(), reply_markup=markup_inline)


class StartGame:

    def welcom(self, message):
        # Добавляем пользователя в базу данных
        database.Create_User(id_account=message.from_user.id)
        user.set_id_account(id_account=message.from_user.id)

        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup()
        markup_inline = types.InlineKeyboardMarkup()

        # кнопки
        start_game_button = types.KeyboardButton('/startgame')
        creating_hero_button = types.KeyboardButton('/reghero')
        settings_button = types.KeyboardButton('/settings')

        # создание кнопки и добавление туда кнопок.
        markup_reply.add(creating_hero_button, start_game_button, settings_button)
        markup_inline.add(
            types.InlineKeyboardButton(text=settings.text_menu_button_game_start_game(), callback_data='startgame'),
            types.InlineKeyboardButton(text=settings.text_menu_button_game_register_hero(), callback_data='reghero'),
            types.InlineKeyboardButton(text=settings.text_menu_button_game_settings(), callback_data='settings'),
        )

        bot.send_message(chat_id=user.get_id_account(), text=settings.text_on_start_game(), reply_markup=markup_reply)
        bot.send_message(user.get_id_account(), settings.text_commands(), reply_markup=markup_inline)

    def choice_hero_step_one(self):
        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup()
        markup_inline = types.InlineKeyboardMarkup()

        # кнопки
        start_game_button = types.KeyboardButton('/list_hero')

        # создание кнопки и добавление туда кнопок.
        markup_reply.add(start_game_button, )
        markup_inline.add(
            types.InlineKeyboardButton(text=settings.text_list_hero_button(), callback_data='list_hero'),
        )
        bot.send_message(user.get_id_account(), settings.text_games(), reply_markup=markup_reply)
        bot.send_message(user.get_id_account(), settings.text_commands(), reply_markup=markup_inline)

    def choice_hero_step_two(self):
        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup()
        markup_inline = types.InlineKeyboardMarkup()

        text = {}
        for numm, dicted in database.get_hero_list():
            if settings.get_language() == 'english':

                for row in dicted:
                    oper = int(numm) + 1
                    if not f'{oper} Hero' in text:
                        text[f'{oper} Hero'] = f'{dicted[row]} '
                    else:
                        text[f'{oper} Hero'] += f'{dicted[row]} '
            else:
                for row in dicted:
                    text[f'{int(numm) + 1} Герой'] = f'{dicted[row]} '

        print(text)
        for hero in text.values():
            markup_reply.add(types.KeyboardButton(hero),)
            markup_inline.add(types.InlineKeyboardButton(text=f'{hero}', callback_data=f'{hero}',),
                              )
            if settings.get_language() == 'english':

                bot.send_message(user.get_id_account(), 'list', reply_markup=markup_reply)
                bot.send_message(user.get_id_account(), 'choice', reply_markup=markup_inline)
            else:
                bot.send_message(user.get_id_account(), 'Список', reply_markup=markup_reply)
                bot.send_message(user.get_id_account(), 'Выберите', reply_markup=markup_inline)

    def choice_hero_step_three(self, name_hero):
        heroes = database.get_hero(name_hero=name_hero)

        hero.hero.set_classes_hero(heroes.get('class'))
        hero.hero.set_name_hero(heroes.get('name hero'))
        hero.hero.set_id_account_hero(heroes.get('id account'))
        hero.stats.set_lvl(heroes.get('lvl'))


        pass
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

    def welcom_step_one_creating_hero(self, message):
        # print(message)
        hero.hero.set_name_hero(message.text)  #Установка имени персонажа
        user.set_id_account(id_account=message.from_user.id)

        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup()
        markup_inline = types.InlineKeyboardMarkup()

        # кнопки классов репли( отдельная менюшка справа (на телефонах выпадающая панелька) )
        classes_warrior = types.KeyboardButton(settings.text_on_class_warrior())
        classes_hunter = types.KeyboardButton(settings.text_on_class_hunter())
        classes_paladin = types.KeyboardButton(settings.text_on_class_paladin())
        classes_rogue = types.KeyboardButton(settings.text_on_class_rogue())
        classes_priest = types.KeyboardButton(settings.text_on_class_priest())
        classes_shaman = types.KeyboardButton(settings.text_on_class_shaman())
        classes_mage = types.KeyboardButton(settings.text_on_class_mage())
        classes_warlock = types.KeyboardButton(settings.text_on_class_warlock())
        classes_druid = types.KeyboardButton(settings.text_on_class_druid())
        classes_death_knight = types.KeyboardButton(settings.text_on_class_death_knight())

        # Кнопки инлайн(под сообщением выпадающие) классов
        markup_inline.add(
            types.InlineKeyboardButton(text=settings.text_on_class_warrior(), callback_data='warrior'),
            types.InlineKeyboardButton(text=settings.text_on_class_hunter(), callback_data='hunter'),
            types.InlineKeyboardButton(text=settings.text_on_class_paladin(), callback_data='paladin'),
            types.InlineKeyboardButton(text=settings.text_on_class_rogue(), callback_data='rogue'),
            types.InlineKeyboardButton(text=settings.text_on_class_priest(), callback_data='priest'),
            types.InlineKeyboardButton(text=settings.text_on_class_shaman(), callback_data='shaman'),
            types.InlineKeyboardButton(text=settings.text_on_class_mage(), callback_data='mage'),
            types.InlineKeyboardButton(text=settings.text_on_class_warlock(), callback_data='warlock'),
            types.InlineKeyboardButton(text=settings.text_on_class_druid(), callback_data='druid'),
            types.InlineKeyboardButton(text=settings.text_on_class_death_knight(), callback_data='dk'),
        )
        # Кнопки репли( отдельная менюшка справа (на телефонах выпадающая панелька) )
        markup_reply.add(
            classes_warrior,
            classes_hunter,
            classes_paladin,
            classes_rogue,
            classes_priest,
            classes_shaman,
            classes_mage,
            classes_warlock,
            classes_druid,
            classes_death_knight,
        )

        # Отправка сообщения и кнопок репли
        bot.send_message(user.get_id_account(),
                         settings.text_on_welcom_step_one_creating_hero(),
                         reply_markup=markup_reply)

        # Отправка сообщения и кнопок инлайн
        bot.send_message(user.get_id_account(),
                         settings.text_commands(),
                         reply_markup=markup_inline)
        # Функция необходимая для сообщений в чате (если пользователь захотел сам ввести)
        bot.register_next_step_handler(message, self.two_step_creating_hero)

    def two_step_creating_hero(self, message):
        """Третий этап создания персонажа."""
        # print()
        # hero.hero.set_classes_hero(message.text)    #Задаем класс персонажа
        bot.send_message(user.get_id_account(),
                         settings.text_on_welcom_step_two_creating_hero())

        # создание героя в базе данных
        database.Create_Hero(
            name_hero=hero.hero.get_name_hero(),
            classes=hero.hero.get_classes_hero(),
            id_account=user.get_id_account()
        )

    #     bot.register_next_step_handler(message, self.three_step_creating_hero)
    # def three_step_creating_hero(self, message):
    #     bot.send_message(user.get_id_account(), settings.)

class Game:
    """Класс игры"""
    # Инициализация кнопок для дальнейших действий
    markup_reply = types.ReplyKeyboardMarkup()
    markup_inline = types.InlineKeyboardMarkup()

    # Функция игры.
    def game(self):
        """Функция игры.
        Условия: Если сейчас идет битва, то происходит фаза битвы, иначе фаза ходьбы
        """
        # Если статус битвы == True, то происходит фаза боя, иначе фаза ходьбы
        if battle.battle.get_status_battle():
            # Кнопки
            button_hit = types.KeyboardButton(settings.text_on_button_game_battle_hit())
            button_spell = types.KeyboardButton(settings.text_on_button_game_battle_spell())
            button_block = types.KeyboardButton(settings.text_on_button_game_battle_block())
            button_backpack = types.KeyboardButton(settings.text_on_button_game_battle_backpack())

            # создание кнопки и добавление туда кнопок.
            self.markup_reply.add(
                button_hit,
                button_spell,
                button_block,
                button_backpack,
            )

            # отправка сообщения и команд пользователю
            bot.send_message(user.get_id_account(),
                             settings.text_games(),
                             reply_markup=self.markup_reply)

            bot.send_message(user.get_id_account(),
                             settings.text_commands(),
                             reply_markup=self.markup_inline)

        # Если фаза битвы == False, происходит фаза ходьбы
        else:
            # Кнопки
            button_up = types.KeyboardButton(settings.text_on_button_game_non_battle_up())
            button_down = types.KeyboardButton(settings.text_on_button_game_non_battle_down())
            button_left = types.KeyboardButton(settings.text_on_button_game_non_battle_left())
            button_right = types.KeyboardButton(settings.text_on_button_game_non_battle_right())

            # создание кнопки и добавление туда кнопок.
            self.markup_reply.add(
                button_up,
                button_down,
                button_left,
                button_right,
            )

            self.markup_inline.add(
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_up(), callback_data='Up'),
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_down(), callback_data='Down'),
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_left(), callback_data='Left'),
                types.InlineKeyboardButton(text=settings.text_on_button_game_non_battle_right(), callback_data='Right'),
            )

            # отправка сообщения и команд пользователю
            bot.send_message(user.get_id_account(),
                             settings.text_games(),
                             reply_markup=self.markup_reply)

            bot.send_message(user.get_id_account(),
                             settings.text_commands(),
                             reply_markup=self.markup_inline)


# Инициализация данных
creatinghero = CreatingHero()
startgame = StartGame()
bigstart = BeginningStart()
settings_on_db.set_settings(settings)
