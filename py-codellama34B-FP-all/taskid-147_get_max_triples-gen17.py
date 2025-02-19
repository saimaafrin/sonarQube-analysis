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

    ans = 0
    mod = 10**9 + 7
    a = [0] * (n+1)
    for i in range(1, n+1):
        a[i] = i*i - i + 1
    
    for i in range(1, n):
        for j in range(i+1, n):
            k = (a[i] + a[j]) % 3
            if k == 0:
                ans += j - i
            elif k == 1:
                ans += j - i - 1
    
    return ans % mod
