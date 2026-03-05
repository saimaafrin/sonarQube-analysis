import random

class RandomDict(dict):
    def popitem(self):
        if not self:
            raise KeyError('popitem(): dictionary is empty')
        key = random.choice(list(self.keys()))
        return (key, self.pop(key))