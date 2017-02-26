class Girls:
    def __init__(self, name, attractiveness, maintenance_budget, intelligence, criterion, type_of_gf=''):
        self.name = name
        self.attractiveness = attractiveness
        self.maintenance_budget = maintenance_budget
        self.intelligence = intelligence

        # For deciding couple happiness
        self.happiness = 0  # initially zero

        # Will be of 3 types : Single, Committed, Broke
        self.status = 'Single'  # initially

        # 3 types : 1.The Choosy 2.The Normal 3.The Desperate
        self.type_of_gf = type_of_gf

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
