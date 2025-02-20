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


    def is_multiple(number: int, multiple_of: int) -> bool:
        return number % multiple_of == 0

    def calculate_triples(numbers: list) -> int:
        # count all possible triples
        total_triples = 0
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                for k in range(j + 1, len(numbers)):
                    if is_multiple(numbers[i] + numbers[j] + numbers[k], 3):
                        total_triples += 1
        return total_triples

    a = [i * i - i + 1 for i in range(1, n + 1)]
    return calculate_triples(a)
