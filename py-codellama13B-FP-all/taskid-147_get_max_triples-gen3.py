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

    count = 0
    arr = []
    for i in range(1, n + 1):
        arr.append(i ** 2 - i + 1)
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                    count += 1
    return count
