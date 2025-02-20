def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # return (a == (2 * 3 * 5))

    # a = 30
    # list_prime_nums = []
    # for i in range(2, 10):
    #     if a % i == 0:
    #         list_prime_nums.append(i)
    #         list_prime_nums.append(a / i)
    #         list_prime_nums.sort()
    #         if list_prime_nums[0] * list_prime_nums[1] * list_prime_nums[2] == a:
    #             return True
    #         else:
    #             return False

    # a = 30
    # list_prime_nums = []
    # for i in range(2, 10):
    #     if a % i == 0:
    #         list_prime_nums.append(i)
    #         list_prime_nums.append(a / i)
    #         list_prime_nums.sort()
    #         if list_prime_nums[0] * list_prime_nums[1] * list_prime_nums[2] == a:
    #             return True
    #         else:
    #             return False

    # a = 30
    # for i in range(2, 10):
    #     if a % i == 0:
    #         list_prime_nums = [i, a / i]
    #         list_prime_nums.sort()
    #         if list_prime_nums[0] * list_prime_nums[1] * list_prime_nums[2] == a:
    #             return True
    #         else:
    #             return False
