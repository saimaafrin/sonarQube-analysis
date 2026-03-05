from collections import deque
def generate_numbers(n, rules) -> int:
    """
    Generate all unique numbers from the given number by applying transformation rules.

    Each rule allows a single digit to be transformed into another. A breadth-first search
    (BFS) is used to explore all possible transformations. The function returns the count
    of unique numbers that can be generated from the original number, including the number itself.

    Args:
    - n (int): The original integer number to transform.
    - rules (list of tuples): A list of transformation rules, where each rule is represented
                              as a tuple (x, y) indicating that digit x can be transformed into y.

    Returns:
    - int: The total count of unique numbers that can be generated.

    Cases:
    >>> generate_numbers(234, [(2, 5), (3, 6)])
    4
    >>> generate_numbers(100, [(1, 9)])
    2
    """
    # Initialize the queue with the original number
    queue = deque([n])
    # Initialize the count of unique numbers
    count = 1
    # Loop while the queue is not empty
    while queue:
        # Pop the first number from the queue
        number = queue.popleft()
        # Loop through all transformation rules
        for rule in rules:
            # Get the digit that can be transformed
            digit = number % 10
            # Get the digit that can be transformed into
            transformed = rule[1]
            # Check if the digit can be transformed
            if digit == rule[0]:
                # Get the transformed number
                transformed_number = number * 10 + transformed
                # Add the transformed number to the queue
                queue.append(transformed_number)
                # Increment the count of unique numbers
                count += 1
    # Return the count of unique numbers
    return count
def test_generate_numbers():
    # Test case 1
    n1, k1 = 234, 2
    rules1 = [(2, 5), (3, 6)]
    assert generate_numbers(n1, rules1) == 4, "Test case 1 failed"

    # Test case 2
    n2, k2 = 123, 3
    rules2 = [(1, 9), (2, 8), (3, 7)]
    assert generate_numbers(n2, rules2) == 8, "Test case 2 failed"

    # Test case 3
    n3, k3 = 999, 1
    rules3 = [(9, 1)]
    assert generate_numbers(n3, rules3) == 8, "Test case 3 failed"

    print("All test cases passed!")

# Call the test function
test_generate_numbers()