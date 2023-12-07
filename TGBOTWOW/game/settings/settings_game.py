class Settings:
    def __init__(self, language='english'):
        self.language = language

    def set_language(self, language):
        self.language = language

    def get_language(self):
        return self.language

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

    # def text_

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

    # def text_choice_hero(self):
    #     if self.get_language() == 'русский':
    #         return f'Выберите действие'
    #     else:
    #         return f'Choice action'

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



# Инициализация настроек
settings = Settings()

