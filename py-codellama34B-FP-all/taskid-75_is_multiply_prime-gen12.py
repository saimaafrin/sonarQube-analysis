def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # solution 1:
    # prime_list = [2, 3, 5, 7]
    # is_multiply = False
    # for first_prime in prime_list:
    #     for second_prime in prime_list:
    #         for third_prime in prime_list:
    #             if a == first_prime * second_prime * third_prime:
    #                 is_multiply = True
    # if is_multiply:
    #     return True
    # else:
    #     return False

    # solution 2:
    is_multiply = False
    for first_prime in range(2, 10):
        for second_prime in range(first_prime + 1, 10):
            for third_prime in range(second_prime + 1, 10):
                if a == first_prime * second_prime * third_prime:
                    is_multiply = True
    return is_multiply
