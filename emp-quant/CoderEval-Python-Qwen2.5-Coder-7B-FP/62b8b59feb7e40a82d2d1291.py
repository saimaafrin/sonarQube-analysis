def _getTargetClass(self):
# Default implementation
	return self.__class__.__name__.replace('Py', '').replace('Fallback', '')[:-1] if self.__class__.__name__[-1].isdigit() else self.__class__.__name__.replace('Py', '').replace('Fallback', '')