def pretty(self, indent=0, debug=False):
indent_str = " " * indent
	if debug:
		debug_details = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
	else:
		debug_details = ""
	obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj)
	return f"{indent_str}{self.__class__.__name__}({debug_details}, {obj})"