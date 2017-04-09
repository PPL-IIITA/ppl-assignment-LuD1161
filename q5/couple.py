class Couple:
    def __init__(self, girl, boy):
        self.happiness = 0
        self.boy = boy
        self.girl = girl
        self.gifts = []
        self.compatibility_status = 0

    def set_compatibility(self):
        a = self.boy.budget - self.girl.maintenance_budget
        b = abs(self.boy.attractiveness - self.girl.attractiveness)
        c = abs(self.boy.intelligence - self.girl.intelligence)
        self.compatibility_status = a + b + c

    def set_happiness(self):
        self.happiness = self.boy.happiness + self.girl.happiness

