import random

class RandomDict(dict):
    def popitem(self):
        if not self:
            raise KeyError("popitem(): dictionary is empty")
        key = random.choice(list(self.keys()))
        value = self[key]
        del self[key]
        return (key, value)