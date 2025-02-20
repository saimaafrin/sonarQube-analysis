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


    def is_multiple_of_three(x: int) -> bool:
        return x % 3 == 0

    def get_triples_count(a: list) -> int:
        count = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                for k in range(j + 1, len(a)):
                    if is_multiple_of_three(a[i] + a[j] + a[k]):
                        count += 1
        return count

    def get_numbers(n: int) -> list:
        numbers = []
        for i in range(1, n + 1):
            numbers.append(i * i - i + 1)
        return numbers

    numbers = get_numbers(n)
    return get_triples_count(numbers)
