import os

def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Complement the full path to exe and return it in its original form
    """
    normalized_cmd = []
    for arg in cmd:
        if os.path.isfile(arg) and os.path.isabs(arg):
            normalized_cmd.append(os.path.basename(arg))
        else:
            normalized_cmd.append(arg)
    return tuple(normalized_cmd)