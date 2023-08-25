# from wowgame import user
# from game.character_stats import stats
# from game.character_stats import Stats


class Hero:
    """Класс Героя"""
    def __init__(self):
        self.id_account = ''
        self.name_hero = ''  # имя персонажа
        self.classes = '' #класс героя
        self.status = 'Online'
        self.health_status = 'Alive'
        self.health_procent = 100
        # self.stats = Stats()
        # self.health = self.stats.hp
        # self.armor = Armor()
        # self.backpack = Backpack()
        # self.left_hand = LeftHand()
        # self.right_hand = RightHand()

    def set_id_account_hero(self, id_account):
        self.id_account = id_account

    def get_id_account_hero(self):
        return self.id_account

    def set_name_hero(self, name_hero):
        self.name_hero = name_hero

    def set_classes_hero(self, classes):
        self.classes = classes

    def get_name_hero(self):
        return self.name_hero

    def get_classes_hero(self):
        return self.classes


# hero = Hero()
