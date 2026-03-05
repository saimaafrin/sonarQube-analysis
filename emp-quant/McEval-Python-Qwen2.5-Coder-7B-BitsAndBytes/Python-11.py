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
    direction = 1  # 1 for ascending, -1 for descending
    diagonal = 1  # The diagonal number in the Cantor table

    # Loop until we reach the N-th term
    while N > 0:
        # Calculate the number of terms in the current diagonal
        diagonal_terms = diagonal + 1

        # If N is within the current diagonal
        if N <= diagonal_terms:
            # If the diagonal is even, the numerator starts from 1 and increases
            if diagonal % 2 == 0:
                numerator = 1
                denominator = diagonal - N + 1
            # If the diagonal is odd, the denominator starts from 1 and increases
            else:
                numerator = diagonal - N + 1
                denominator = 1
            break

        # If N is not within the current diagonal, move to the next diagonal
        N -= diagonal_terms
        diagonal += 1

    # Return the fraction as a string
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