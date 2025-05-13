def verify_isbn(isbn: str) -> str:
    """
    Verify the correctness of a given ISBN number and correct it if necessary.

    The function checks the provided ISBN number against the ISBN standard checksum calculation.
    If the checksum is correct, the function returns "Right". If the checksum is incorrect,
    the function returns the corrected ISBN number.

    Args:
    isbn: A string representing the ISBN number to be verified. The format should be 'x-xxx-xxxxx-x',
          where 'x' is a digit, and the last 'x' could also be 'X' representing the checksum digit.

    Returns:
    A string that is either "Right" if the ISBN checksum is correct, or the corrected ISBN number
    in the same format as the input if the checksum is incorrect.

    Examples:
    >>> verify_isbn("0-670-82162-4")
    'Right'
    
    >>> verify_isbn("0-670-82162-0")
    '0-670-82162-4'
    """

    # Check if the ISBN string length is valid.
    if len(isbn) != 14:
        raise ValueError("ISBN must be 14 characters long")

    # Create a list for the characters of the ISBN string.
    isbn_list = list(isbn)

    # If the last character is a letter, it must be 'X'. If not, convert it to an integer.
    if isbn_list[-1].isalpha():
        isbn_list[-1] = 'X'
    else:
        isbn_list[-1] = int(isbn_list[-1])

    # Calculate the checksum.
    checksum = sum(10 - i for i in range(12)) * isbn_list[-1] + sum(i for i in range(1, 13) if i % 2 == 0)

    # If the checksum is correct, return "Right". If not, correct the ISBN number.
    if checksum % 11 == 0:
        isbn_list[-1] = '0'
    else:
        isbn_list[-1] = str(11 - checksum % 11)

    return ''.join(isbn_list)
def test_verify_isbn():
    # Test case 1: Correct ISBN number
    assert verify_isbn("0-670-82162-4") == "Right", "Test case 1 failed"

    # Test case 2: Incorrect ISBN number with wrong checksum digit
    assert verify_isbn("0-670-82162-0") == "0-670-82162-4", "Test case 2 failed"

    print("All test cases passed!")

# Run the test cases
test_verify_isbn()