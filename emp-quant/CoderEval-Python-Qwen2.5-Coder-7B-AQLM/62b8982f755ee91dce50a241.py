def normalized(self):
    """
    Normalize all units of time to integers.
    """
    self.seconds = int(self.seconds)
    self.minutes = int(self.minutes)
    self.hours = int(self.hours)
    self.days = int(self.days)
    self.weeks = int(self.weeks)
    self.months = int(self.months)
    self.years = int(self.years)