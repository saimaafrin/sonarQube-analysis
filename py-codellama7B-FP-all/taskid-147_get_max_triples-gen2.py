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

    i_max = n // 3
    i_max = i_max if i_max * 3 >= n else i_max - 1
    # i_max = i_max - 1 if i_max * 3 < n else i_max
    cnt = 0
    for i in range(i_max + 1):
        for j in range(i + 1, i_max + 1):
            for k in range(j + 1, i_max + 1):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    cnt += 1
    return cnt
