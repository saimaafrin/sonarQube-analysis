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

    a = [i * i - i + 1 for i in range(1, n + 1)]

    dp = [[0] * len(a) for _ in range(len(a))]

    for i in range(len(a)):
        dp[i][i] = 1

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            dp[i][j] = 1 if a[i] + a[j] in [0, 3] else 0

    for k in range(2, len(a)):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                dp[i][j] += dp[i][k] * dp[k][j]
    return dp[0][len(a) - 1]
