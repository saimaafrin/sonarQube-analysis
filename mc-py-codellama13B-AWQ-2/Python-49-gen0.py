def hanoi_double_iterative(n: int) -> int:
    """
    Calculate the minimum number of moves required to solve the double-disc Hanoi Towers problem for n pairs of discs.
    
    This function implements an iterative algorithm to determine the minimum number of moves necessary to transfer
    2n discs from the A pole to the C pole in a double-disc Hanoi Towers setup, following the rules that only one disc 
    can be moved at a time and no disc may be placed on top of a smaller disc. The function uses a known recursive relation 
    and iteratively computes the total number of moves for n pairs of discs.
    
    Args:
    n (int): The number of disc pairs (each of two identical discs) on the A pole.

    Returns:
    int: The minimum number of moves required to transfer all the discs from the A pole to the C pole.

    Cases:
    - For n=1, the function should return 2.
    - For n=2, the function should return 6.
    - For n=3, the function should return 14.
    """
    # Initialize the value of the minimum number of moves to zero
    moves = 0

    # Calculate the minimum number of moves required to transfer the first disc pair
    moves += 2**n
    
    # Initialize the current number of disc pairs to the number of disc pairs passed in the function call
    current_number_of_disc_pairs = n

    # Calculate the minimum number of moves required to transfer each additional disc pair
    while current_number_of_disc_pairs > 0:

        # Add the number of moves required to transfer the current number of disc pairs to the total number of moves
        moves += 2**current_number_of_disc_pairs

        # Decrease the current number of disc pairs by 1
        current_number_of_disc_pairs -= 1

    # Return the minimum number of moves required to transfer all the discs
    return moves
def test_hanoi_double_iterative():
    # Test case 1: n = 1
    assert hanoi_double_iterative(1) == 2, "Test case 1 failed"

    # Test case 2: n = 2
    assert hanoi_double_iterative(2) == 6, "Test case 2 failed"

    # Test case 3: n = 3
    assert hanoi_double_iterative(3) == 14, "Test case 3 failed"

    # Additional test cases can be added based on computed or known results
    # Test case 4: n = 4 (computed using the formula)
    assert hanoi_double_iterative(4) == 30, "Test case 4 failed"

    # Test case 5: n = 5 (computed using the formula)
    assert hanoi_double_iterative(5) == 62, "Test case 5 failed"

    # Test case 6: Large n, n = 10 (computed using the formula or a trusted source)
    assert hanoi_double_iterative(10) == 2046, "Test case 6 failed"

    print("All test cases passed!")


# Run the test function
test_hanoi_double_iterative()