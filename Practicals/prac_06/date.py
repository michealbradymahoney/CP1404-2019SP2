class Date:

    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    def add_days(self, n):
        self.date += n

    def __str__(self):
        return "{}/{}/{}".format(self.date, self.month, self.year)