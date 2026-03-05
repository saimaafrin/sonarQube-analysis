from collections import deque
from typing import Union
def string_transformation(A: str, B: str, rules: list) -> Union[int, str]:
    """
    Perform string transformation from A to B using a set of transformation rules.

    This function takes an initial string A and a target string B, along with a list
    of transformation rules, and attempts to transform A into B using the rules.
    A Breadth-First Search (BFS) algorithm is used to explore the possible transformations
    up to a maximum of 10 steps. If A can be transformed into B within 10 steps, the function
    returns the minimum number of steps required. If it's not possible, the function returns
    "NO ANSWER!".

    Parameters:
    A (str): The initial string to be transformed.
    B (str): The target string to be achieved.
    rules (list of tuples): A list of transformation rules, where each rule is a tuple
                            containing the source substring (to be replaced) and the
                            target substring (to replace with).

    Returns:
    Union[int, str]: The minimum number of transformation steps if possible, otherwise "NO ANSWER!".

    Examples:
    >>> string_transformation("abcd", "xyz", [("abc", "xu"), ("ud", "y"), ("y", "yz")])
    3
    >>> string_transformation("aaa", "bbbb", [("a", "b"), ("aa", "bb"), ("aaa", "bbb")])
    'NO ANSWER!'
    """


    # Initialize the queue with the initial string and the number of steps (0)
    queue = deque([(A, 0)])

    # Set to keep track of visited strings to avoid processing the same string multiple times
    visited = set()

    # Process the queue until it's empty
    while queue:
        current_string, steps = queue.popleft()

        # If the current string is the target string, return the number of steps
        if current_string == B:
            return steps

        # If the current string has already been visited, skip it
        if current_string in visited:
            continue

        # Mark the current string as visited
        visited.add(current_string)

        # Apply each transformation rule to the current string
        for source, target in rules:
            # Find all occurrences of the source substring in the current string
            start = 0
            while start < len(current_string):
                start = current_string.find(source, start)
                if start == -1:
                    break
                # Create a new string with the source substring replaced by the target substring
                new_string = current_string[:start] + target + current_string[start + len(source):]
                # Add the new string to the queue with an incremented step count
                queue.append((new_string, steps + 1))
                # Move the start index forward to find the next occurrence of the source substring
                start += len(target)

        # If the number of steps exceeds 10, return "NO ANSWER!"
        if steps > 10:
            return "NO ANSWER!"

    # If the target string is not reachable, return "NO ANSWER!"
    return "NO ANSWER!"
def test_string_transformation():
    # Test case 1
    A1 = "abcd"
    B1 = "xyz"
    rules1 = [("abc", "xu"), ("ud", "y"), ("y", "yz")]
    expected_result1 = 3
    assert string_transformation(A1, B1, rules1) == expected_result1, "Test case 1 failed"

    # Test case 2
    A2 = "aaa"
    B2 = "bbbb"
    rules2 = [("a", "b"), ("aa", "bb"), ("aaa", "bbb")]
    expected_result2 = "NO ANSWER!"
    assert string_transformation(A2, B2, rules2) == expected_result2, "Test case 2 failed"

    # Test case 3
    A3 = "hello"
    B3 = "world"
    rules3 = [("h", "w"), ("e", "o"), ("l", "r"), ("lol", "ldr")]
    expected_result3 = "NO ANSWER!"
    assert string_transformation(A3, B3, rules3) == expected_result3, "Test case 3 failed"

    print("All test cases passed!")

# Run the test function
test_string_transformation()