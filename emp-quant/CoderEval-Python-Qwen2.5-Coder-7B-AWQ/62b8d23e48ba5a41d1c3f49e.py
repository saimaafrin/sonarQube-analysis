import random

class RandomDict(dict):
    def popitem(self):
        if not self:
            raise KeyError("popitem from empty dictionary")
        key = random.choice(list(self.keys()))
        value = self.pop(key)
        return (key, value)