class D:
    def __init__(self):
        self.data = {}
    
    def pop(self, key, default=None):
        if key in self.data:
            return self.data.pop(key)
        elif default is not None:
            return default
        else:
            raise KeyError(f"Key '{key}' not found")