class Man:
    def __init__(self, name, surname, sex, growth, weight):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.growth = growth
        self.weight = weight

    def __str__(self):
        return "Man: [name = {}, surname = {}, sex = {}, growth = {}, weight = {}]".format(self.name, self.surname,
                                                                                           self.sex, self.growth,
                                                                                           self.weight)
