import os

def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Complement the full path to exe and return it in its original form
    """
    normalized_cmd = []
    for arg in cmd:
        if os.path.isfile(arg):
            normalized_cmd.append(os.path.abspath(arg))
        else:
            normalized_cmd.append(arg)
    return tuple(normalized_cmd)