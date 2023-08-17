class Settings:
    def __init__(self, language='english'):
        self.language = language

    def set_language(self, language):
        self.language = language

    def get_language(self):
        return self.language

    def beggining_settings(self):
        if self.language == 'русский':
            return f'Выберите язык'
        else:
            return f'Choice language'

    def text_on_start_game(self):
        if self.language == 'русский':
            return f'Приветствую в Текстовой ролевой игре по миру RustyForge\nСоздание...'
        else:
            return f'Welcom in Text Roly Game on world RustyForge\nCreating...'


