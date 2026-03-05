def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs:
	"""
	Simplified Implementation of Xargs in Linux
	"""
	if not varargs:
		return cmd
	if len(varargs) == 1:
		return cmd + (varargs[0],)
	if len(varargs) > _max_length:
		raise ValueError(f"Too many arguments: {len(varargs)}")
	if color:
		varargs = [f"{vararg}".replace(" ", "\u00b7") for vararg in varargs]
		cmd = (cmd[0],) + tuple(f"{arg}" for arg in cmd[1:])
		cmd = (
			"echo",
			" ".join(cmd),
			"|",
			"xargs",
			"-n",
			str(len(cmd)),
			"-P",
			str(target_concurrency),
			"-I",
			"{}",
		)
	else:
		cmd = (
			"echo",
			" ".join(cmd),
			"|",
			"xargs",
			"-n",
			str(len(cmd)),
			"-P",
			str(target_concurrency),
			"-I",
			"{}",
		)
	return cmd + tuple(varargs)