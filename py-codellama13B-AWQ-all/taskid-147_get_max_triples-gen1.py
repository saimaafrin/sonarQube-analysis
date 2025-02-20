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

    def check(a):
        print(a)
        a_set = set(a)
        ans = 0
        for i in range(1, len(a) + 1):
            for j in range(i + 1, len(a) + 1):
                for k in range(j + 1, len(a) + 1):
                    if a[i] + a[j] + a[k] == 0:
                        ans += 1
        return ans

    def get_next_number(n: int):
        if n % 3 == 0:
            return n // 3
        if n % 3 == 1:
            return n // 3 + 2
        return n // 3 + 1

    if n == 1:
        return 0

    curr_number = n
    res = 0

    while curr_number > 0:
        arr = []
        while curr_number > 0:
            arr.append(curr_number)
            curr_number = get_next_number(curr_number)
        res += check(arr)

    return res
