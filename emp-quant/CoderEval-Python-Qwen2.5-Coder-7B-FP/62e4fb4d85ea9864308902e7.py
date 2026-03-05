def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
# Remove any leading or trailing whitespace from each element in the command tuple
	cmd = tuple(element.strip() for element in cmd)
	return cmd