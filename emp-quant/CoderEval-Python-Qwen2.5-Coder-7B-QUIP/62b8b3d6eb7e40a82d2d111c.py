def _normalizeargs(sequence, output=None):
    """
    Normalize declaration arguments

    Normalization arguments might contain Declarations, tuples, or single
    interfaces.

    Anything but individual interfaces or implements specs will be expanded.
    """
    if isinstance(sequence, tuple):
        return tuple(_normalizeargs(item) for item in sequence)
    elif isinstance(sequence, list):
        return [_normalizeargs(item) for item in sequence]
    elif isinstance(sequence, dict):
        return {key: _normalizeargs(value) for key, value in sequence.items()}
    else:
        return sequence