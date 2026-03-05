def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if not cmd[0]:
		return cmd
	if os.path.isabs(cmd[0]):
		return cmd
	return (os.path.join(os.environ['PATH'], cmd[0]),) + cmd[1:]