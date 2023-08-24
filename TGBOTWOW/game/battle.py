from wowgame import bot
from game.user import user
from game.settings.settings_game import settings


class Battle:
    """Класс Битва с мобами"""
    def __init__(self):
        self.battle = False

    def set_status_battle(self, status):

        if status:
            self.battle = True
        else:
            self.battle = False

    def get_status_battle(self):
        return self.battle

    def hit(self, hero, npc):
        # Удар героя по нпс
        npc.health -= hero.stats.damage
        bot.send_message(user.get_id_account(),
                         str(settings.text_battle(hero.name_hero, npc.name_npc) + hero.stats.damage))

        # Если здоровье нпс выше 0, то нпс наносит удар по герою
        if npc.health > 0:
            hero.health -= npc.stats.damage
            bot.send_message(user.get_id_account(),
                             str(settings.text_battle(npc.name_hero, hero.name_npc) + npc.stats.damage))

        else:
            pass


battle = Battle()
