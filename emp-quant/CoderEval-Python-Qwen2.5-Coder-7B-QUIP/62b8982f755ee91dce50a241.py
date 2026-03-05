def normalized(self):
    """
    Normalize all units of time to integers.
    """
    # Assuming self is a time-related object with attributes like hours, minutes, and seconds
    self.hours = int(self.hours)
    self.minutes = int(self.minutes)
    self.seconds = int(self.seconds)