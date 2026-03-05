import random

class RandomDict(dict):
    def popitem(self):
        """
        Find, remove and return a random `(key, value)` pair via __choice in the class
        """
        if not self:
            raise KeyError("popitem(): dictionary is empty")
        key, value = random.choice(list(self.items()))
        del self[key]
        return key, value