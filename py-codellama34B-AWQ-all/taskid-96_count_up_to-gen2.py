from typing import List

def count_up_to(n: int) -> List[int]:
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    >>> count_up_to(5)
    [2, 3]
    >>> count_up_to(11)
    [2, 3, 5, 7]
    >>> count_up_to(0)
    []
    >>> count_up_to(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> count_up_to(1)
    []
    >>> count_up_to(18)
    [2, 3, 5, 7, 11, 13, 17]
    """

    # if n == 0:
    #     return []
    # if n == 1:
    #     return []
    # if n == 2:
    #     return [2]
    # if n == 3:
    #     return [2, 3]

    # numbers: List[int] = [2]
    # current_number: int = 3

    # while len(numbers) < n:
    #     is_prime: bool = True
    #     for number in numbers:
    #         if current_number % number == 0:
    #             is_prime = False
    #             break
    #     if is_prime:
    #         numbers.append(current_number)
    #     current_number += 1
    # return numbers
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, num)):
            primes.append(num)
    return primes
