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
    # Initialize the queue with the initial state
    queue = deque([(A, 0)])
    # Initialize the visited states
    visited = set()
    # Initialize the minimum number of steps
    min_steps = 10
    # Loop until the queue is empty
    while queue:
        # Extract the current state
        state = queue.popleft()
        # Check if the current state is the target state
        if state[0] == B:
            # If it is, return the minimum number of steps
            return min_steps
        # Get the source substring and the target substring
        source, target = rules[state[1]]
        # Get the substring to be replaced
        source_substring = state[0][:state[0].index(source)] + target + state[0][state[0].index(source) + len(source):]
        # Get the number of steps
        steps = state[1] + 1
        # Check if the current state has not been visited
        if source_substring not in visited:
            # If it hasn't, add it to the visited states
            visited.add(source_substring)
            # Add the new state to the queue
            queue.append((source_substring, steps))
            # If the minimum number of steps is greater than the current number of steps, update it
            if steps < min_steps:
                min_steps = steps
    # If it's not possible, return "NO ANSWER!"
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