class Settings:
    def __init__(self, language='english'):
        self.language = language
        self.message_id = None

    def set_language(self, language):
        self.language = language

    def get_language(self):
        return self.language

    def set_last_message_id(self, message_id):
        self.message_id = message_id

    def get_last_message_id(self,):
        return self.message_id

    def beggining_settings(self):
        if self.get_language() == 'русский':
            return f'Выберите язык'
        else:
            return f'Choice language'

    def text_on_language_set(self):
        if self.get_language() == 'русский':
            return f'✅ Ваши языковые настройки были успешно изменены. Приятной игры!'
        else:
            return f'✅ Your language settings have been successfully changed. Have a nice game!'

    def text_on_start_game(self):
        if self.get_language() == 'русский':
            return f'Приветствую в Текстовой ролевой игре по миру RustyForge'
        else:
            return f'Welcom in Text Roly Game on world RustyForge'

    def text_menu_button_game_start_game(self):
        if self.get_language() == 'русский':
            return f'старт игры ➡️'
        else:
            return f'start game ➡️'

    def text_menu_button_game_register_hero(self):
        if self.get_language() == 'русский':
            return f'Зарегистрировать героя 📜 '
        else:
            return f'Register hero 📜'

    def text_menu_button_game_set_name_hero(self):
        if self.get_language() == 'русский':
            return f'Введите имя персонажа'
        else:
            return f'Enter the name of the character'

    def text_menu_button_choice_class_hero(self):
        if self.get_language() == 'русский':
            return f'Выберите ️класс героя'
        else:
            return f'Choice class hero️'

    def text_menu_button_game_settings(self):
        if self.get_language() == 'русский':
            return f'Настройки ⚙️'
        else:
            return f'Settings ⚙️'

    def text_list_hero_button(self):
        if self.get_language() == 'русский':
            return f'Список персонажей 🧾'
        else:
            return f'List Heroes 🧾'

    def text_choice_action(self):
        if self.get_language() == 'русский':
            return f'Выберите'
        else:
            return f'Choice'

    def text_on_func_choice_hero_step_two_hero(self):
        if self.get_language() == 'русский':
            return f'Герой'
        else:
            return f'Hero'

    def text_on_welcom_step_one_creating_hero(self):
        return f'{self.text_on_class_classes()}:\n'\
               f'{self.text_on_class_warrior()}\n'\
               f'{self.text_on_class_hunter()}\n'\
               f'{self.text_on_class_paladin()}\n'\
               f'{self.text_on_class_rogue()}\n'\
               f'{self.text_on_class_priest()}\n'\
               f'{self.text_on_class_shaman()}\n'\
               f'{self.text_on_class_mage()}\n'\
               f'{self.text_on_class_warlock()}\n'\
               f'{self.text_on_class_druid()}\n'\
               f'{self.text_on_class_death_knight()}'

    def text_on_welcom_step_two_creating_hero(self):
        if self.get_language() == 'русский':
            return f'Поздравляем, Ваш герой создан!'
        else:
            return f'Congratulations, your hero has been created!'

    def text_on_class_classes(self):
        if self.get_language() == 'русский':
            return f'Классы 👑'
        else:
            return f'Classes 👑'

    def text_on_class_warrior(self):
        if self.get_language() == 'русский':
            return f'Воин 📕'
        else:
            return f'Warrior 📕'

    def text_on_class_hunter(self):
        if self.get_language() == 'русский':
            return f'Охотник 📗'
        else:
            return f'Hunter 📗'

    def text_on_class_paladin(self):
        if self.get_language() == 'русский':
            return f'Паладин 📕'
        else:
            return f'Paladin 📕'

    def text_on_class_rogue(self):
        if self.get_language() == 'русский':
            return f'Разбойник 📗'
        else:
            return f'Rogue 📗'

    def text_on_class_priest(self):
        if self.get_language() == 'русский':
            return f'Жрец 📘'
        else:
            return f'Priest 📘'

    def text_on_class_shaman(self):
        if self.get_language() == 'русский':
            return f'Шаман 📘'
        else:
            return f'Shaman 📘'

    def text_on_class_mage(self):
        if self.get_language() == 'русский':
            return f'Маг 📘'
        else:
            return f'Mage 📘'

    def text_on_class_warlock(self):
        if self.get_language() == 'русский':
            return f'Чернокнижник 📘'
        else:
            return f'Warlock 📘'

    def text_on_class_druid(self):
        if self.get_language() == 'русский':
            return f'Друид 📗'
        else:
            return f'Druid 📗'

    def text_on_class_death_knight(self):
        if self.get_language() == 'русский':
            return f'Рыцарь Смерти 📕'
        else:
            return f'Death Knight 📕'

    def text_lvl_up(self):
        if self.get_language() == 'русский':
            return f'Поздравляем, Вы повысили уровень!'
        else:
            return f'Congratulations, you have raised the level!'

    def text_battle(self, target1, target2):
        if self.get_language() == 'русский':
            return f'{target1} ударил по {target2} и нанес: '
        else:
            return f'{target1} hit {target2} and strike: '

    def text_games(self):
        if self.get_language() == 'русский':
            return f'Выберите действие или напишите'
        else:
            return f'Choice action or write'

    def text_movement_none_find(self):
        if self.get_language() == 'русский':
            return f'Вы ничего не нашли'
        else:
            return f"You didn't find anything"

    def text_commands(self):
        if self.get_language() == 'русский':
            return f'Команды ⚙️'
        else:
            return f'Commands ⚙️'

    def text_on_button_game_battle_hit(self):
        if self.get_language() == 'русский':
            return f'Удар 💥'
        else:
            return f'Hit 💥'

    def text_on_button_game_battle_spell(self):
        if self.get_language() == 'русский':
            return f'Способности ⚡'
        else:
            return f'Spell ⚡'

    def text_on_button_game_battle_block(self):
        if self.get_language() == 'русский':
            return f'Защита 🛡️'
        else:
            return f'Block 🛡️'

    def text_on_button_game_battle_backpack(self):
        if self.get_language() == 'русский':
            return f'Сумка 🎒'
        else:
            return f'Backpack 🎒'

    def text_on_button_game_non_battle_up(self):
        if self.get_language() == 'русский':
            return f'Вверх 🔼'
        else:
            return f'Up 🔼'

    def text_on_button_game_non_battle_down(self):
        if self.get_language() == 'русский':
            return f'Вниз 🔽'
        else:
            return f'Down 🔽'

    def text_on_button_game_non_battle_left(self):
        if self.get_language() == 'русский':
            return f'Влево ⬅️'
        else:
            return f'Left ⬅️'

    def text_on_button_game_non_battle_right(self):
        if self.get_language() == 'русский':
            return f'Вправо ➡️'
        else:
            return f'Right ➡️'

    def text_on_db_name_hero(self):
        if self.get_language() == 'русский':
            return f'имя персонажа'
        else:
            return f'name hero️'

    def text_on_db_classes_hero(self):
        if self.get_language() == 'русский':
            return f'класс героя'
        else:
            return f'classes hero'

    def text_on_db_lvl_hero(self):
        if self.get_language() == 'русский':
            return f'уровень'
        else:
            return f'lvl'


# Инициализация настроек
settings = Settings()

