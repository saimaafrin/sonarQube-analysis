def _normalizeargs(sequence, output=None):
    """
    Normalize declaration arguments

    Normalization arguments might contain Declarations, tuples, or single
    interfaces.

    Anything but individual interfaces or implements specs will be expanded.
    """
    if output is None:
        output = []

    for item in sequence:
        if isinstance(item, tuple):
            output.extend(_normalizeargs(item))
        elif isinstance(item, list):
            output.extend(_normalizeargs(item))
        else:
            output.append(item)

    return output