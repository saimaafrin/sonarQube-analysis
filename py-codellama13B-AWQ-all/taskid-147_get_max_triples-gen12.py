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

    max_triples = 0
    modulo_3 = 0
    i = 1

    while i < n:
        modulo_3 = (i * i - i + 1) % 3
        if modulo_3 == 1:
            j = i + 1
            while j < n:
                modulo_3 = (j * j - j + 1) % 3
                if modulo_3 == 1:
                    k = j + 1
                    while k < n:
                        if (i * i - i + 1) + (j * j - j + 1) + (k * k - k + 1) % 3 == 0:
                            max_triples += 1
                        k += 1
                j += 1
        i += 1
    return max_triples
