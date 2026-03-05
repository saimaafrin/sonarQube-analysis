def cantor_numbering(N: int) -> str:
    """
    Determines the numerator and denominator of the N-th term in the Cantor table.

    Args:
    - N (int): The position in the Cantor table to find the corresponding fraction for.

    Returns:
    - str: A string representation of the fraction at the N-th position in the Cantor table.
    """


    # Initialize variables
    numerator = 1
    denominator = 1
    level = 1

    # Iterate through the levels of the Cantor table
    while N > 0:
        # If N is in the left half of the level, move to the next level
        if N <= level:
            N -= level
            level *= 2
        else:
            # If N is in the right half of the level, move to the next level and subtract the level
            N -= level
            level *= 2
            N += level

    # Adjust the numerator and denominator based on the level
    if level % 2 == 0:
        numerator = N
        denominator = level - N + 1
    else:
        numerator = level - N + 1
        denominator = N

    return f"{numerator}/{denominator}"
def test_cantor_numbering():
    # Test case 1: N = 1, the first element, should be "1/1"
    assert cantor_numbering(1)=="1/1"

    # Test case 2: N = 2, the second element, should be "1/2"
    assert cantor_numbering(2)=="1/2"

    # Test case 3: N = 6, the sixth element, should be "1/3"
    assert cantor_numbering(6)=="1/3"

    # Corrected test case: N = 7, the seventh element, should be "1/4"
    assert cantor_numbering(7) == "1/4"

    # Additional test case: N = 8, the eighth element, should be "2/3"
    assert cantor_numbering(8) == "2/3"


test_cantor_numbering()