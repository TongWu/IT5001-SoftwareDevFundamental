class Radeon(Fighter):
    def __init__(self):
        super().__init__()
        self.name = 'Radeon'
        self.cost = 200
        self.hp = self.maxhp = 900
        self.power = 0

    def gotHurt(self, damage):
        real_damage = damage * 3 // 4
        self.power += damage // 4
        if real_damage >= self.hp:
            self.hp = 0
            self.alive = False
        else:
            self.hp -= real_damage