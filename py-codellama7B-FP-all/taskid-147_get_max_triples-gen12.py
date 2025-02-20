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


    # a = [i**2 - i + 1 for i in range(1, n+1)]

    # return sum(i for i in range(n) if a[i+1] - a[i] == 3)

    # return sum(j for j in range(n) if a[j+1] - a[j] == 3 and a[j+2] - a[j+1] == 3)

    # return sum(k for k in range(n-1) if a[k+1] - a[k] == 3 and a[k+2] - a[k+1] == 3 and a[k+3] - a[k+2] == 3)


    # return sum(j for j in range(n) if a[j+1] - a[j] == 3 and a[j+2] - a[j+1] == 3 and a[j+3] - a[j+2] == 3)

    # return sum(i for i in range(n) if a[i+1] - a[i] == 3 and a[i+2] - a[i+1] == 3 and a[i+3] - a[i+2] == 3)


    # return sum(i for i in range(n) if a[i+1] - a[i] == 3 and a[i+2] - a[i+1] == 3 and a[i+3] - a[i+2] == 3 and a[i+4] - a[i+3] == 3)


    return sum(i for i in range(n) if a[i+1] - a[i] == 3 and a[i+2] - a[i+1] == 3 and a[i+3] - a[i+2] == 3 and a[i+4] - a[i+3] == 3 and a[i+5] - a[i+4] == 3)
