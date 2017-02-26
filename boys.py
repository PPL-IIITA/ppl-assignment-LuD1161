class Boys:
    def __init__(self, name, attractiveness, intelligence, budget, min_attractiveness_req,
                 status='Single', type_of_bf='', happiness=0):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.budget = budget

        # Minimum attractiveness requirement from a girl
        self.min_attractiveness_req = min_attractiveness_req

        # Will be of 3 types : Single, Committed, Broke
        self.status = status

        # if committed then type of boy
        self.type_of_boyfriend = type_of_bf

        # initially happiness set to zero
        self.happiness = happiness

    def set_budget(self, budget):
        self.budget = budget

    def set_happiness(self, happiness):
        self.happiness = happiness

    def get_budget(self):
        return self.budget
