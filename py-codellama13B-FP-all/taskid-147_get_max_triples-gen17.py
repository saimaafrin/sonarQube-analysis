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

    max_triples = 0
    for i in range(1, n):
        j = i + 1
        k = i + 2
        while j < n and k < n:
            if (a[i] + a[j] + a[k]) % 3 == 0:
                max_triples += 1
            if j < k:
                j += 1
            else:
                k += 1

    return max_triples
