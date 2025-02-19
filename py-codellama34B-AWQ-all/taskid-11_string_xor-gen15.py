def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    assert set(a).issubset({'0', '1'}), 'Input strings must contain only 0s and 1s'
    assert set(b).issubset({'0', '1'}), 'Input strings must contain only 0s and 1s'
    max_len = max(len(a), len(b))
    return ''.join('1' if sum(map(int, x)) % 2 else '0' for x in zip(a.zfill(max_len), b.zfill(max_len)))
