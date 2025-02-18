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


    # for a[i] = i * i - i + 1
    # (a[i], a[j], a[k]) = (i, j, k)
    # so we can say that i + j + k is always a multiple of 3
    # and we can get a[i] + a[j] + a[k] = i * i - i + 1 + j * j - j + 1 + k * k - k + 1 = 3(i+j+k)
    # so we want to get the number of triples that can be formed 
    # with elements of a, such that a[i] + a[j] + a[k] = 3*3 = 9

    # we can do this by taking the square root of 9 to get 3,
    # and then we can iterate through each element, 
    # and see if a[i] + a[j] + a[k] is a multiple of 9
    # and if it is then we increment our count by one

    # the answer will be our count

    count = 0

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if (i * i - i + 1) + (j * j - j + 1) + (k * k - k + 1) % 9 == 0:
                    count += 1

    return count
