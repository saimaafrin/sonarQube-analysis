import inspect

def _normalizeargs(sequence, output=None):
    if output is None:
        output = []

    for item in sequence:
        if isinstance(item, tuple):
            output.extend(_normalizeargs(item))
        elif inspect.isclass(item) and issubclass(item, (Declarion, Interface)):
            output.append(item)
        else:
            raise ValueError(f"Invalid argument: {item}")

    return output