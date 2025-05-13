def cantor_numbering(N: int) -> str:
    """
    Determines the numerator and denominator of the N-th term in the Cantor table.

    Args:
    - N (int): The position in the Cantor table to find the corresponding fraction for.

    Returns:
    - str: A string representation of the fraction at the N-th position in the Cantor table.
    """

    # The numerator and denominator are determined by the following formula:
    # N_den = sqrt(N + 1) - floor(sqrt(N + 1))
    # N_num = floor((sqrt(N + 1) - floor(sqrt(N + 1))) * 10^(floor(log10(N + 1))))

    # Convert the numerator and denominator to strings using format() function
    N_den = "{:.0f}".format(math.sqrt(N + 1) - math.floor(math.sqrt(N + 1)))
    N_num = "{:.0f}".format(math.floor((math.sqrt(N + 1) - math.floor(math.sqrt(N + 1))) * 10**math.floor(math.log10(N + 1))))

    return "{}/{}".format(N_num, N_den)
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