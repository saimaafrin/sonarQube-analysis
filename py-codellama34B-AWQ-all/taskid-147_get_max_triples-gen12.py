def get_max_triples(n: int) -> int:
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
    >>> get_max_triples(5)
    1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

    if n < 3:
        return 0

    mods = [1, 2]
    for i in range(2, n):
        mods.append((mods[i - 1] + mods[i - 2]) % 3)

    res = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if mods[j - i] == 1:
                continue
            for k in range(j + 1, n):
                if mods[k - j] == mods[j - i]:
                    res += 1

    return res
