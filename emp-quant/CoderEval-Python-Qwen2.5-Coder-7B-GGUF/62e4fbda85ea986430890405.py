import subprocess
from typing import Sequence

def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs):
    """
    Simplified Implementation of Xargs in Linux
    """
    if color:
        cmd = ('echo',) + cmd

    args = []
    for arg in varargs:
        if len(' '.join(args + [arg])) + 1 > _max_length:
            subprocess.run(cmd + tuple(args), **kwargs)
            args = []
        args.append(arg)

    if args:
        subprocess.run(cmd + tuple(args), **kwargs)