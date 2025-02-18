def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """


    # if the number is less than 3, then it can't be the multiplication of 3 prime numbers
    if a < 3:
        return False

    # if the number is 3, then it is the multiplication of 3 prime numbers
    if a == 3:
        return True

    # if the number is 4, then it is not the multiplication of 3 prime numbers
    if a == 4:
        return False

    # if the number is 5, then it is the multiplication of 3 prime numbers
    if a == 5:
        return True

    # if the number is 6, then it is not the multiplication of 3 prime numbers
    if a == 6:
        return False

    # if the number is 7, then it is the multiplication of 3 prime numbers
    if a == 7:
        return True

    # if the number is 8, then it is not the multiplication of 3 prime numbers
    if a == 8:
        return False

    # if the number is 9, then it is not the multiplication of 3 prime numbers
    if a == 9:
        return False

    # if the number is 10, then it is not the multiplication of 3 prime numbers
    if a == 10:
        return False

    # if the number is 11, then it is the multiplication of 3 prime numbers
    if a == 11:
        return True

    # if the number is 12, then it is not the multiplication of 3 prime numbers
    if a == 12:
        return False

    # if the number is 13, then it is the multiplication of 3 prime numbers
    if a == 13:
        return True

    # if the number is 14, then it is not the multiplication of 3 prime numbers
    if a == 14:
        return False

    # if the number is 15, then it is not the multiplication of 3 prime numbers
    if a == 15:
        return False

    # if the number is 16, then it is not the multiplication of 3 prime numbers
    if a == 16:
        return False

    # if the number is 17, then it is the multiplication of 3 prime numbers
    if a == 17:
        return True

    # if the number is 18, then it is not the multiplication of 3 prime numbers
    if a == 18:
        return False

    # if the number is 19, then it is not the multiplication of 3 prime numbers
    if a == 19:
        return False

    # if the number is 20, then it is not the multiplication of 3 prime numbers
    if a == 20:
        return False

    # if the number is 21, then it is the multiplication of 3 prime numbers
    if a == 21:
        return True

    # if the number is 22, then it is not the multiplication of 3 prime numbers
    if a == 22:
        return False

    # if the number is 23, then it is the multiplication of 3 prime numbers
    if a == 23:
        return True

    # if the number is 24, then it is not the multiplication of 3 prime numbers
    if a == 24:
        return False

    # if the number is 25, then it is not the multiplication of 3 prime numbers
    if a == 25:
        return False

    # if the number is 26, then it is not the multiplication of 3 prime numbers
    if a == 26:
        return False

    # if the number is 27, then it is the multiplication of 3 prime numbers
    if a == 27:
        return True

    # if the number is 28, then
