class MyClass:
    def __init__(self):
        self.data = {}

    def setdefault(self, key, default=None):
        if key in self.data:
            return self.data[key]
        else:
            self.data[key] = default
            return default