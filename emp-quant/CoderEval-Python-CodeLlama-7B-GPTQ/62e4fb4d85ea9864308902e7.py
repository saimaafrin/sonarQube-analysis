def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if cmd[0].startswith("/"):
		return cmd
	else:
		return (which(cmd[0]), *cmd[1:])