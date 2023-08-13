class Settings:
    def __init__(self, language='english'):
        self.language = language

    def get_language(self):
        return self.language

    def text_on_start_game(self):
        if self.language == 'русский':
            return f'Приветствую в ...\nСоздание'
        else:
            return f'Welcom in ...\nCreating'
