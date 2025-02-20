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

    # Using Sieve of Eratosthenes
    # The logic behind the sieve is that the array a contains 1, 2, 3, 4, 5, ..., n
    # Therefore, if a[i] + a[j] + a[k] is divisible by 3, then i + j + k is divisible by 3
    # as a is a permutation of 1, 2, 3, 4, 5, ..., n
    # So, we need to find the number of triples (i, j, k) such that i + j + k is divisible by 3
    # Now, we need to find the number of triples (i, j, k) such that i + j + k is divisible by 3
    # This is equivalent to finding the number of triples (i, j, k) such that (i + j + k) % 3 == 0
    # The number of triples (i, j, k) such that (i + j + k) % 3 == 0 is equal to the number of triples (i + j, j + k, k + n) % 3 == 0
    # This is because i + j + k = (i + j) + (j + k) + (k + n)
    # Therefore, the number of triples (i, j, k) such that (i + j + k) % 3 == 0 is equal to the number of triples (i + j, j + k, k + n) % 3 == 0
    # Now, we need to find the number of triples (i + j, j + k, k + n) such that (i + j) + (j + k) + (k + n) is divisible by 3
    # We need to find the number of triples (i + j, j + k, k + n) such that (i + j) + (j + k) + (k + n) - (i + j + k) is divisible by 3
    # This is because (i + j) + (j + k) + (k + n) - (i + j + k) is divisible by 3 if and only if (i + j) + (j + k) + (k + n) is divisible by 3
    # Therefore, the number of triples (i, j, k) such that (i + j + k) % 3 == 0 is equal to the number of triples (i + j, j + k, k + n) such that (i + j) + (j + k) + (k + n) - (i + j + k) is divisible by 3
    # Now, we can find the number of triples (i + j, j + k, k + n) such that (i + j) + (j + k) + (k + n) - (i + j + k) is divisible by 3 using Sieve of Eratosthenes
    # The logic behind the sieve is that the array a contains 1, 2, 3, 4, 5, ..., n
    # Therefore, if (i + j) + (j + k) + (k + n) - (i + j + k) is divisible by 3, then (i + j) + (j + k) + (k + n) is divisible by 3
    # as a is a permutation of 1, 2, 3, 4, 5, ..., n
    # So, we need to find the number of triples (i + j
