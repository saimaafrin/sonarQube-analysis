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


    # 1. Find the smallest multiple of 3 greater or equal to n
    n = (n//3 + 1)*3

    # 2. Find the largest multiple of 3 lesser or equal to n
    n = n - n%3

    # 3. Subtract 1 from both n's and the result would be 
    # the number of triples
    n -= 1

    return n
