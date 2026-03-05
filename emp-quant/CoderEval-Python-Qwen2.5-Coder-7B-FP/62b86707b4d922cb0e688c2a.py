def on(self, hook):
# Get the current class
	current_class = self.__class__
	
	def decorator(func):
		# Add the handler to the hook in the registry of the class
		if not hasattr(current_class, '_registry'):
			setattr(current_class, '_registry', {})
		if hook not in current_class._registry:
			current_class._registry[hook] = []
		current_class._registry[hook].append(func)
		
		return func
	
	return decorator