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

    def text_on_start_game(self):
        if self.get_language() == 'русский':
            return f'Приветствую в Текстовой ролевой игре по миру RustyForge\nСоздание...'
        else:
            return f'Welcom in Text Roly Game on world RustyForge\nCreating...'

    def text_on_welcom_step_one_creating_hero(self):
        if self.get_language() == 'русский':
            return 'Классы:\n'\
                   'Воин\n'\
                   'Охотник\n'\
                   'Паладин\n'\
                   'Разбойник\n'\
                   'Жрец\n'\
                   'Шаман\n'\
                   'Маг\n'\
                   'Чернокнижник\n'\
                   'Друид\n'\
                   'Рыцарь Смерти'
        else:
            return 'Classes:\n' \
                   'Warrior\n' \
                   'Hunter\n'\
                   'Paladin\n'\
                   'Rogue\n'\
                   'Priest\n'\
                   'Shaman\n'\
                   'Mage\n'\
                   'Warlock\n'\
                   'Druid\n'\
                   'Death Knight'

    def text_on_welcom_step_two_creating_hero(self):
        if self.get_language() == 'русский':
            return f'Поздравляем, Ваш герой создан!'
        else:
            return f'Congratulations, your hero has been created!'

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
            return f'Выберите действие'
        else:
            return f'Choice action'

    def text_choice_hero(self):
        if self.get_language() == 'русский':
            return f'Выберите действие'
        else:
            return f'Choice action'

# Инициализация настроек
settings = Settings()

