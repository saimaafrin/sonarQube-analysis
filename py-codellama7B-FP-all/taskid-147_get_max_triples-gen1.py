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


    # Find the first number that is not a multiple of 3
    first_non_multiple = 3
    while first_non_multiple % 3 == 0:
        first_non_multiple += 1

    # First we need to find all the multiples of 3
    multiples_of_3 = [first_non_multiple]
    for i in range(first_non_multiple + 1, n):
        if i % 3 == 0:
            multiples_of_3.append(i)

    # Now for each number in multiples_of_3 we check if there are any numbers in multiples_of_3 that are
    # a[i] + a[j] = x, and a[k] = 3 * x + 1
    total = 0
    for i in range(len(multiples_of_3)):
        for j in range(i + 1, len(multiples_of_3)):
            x = multiples_of_3[i] + multiples_of_3[j]
            for k in range(len(multiples_of_3)):
                if multiples_of_3[k] == 3 * x + 1:
                    total += 1
    return total
