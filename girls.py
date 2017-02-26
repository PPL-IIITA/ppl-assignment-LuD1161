class Girls:
    def __init__(self, name, attractiveness, maintenance_budget, intelligence, criterion, status='Single',
                 type_of_gf='', happiness=0):
        self.name = name
        self.attractiveness = attractiveness
        self.maintenance_budget = maintenance_budget
        self.intelligence = intelligence

        # Will be of 3 types : Single, Committed, Broke
        self.status = status

        # For deciding couple happiness
        self.happiness = happiness
        self.type_of_gf = type_of_gf

        # The Deciding criterion --- 1.Most Attractive 2.Most Rich 3.Most Intelligent
        self.criterion = criterion
