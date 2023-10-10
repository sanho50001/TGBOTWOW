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
from game.db_commands import database
from game.hero import Hero
from game.user import user
from game.character_stats import Stats
from game.npc import npc
from game.zone import zone
# from main import bot
from telebot import types
import telebot

bot = telebot.TeleBot('5824374073:AAEfAlM2tCZzknjkol1_NKyPnzfaMYI31BE')
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
        bot.send_message(user.get_id_account(), settings.text_games(), reply_markup=markup_reply)
        bot.send_message(user.get_id_account(), 'Commands', reply_markup=markup_inline)


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

        # Если язык пользователем установлен 'english', то берется английская адаптация
        if settings.get_language() == 'english':
            markup_inline.add(
                types.InlineKeyboardButton(text='start game', callback_data='startgame'),
                types.InlineKeyboardButton(text='register hero', callback_data='reghero'),
                types.InlineKeyboardButton(text='settings', callback_data='settings'),
            )

            bot.send_message(chat_id=user.get_id_account(), text=settings.text_on_start_game(), reply_markup=markup_reply)
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

    def choice_hero_step_one(self):

        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup()
        markup_inline = types.InlineKeyboardMarkup()

        # кнопки
        start_game_button = types.KeyboardButton('/list_hero')

        # создание кнопки и добавление туда кнопок.
        if settings.get_language() == 'english':
            markup_reply.add(start_game_button, )
            markup_inline.add(
                types.InlineKeyboardButton(text='List Heroes', callback_data='list_hero'),
            )
            bot.send_message(user.get_id_account(), settings.text_games(), reply_markup=markup_reply)
            bot.send_message(user.get_id_account(), 'Commands', reply_markup=markup_inline)
        else:
            markup_reply.add(start_game_button, )
            markup_inline.add(
                types.InlineKeyboardButton(text='Список персонажей', callback_data='list_hero'),
            )
            bot.send_message(user.get_id_account(), settings.text_games(), reply_markup=markup_reply)
            bot.send_message(user.get_id_account(), 'Комманды', reply_markup=markup_inline)

    def choice_hero_step_two(self):

        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup()
        markup_inline = types.InlineKeyboardMarkup()

        text = ''
        for numm, dicted in database.get_hero_list():
            if settings.get_language() == 'english':

                text += f'{int(numm) + 1} Hero: \n'
                for row in dicted:
                    text += (f'{row}:{dicted[row]} ')
            else:

                text += f'{int(numm) + 1} Герой: \n'
                for row in dicted:
                    text += (f'{row}:{dicted[row]} ')

        markup_reply.add(types.KeyboardButton(text),)
        markup_inline.add(types.InlineKeyboardButton(text=f'{text[0:7]}', callback_data=f'{text[0:7]}',),
                          )
        if settings.get_language() == 'english':

            bot.send_message(user.get_id_account(), 'list', reply_markup=markup_reply)
            bot.send_message(user.get_id_account(), 'choice', reply_markup=markup_inline)
        else:
            bot.send_message(user.get_id_account(), 'Список', reply_markup=markup_reply)
            bot.send_message(user.get_id_account(), 'Выберите', reply_markup=markup_inline)
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
                types.InlineKeyboardButton(text='Priest', callback_data='priest'),
                types.InlineKeyboardButton(text='Shaman', callback_data='shaman'),
                types.InlineKeyboardButton(text='Mage', callback_data='mage'),
                types.InlineKeyboardButton(text='Warlock', callback_data='warlock'),
                types.InlineKeyboardButton(text='Druid', callback_data='druid'),
                types.InlineKeyboardButton(text='Death Knight', callback_data='dk'),
            )

            bot.send_message(user.get_id_account(),
                             settings.text_on_welcom_step_one_creating_hero(),
                             reply_markup=markup_reply)

            bot.send_message(user.get_id_account(),
                             'Choice class or write',
                             reply_markup=markup_inline)

            bot.register_next_step_handler(message, self.two_step_creating_hero)
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
                types.InlineKeyboardButton(text='Priest', callback_data='priest'),
                types.InlineKeyboardButton(text='Shaman', callback_data='shaman'),
                types.InlineKeyboardButton(text='Mage', callback_data='mage'),
                types.InlineKeyboardButton(text='Warlock', callback_data='warlock'),
                types.InlineKeyboardButton(text='Druid', callback_data='druid'),
                types.InlineKeyboardButton(text='Death Knight', callback_data='dk'),
            )

            bot.send_message(user.get_id_account(),
                             settings.text_on_welcom_step_one_creating_hero(),
                             reply_markup=markup_reply)

            bot.send_message(user.get_id_account(),
                             'Выберите класс героя или напишите его.',
                             reply_markup=markup_inline)

            bot.register_next_step_handler(message, self.two_step_creating_hero)

    def two_step_creating_hero(self, message):
        # hero.hero.set_classes_hero(message.text)    #Задаем класс персонажа
        bot.send_message(user.get_id_account(),
                         settings.text_on_welcom_step_two_creating_hero())

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
    markup_reply = types.ReplyKeyboardMarkup()
    markup_inline = types.InlineKeyboardMarkup()

    def game(self):
        if battle.battle.get_status_battle():
            if settings.get_language() == 'english':
                # кнопки eng
                eng_button_hit = types.KeyboardButton('hit')
                eng_button_spell = types.KeyboardButton('spell')
                eng_button_block = types.KeyboardButton('block')
                eng_button_backpack = types.KeyboardButton('backpack')

                # создание кнопки и добавление туда кнопок.
                self.markup_reply.add(
                    eng_button_hit,
                    eng_button_spell,
                    eng_button_block,
                    eng_button_backpack,
                )

                self.markup_inline.add(
                    types.InlineKeyboardButton(text='hit', callback_data='hit'),
                    types.InlineKeyboardButton(text='spell', callback_data='spell'),
                    types.InlineKeyboardButton(text='block', callback_data='block'),
                    types.InlineKeyboardButton(text='backpack', callback_data='backpack'),
                )

                bot.send_message(user.get_id_account(),
                                 settings.text_games(),
                                 reply_markup=self.markup_reply)

                bot.send_message(user.get_id_account(),
                                 'Choice action or write',
                                 reply_markup=self.markup_inline)
            else:
                # кнопки ru
                ru_button_hit = types.KeyboardButton('Удар')
                ru_button_spell = types.KeyboardButton('Способности')
                ru_button_block = types.KeyboardButton('Защита')
                ru_button_backpack = types.KeyboardButton('Сумка')

                # создание кнопки и добавление туда кнопок.
                self.markup_reply.add(
                    ru_button_hit,
                    ru_button_spell,
                    ru_button_block,
                    ru_button_backpack,
                )

                self.markup_inline.add(
                    types.InlineKeyboardButton(text='hit', callback_data='hit'),
                    types.InlineKeyboardButton(text='spell', callback_data='spell'),
                    types.InlineKeyboardButton(text='block', callback_data='block'),
                    types.InlineKeyboardButton(text='backpack', callback_data='backpack'),
                )

                bot.send_message(user.get_id_account(),
                                 settings.text_games(),
                                 reply_markup=self.markup_reply)

                bot.send_message(user.get_id_account(),
                                 'Выберите действие или напишите',
                                 reply_markup=self.markup_inline)
        else:
            if settings.get_language() == 'english':
                # кнопки eng
                eng_button_Up = types.KeyboardButton('Up')
                eng_button_Down = types.KeyboardButton('Down')
                eng_button_Left = types.KeyboardButton('Left')
                eng_button_Right = types.KeyboardButton('Right')

                # создание кнопки и добавление туда кнопок.
                self.markup_reply.add(
                    eng_button_Up,
                    eng_button_Down,
                    eng_button_Left,
                    eng_button_Right,
                )

                self.markup_inline.add(
                    types.InlineKeyboardButton(text='Up', callback_data='Up'),
                    types.InlineKeyboardButton(text='Down', callback_data='Down'),
                    types.InlineKeyboardButton(text='Left', callback_data='Left'),
                    types.InlineKeyboardButton(text='Right', callback_data='Right'),
                )

                bot.send_message(user.get_id_account(),
                                 settings.text_games(),
                                 reply_markup=self.markup_reply)

                bot.send_message(user.get_id_account(),
                                 'Choice action or write',
                                 reply_markup=self.markup_inline)
            else:
                # кнопки ru
                ru_button_Up = types.KeyboardButton('Вверх')
                ru_button_Down = types.KeyboardButton('Вниз')
                ru_button_Left = types.KeyboardButton('Влево')
                ru_button_Right = types.KeyboardButton('Вправо')

                # создание кнопки и добавление туда кнопок.
                self.markup_reply.add(
                    ru_button_Up,
                    ru_button_Down,
                    ru_button_Left,
                    ru_button_Right,
                )

                self.markup_inline.add(
                    types.InlineKeyboardButton(text='Вверх', callback_data='Up'),
                    types.InlineKeyboardButton(text='Вниз', callback_data='Down'),
                    types.InlineKeyboardButton(text='Влево', callback_data='Left'),
                    types.InlineKeyboardButton(text='Вправо', callback_data='Right'),
                )

                bot.send_message(user.get_id_account(),
                                 settings.text_games(),
                                 reply_markup=self.markup_reply)

                bot.send_message(user.get_id_account(),
                                 'Выберите действие или напишите',
                                 reply_markup=self.markup_inline)


creatinghero = CreatingHero()
startgame = StartGame()
bigstart = BeginningStart()
