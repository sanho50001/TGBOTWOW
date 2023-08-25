
class NPC:
    """Класс НПС"""
    def __init__(self, name_npc='Zombie'):
        self.name_npc = name_npc
        self.status = 'Alive'
        self.loot = {}
        self.health_procent = 100

        # self.armor = Armor()
        # self.left_hand = LeftHand()
        # self.right_hand = RightHand()


npc = NPC()
