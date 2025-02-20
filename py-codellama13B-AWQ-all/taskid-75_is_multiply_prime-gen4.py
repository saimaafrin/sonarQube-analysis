def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # first of all, if it's not the multiplication of 3 prime numbers
    # it will have 1 or 2 numbers
    if len(str(a)) == 1 or len(str(a)) == 2:
        return False
    
    # check if it's not the multiplication of 3 numbers
    # i.e. 12 = 2 * 2 * 3  but not 2 * 3 * 2
    if len(str(a)) % 2 == 0:
        return False
    
    # split the number to two parts: 
    # 1. the part of the number which is less than the number
    # 2. the part of the number which is more than the number
    part1 = int(str(a)[:len(str(a))//2])
    part2 = int(str(a)[len(str(a))//2:])
    
    # check if both of the parts are prime numbers
    if part1 > 1 and part2 > 1:
        for i in range(2, part1):
            if part1 % i == 0:
                return False
        
        for i in range(2, part2):
            if part2 % i == 0:
                return False
        
    return True
