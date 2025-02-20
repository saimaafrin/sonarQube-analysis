def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a <= 1 or a >= 100:
        return False
    else:
        list_of_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        temp = a
        for i in list_of_prime:
            if temp % i == 0:
                temp /= i
        return temp == 1
