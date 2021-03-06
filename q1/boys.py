class Boys:
    def __init__(self, name, attractiveness, intelligence, budget, min_attractiveness_req, type_of_bf=''):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.budget = budget

        # Minimum attractiveness requirement from a girl
        self.min_attractiveness_req = min_attractiveness_req

        # Will be of 3 types : Single, Committed, Broke
        self.status = 'Single'  # initially Single

        # Miser, Generous, Geek
        self.type_of_boyfriend = type_of_bf

        # initially happiness set to zero
        self.happiness = 0
        self.gf = ''

    def set_budget(self, budget):
        self.budget = budget

    def set_happiness(self, happiness):
        self.happiness = happiness

    def get_budget(self):
        return self.budget

    def set_status(self, status):
        # Will be of 3 types : Single, Committed, Broke
        self.status = status

    def check_eligibility(self, maintenance_budget, attractiveness):
        if self.budget >= maintenance_budget and \
                        self.min_attractiveness_req >= attractiveness:
            return True
        else:
            return False
