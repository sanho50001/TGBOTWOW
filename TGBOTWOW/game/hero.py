from wowgame import user
from game.character_stats import stats


class Hero(user):
    """Класс Героя"""
    def __init__(self):
        super().__init__()
        self.name_hero = ''  # имя персонажа
        self.classes = '' #класс героя
        self.status = 'Online'
        self.health_status = 'Alive'
        self.health_procent = 100
        self.stats = stats
        self.health = self.stats.hp
        # self.armor = Armor()
        # self.backpack = Backpack()
        # self.left_hand = LeftHand()
        # self.right_hand = RightHand()

        if self.health or self.health_procent <= 0:
            self.health_status = 'Dead'

    def set_name_hero(self, name_hero):
        self.name_hero = name_hero

    def set_classes_hero(self, classes):
        self.classes = classes

    def get_name_hero(self):
        return self.name_hero

    def get_classes_hero(self):
        return self.classes

    def get_health_hero(self):
        return self.health


hero = Hero()
