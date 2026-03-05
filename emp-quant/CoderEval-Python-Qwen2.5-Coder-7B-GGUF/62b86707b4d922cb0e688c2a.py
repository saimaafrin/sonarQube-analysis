def on(self, hook):
    def decorator(func):
        if not hasattr(self, '_registry'):
            self._registry = {}
        if hook not in self._registry:
            self._registry[hook] = []
        self._registry[hook].append(func)
        return func
    return decorator