def on(self, hook):
    """
    Return a decorator function to add a new handler to the "hook" in the registry in the class.
    """
    def decorator(func):
        if not hasattr(self, 'hooks'):
            self.hooks = {}
        if hook not in self.hooks:
            self.hooks[hook] = []
        self.hooks[hook].append(func)
        return func
    return decorator