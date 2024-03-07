import discord


class Settings:

    def __init__(self):
        self.intents = discord.Intents().all()
        self.prefix = '>'

    def set_prefix(self, prefix):
        self.prefix = prefix

    def get_prefix(self):
        return self.prefix

    def get_intents(self):
        return self.intents

