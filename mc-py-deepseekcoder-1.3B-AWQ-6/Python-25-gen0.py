def count_sequences(n: int, last: int, memo: dict) -> int:
    """
    Calculate the number of valid sequences that can be formed according to specific rules.
    
    Each sequence starts with a given number 'n', and a new number can be appended to the sequence
    if it is a positive integer and not greater than half the last number in the sequence. This
    function uses memoization to store previously calculated results to optimize performance.
    
    Args:
        n (int): The starting number of the sequence.
        last (int): The last number in the current sequence.
        memo (dict): A dictionary used for memoization, storing the number of valid sequences
                     for each 'last' value encountered.
    
    Returns:
        int: The total number of valid sequences that can be formed starting with 'n'.
    
    Examples:
        >>> count_sequences(1, 1, {})
        1
        >>> count_sequences(6, 6, {})
        6
    """
    # Base cases: if 'last' is less than 'n', then no sequences can be formed
    if last < n:
        return 0
    
    # if 'last' is equal to 'n' and 'last' is the first sequence of the number 'n',
    # then one valid sequence can be formed
    if last == n and n == 1:
        return 1
    
    # if 'last' is equal to 'n' and 'last' is the first sequence of the number 'n',
    # then one valid sequence can be formed
    if last == n and n == 1:
        return 1

    # If the result is already in the memoization dictionary, return the result
    if last in memo:
        return memo[last]

    # Count the number of valid sequences by adding a new number to the end of an existing
    # sequence. The new number must not exceed half the last number
    count = sum(count_sequences(n, last/2, memo) for last in range(n, last*2+1))

    # Store the result in the memoization dictionary
    memo[last] = count

    return count
def test_count_sequences():
    test_cases = [
        (6, 6),
        (1, 1),
        (10, 14)
    ]

    for i, (n, expected) in enumerate(test_cases):
        memo = {}
        result = count_sequences(n, n, memo)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed: n = {n}, expected = {expected}, got = {result}")

# Call the test function
test_count_sequences()