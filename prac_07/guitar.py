class Guitar:
    def __init__(self, name = '', year = 0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            return True
        else:
            return False

    def __str__(self):
        return"{} ({}) : ${:,.2f}".format(self.name, self.cost, self.year)

    def get_age(self):
        return 2017 - self.year

    def is_vintage(self):

        if self.get_age() >= 50:
            return True
        else:
            return False