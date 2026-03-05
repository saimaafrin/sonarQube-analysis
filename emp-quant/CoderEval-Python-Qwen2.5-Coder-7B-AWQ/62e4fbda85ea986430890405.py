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
    
    for i in range(0, len(varargs), target_concurrency):
        chunk = varargs[i:i + target_concurrency]
        process = subprocess.Popen(cmd + tuple(chunk), **kwargs)
        process.wait()