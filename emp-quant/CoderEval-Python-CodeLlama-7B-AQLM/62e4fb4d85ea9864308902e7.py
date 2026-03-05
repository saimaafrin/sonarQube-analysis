def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if not cmd[0].endswith(".exe"):
		cmd = (cmd[0] + ".exe", *cmd[1:])
	return cmd