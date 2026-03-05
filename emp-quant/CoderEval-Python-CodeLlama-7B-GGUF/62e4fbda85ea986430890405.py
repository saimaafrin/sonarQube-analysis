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
		raise ValueError("cmd cannot be empty")
	if target_concurrency < 1:
		raise ValueError("target_concurrency must be greater than 0")
	if _max_length < 1:
		raise ValueError("_max_length must be greater than 0")
	if len(varargs) > _max_length:
		raise ValueError(f"varargs cannot be greater than {_max_length}")
	if color:
		cmd = ("tput", "setaf", "1") + cmd
		varargs = ("tput", "setaf", "2") + varargs
		kwargs["shell"] = True
		kwargs["stdout"] = subprocess.PIPE
		kwargs["stderr"] = subprocess.PIPE
		kwargs["universal_newlines"] = True
		kwargs["bufsize"] = 1
		kwargs["close_fds"] = True
		kwargs["env"] = os.environ.copy()
		kwargs["env"]["TERM"] = "xterm-256color"
		kwargs["env"]["COLORTERM"] = "truecolor"
		kwargs["env"]["TERM_PROGRAM"] = "xargs"
		kwargs["env"]["TERM_PROGRAM_VERSION"] = "0.1.0"
		kwargs["env"]["TERM_PROGRAM_VERSION_MAJOR"] = "0"
		kwargs["env"]["TERM_PROGRAM_VERSION_MINOR"] = "1"
		kwargs["env"]["TERM_PROGRAM_VERSION_PATCH"] = "0"
		kwargs["env"]["TERM_PROGRAM_AUTHOR"] = "xargs"
		kwargs["env"]["TERM_PROGRAM_AUTHOR_VERSION"] = "0.1.0"
		kwargs["env"]["TERM_PROGRAM_AUTHOR_VERSION_MAJOR"] = "0"
		kwargs["env"]["TERM_PROGRAM_AUTHOR_VERSION_MINOR"]