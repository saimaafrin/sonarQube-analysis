def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    i = 2
    while i < a:
        if a % i == 0:
            if is_prime(i):
                j = i + i
                while j < a:
                    if a % j == 0:
                        if is_prime(j):
                            k = j + j
                            while k < a:
                                if a % k == 0:
                                    return True
                                k += 1
                            return False
                        else:
                            break
                    j += 1
                return False
            else:
                break
        i += 1
    return False
