import random

class MyClass:
    def __init__(self, items):
        self.items = items

    def popitem(self):
        """
        Find, remove and return a random `(key, value)` pair via __choice in the class
        """
        if not self.items:
            raise KeyError("popitem from an empty dictionary")
        key, value = random.choice(list(self.items.items()))
        del self.items[key]
        return key, value