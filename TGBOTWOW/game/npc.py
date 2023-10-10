
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

    def set_name_npc(self, name_npc):
        self.name_npc = name_npc

    def get_name_npc(self):
        return self.name_npc


npc = NPC()
