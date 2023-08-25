class Stats:
    def __init__(self):
        # Главные статы

        self.main_stats = ''
        self.lvl = 0
        self.xp = 0
        self.str = 0
        self.agi = 0
        self.int = 0
        self.stamina = 0
        self.spirit = 0
        self.hp = 0
        self.mana = 0

        # Второстепенные
        self.ap = 0
        self.spd = 0
        self.damage = 0
        self.defense = 0
        self.dodge = 0
        self.parry = 0
        self.crit_chance = self.agi / 100
        self.crit_damage = self.damage * 2

        # if self.xp >= self.lvl * 200:
        #     self.xp -= self.lvl * 200
        #     self.lvl_up()

    def set_xp(self, xp):
        self.xp += xp

    def get_xp(self):
        return self.xp

    def stats_up(self):

        if self.main_stats == self.str:
            # Главные статы
            self.str += self.lvl + 2
            self.agi += self.lvl + 1
            self.int += self.lvl + 1
            self.stamina += self.lvl + 2
            self.spirit += self.lvl + 1
            self.hp += self.lvl + self.stamina * 2
            self.mana += self.lvl * self.int

            # Второстепенные
            self.ap = (self.str * 2) + (self.agi + 1)
            self.damage = self.ap
            self.defense = (self.str * 1.5) + (self.agi * 2)
            self.dodge = self.agi * 2
            self.parry = self.agi * 1.5


        elif self.main_stats == self.agi:
            # Главные статы
            self.str += self.lvl + 1
            self.agi += self.lvl + 2
            self.int += self.lvl + 1
            self.stamina += self.lvl + 2
            self.spirit += self.lvl + 1
            self.hp += self.lvl + self.stamina * 2
            self.mana += self.lvl * self.int

            # Второстепенные
            self.ap = (self.str + 1) + (self.agi * 2)
            self.damage = self.ap
            self.defense = (self.str * 1.5) + (self.agi * 2)
            self.dodge = self.agi * 2
            self.parry = self.agi * 1.5

        elif self.main_stats == self.int:
            # Главные статы
            self.str += self.lvl + 1
            self.agi += self.lvl + 1
            self.int += self.lvl + 2
            self.stamina += self.lvl + 2
            self.spirit += self.lvl + 1
            self.hp += self.lvl + self.stamina * 2
            self.mana += self.lvl * (self.int * 2)

            # Второстепенные
            self.ap = (self.str + 1) + (self.agi + 1)
            self.spd = self.lvl * (self.int * 2)
            self.damage = self.spd
            self.defense = (self.str * 1.5) + (self.agi * 2)
            self.dodge = self.agi * 2
            self.parry = self.agi * 1.5

        else:
            # Главные статы
            self.str += self.lvl + 2
            self.agi += self.lvl + 1
            self.int += self.lvl + 1
            self.stamina += self.lvl + 2
            self.spirit += self.lvl + 1
            self.hp += self.lvl + self.stamina * 2
            self.mana += self.lvl * self.int

            # Второстепенные
            self.ap = (self.str * 2) + (self.agi + 1)
            self.damage = self.ap
            self.defense = (self.str * 1.5) + (self.agi * 2)
            self.dodge = self.agi * 2
            self.parry = self.agi * 1.5

    def set_str(self, str):
        self.str = str

    def get_str(self):
        return self.str

    def set_agi(self, agi):
        self.agi = agi

    def get_agi(self):
        return self.agi

    def set_int(self, int):
        self.agi = int

    def get_int(self):
        return self.int

    def set_stamina(self, stamina):
        self.stamina = stamina

    def get_stamina(self):
        return self.stamina

    def set_spirit(self, spirit):
        self.spirit = spirit

    def get_spirit(self):
        return self.spirit

    def set_hp(self, hp):
        self.hp += hp

    def get_hp(self):
        return self.hp

    def set_mana(self, mana, use=False):
        if use:
            self.mana -= mana
        else:
            self.mana += mana

    def get_mana(self):
        return self.mana

    def set_ap(self, ap):
        self.ap = ap

    def get_ap(self):
        return self.ap

    def set_spd(self, spd):
        self.spd = spd

    def get_spd(self):
        return self.spd

    def set_damage(self, damage):
        self.damage = damage

    def get_damage(self):
        return self.damage

    def set_defense(self, defense):
        self.defense = defense

    def get_defense(self):
        return self.defense

    def set_dodge(self, dodge):
        self.dodge = dodge

    def get_dodge(self):
        return self.dodge

    def set_parry(self, parry):
        self.parry = parry

    def get_parry(self):
        return self.parry

