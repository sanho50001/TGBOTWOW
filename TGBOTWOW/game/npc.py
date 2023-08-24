from game.character_stats import stats


class NPC:
    """Класс НПС"""
    def __init__(self, name_npc='Zombie'):
        self.name_npc = name_npc
        self.status = 'Alive'
        self.loot = {}
        self.stats = stats
        self.health_procent = 100
        self.health = self.stats.hp

        if self.health or self.health_procent <= 0:
            self.status = 'Dead'


        # self.armor = Armor()
        # self.left_hand = LeftHand()
        # self.right_hand = RightHand()


npc = NPC()
