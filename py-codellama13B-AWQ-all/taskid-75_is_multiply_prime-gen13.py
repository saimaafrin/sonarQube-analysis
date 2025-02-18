def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # The function "is_prime" should be a helper function.
    # It should return "True" if the given number is a prime number
    # and "False" otherwise.
    def is_prime(n: int) -> bool:
        pass

    # The function "is_divisible" should be a helper function.
    # It should return "True" if the given number is divisible by the given divisor.
    # And it should return "False" otherwise.
    # Remember that you can use the modulo operator (%) to check if a number is divisible by another number.
    # The modulo operator will return the remainder of the division of two numbers.
    # If the remainder is 0 then the number is divisible by the divisor.
    def is_divisible(n: int, divisor: int) -> bool:
        pass

    # Write your code here
    if not (a % 3 == 0 and a % 5 == 0):
        return False
    else:
        return is_prime(a // 3) and is_prime(a // 5)
