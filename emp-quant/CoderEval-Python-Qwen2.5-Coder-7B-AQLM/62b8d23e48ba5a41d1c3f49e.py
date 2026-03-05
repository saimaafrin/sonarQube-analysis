import random

def popitem(self):
    """
    Find, remove and return a random `(key, value)` pair via __choice in the class
    """
    if not self:
        raise KeyError("popitem from an empty dictionary")
    key = random.choice(list(self.keys()))
    value = self[key]
    del self[key]
    return key, value