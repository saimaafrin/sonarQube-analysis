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
	        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs:
if not varargs:
		return
	if color:
		from .color import color_print
		color_print(f"{cmd[0]} {varargs}", color="green")
	if target_concurrency == 1:
		for arg in varargs:
			subprocess.run(cmd + (arg,), **kwargs)
	else:
		with concurrent.futures.ThreadPoolExecutor(max_workers=target_concurrency) as executor:
			futures = [executor.submit(subprocess.run, cmd + (arg,), **kwargs) for arg in varargs]
			for future in concurrent.futures.as_completed(futures):
				future.result()