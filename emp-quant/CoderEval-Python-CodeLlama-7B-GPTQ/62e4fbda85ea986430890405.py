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
		return
	if not cmd:
		raise ValueError("cmd must be a non-empty tuple")
	if target_concurrency < 1:
		raise ValueError("target_concurrency must be a positive integer")
	if _max_length < 1:
		raise ValueError("_max_length must be a positive integer")
	if color:
		cmd = ("tput", "setaf") + cmd
		kwargs["_color"] = True
		kwargs["_color_cmd"] = cmd
		kwargs["_color_varargs"] = varargs
		kwargs["_color_target_concurrency"] = target_concurrency
		kwargs["_color_max_length"] = _max_length
		kwargs["_color_kwargs"] = kwargs
		return
	if target_concurrency > 1:
		cmd = ("xargs", "-n", str(target_concurrency), "-P", str(target_concurrency), *cmd)
		kwargs["_target_concurrency"] = target_concurrency
		kwargs["_max_length"] = _max_length
		kwargs["_kwargs"] = kwargs
		return
	if len(varargs) > _max_length:
		varargs = varargs[:_max_length]
	cmd = (*cmd, *varargs)
	kwargs["_cmd"] = cmd
	kwargs["_kwargs"] = kwargs