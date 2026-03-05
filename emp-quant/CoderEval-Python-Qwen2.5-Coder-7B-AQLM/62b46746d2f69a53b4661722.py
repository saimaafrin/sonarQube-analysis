def absorb(self, args):
    """
    Given an `args` sequence of expressions, return a new list of expression applying absorption.
    """
    new_args = []
    for arg in args:
        if isinstance(arg, list):
            new_args.extend(arg)
        else:
            new_args.append(arg)
    return new_args