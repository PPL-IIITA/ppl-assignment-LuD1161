from q3 import person


class Boys(person):
    def __init__(self, name, attractiveness, intelligence, budget, min_attractiveness_req, type_of=''):
        person.__init__(self, name, attractiveness, intelligence, type_of)

        self.budget = budget

        # Minimum attractiveness requirement from a girl
        self.min_attractiveness_req = min_attractiveness_req

        # Will be of 3 types : Single, Committed, Broke
        self.status = 'Single'  # initially Single

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
