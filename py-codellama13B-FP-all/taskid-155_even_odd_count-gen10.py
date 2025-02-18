from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    # 1. Initialize a counter for even and odd digits
    count_even = 0
    count_odd = 0
    
    # 2. Loop through all digits in the number
    while num > 0:
        
        # 3. If the current digit is even, increment count_even
        if num % 10 % 2 == 0:
            count_even += 1
        
        # 4. If the current digit is odd, increment count_odd
        else:
            count_odd += 1
        
        # 5. Divide the number by 10 to move to the next digit
        num //= 10
    
    # 6. Return a tuple with count_even and count_odd
    return count_even, count_odd
