from q3 import person


class Girls(person):
    def __init__(self, name, attractiveness, maintenance_budget, intelligence, criterion, type_of=''):
        person.__init__(self, name, attractiveness, intelligence, type_of)

        # self.name = name
        # self.attractiveness = attractiveness
        # self.intelligence = intelligence
        # self.type_of = type_of

        self.maintenance_budget = maintenance_budget

        # For deciding couple happiness
        self.happiness = 0  # initially zero

        # Will be of 3 types : Single, Committed, Broke
        self.status = 'Single'  # initially

        # The Deciding criterion --- 1.Most Attractive 2.Most Rich 3.Most Intelligent
        self.criterion = criterion
        self.bf = ''

    def set_happiness(self, happiness):
        self.happiness = happiness

    def set_status(self, status):
        # Will be of 3 types : Single, Committed, Broke
        self.status = status

    def get_maintenance_budget(self):
        return self.maintenance_budget

    def check_eligibility(self, boys_budget):
        if self.maintenance_budget <= boys_budget:
            return True
        else:
            return False
