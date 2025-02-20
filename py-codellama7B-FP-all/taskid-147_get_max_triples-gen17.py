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


    # 1 <= n <= 1e6
    # 1 <= a[i] <= 1e6

    # (a[i] + a[j] + a[k]) % 3 = 0 => (a[i] + a[j]) % 3 = a[k] % 3
    # a[i] + a[j] 可能是 3 的倍数 也可能不是，所以答案是 (a[i] + a[j]) % 3 = a[k] % 3 中最大的，
    # 可以记录 a[i] + a[j] 的取值分布，然后找到最大的 a[k] % 3 值对应的 a[i] 和 a[j]

    a = [i * i - i + 1 for i in range(1, n + 1)]

    d = {}
    for i in range(1, n):
        d[a[i]] = d.get(a[i], 0) + 1
    print(d)

    max_n = 0
    for k, v in d.items():
        if k % 3 == 0:
            max_n = max(max_n, v * (k // 3))
    return max_n
