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
    # Initialize the number of moves to 0.
    moves = 0

    # Initialize the number of discs on the A pole.
    discs_on_A = n

    # Initialize the number of discs on the B pole.
    discs_on_B = 0

    # Initialize the number of discs on the C pole.
    discs_on_C = 0

    # Initialize the number of discs on the D pole.
    discs_on_D = 0

    # Initialize the number of discs on the E pole.
    discs_on_E = 0

    # Initialize the number of discs on the F pole.
    discs_on_F = 0

    # Initialize the number of discs on the G pole.
    discs_on_G = 0

    # Initialize the number of discs on the H pole.
    discs_on_H = 0

    # Initialize the number of discs on the I pole.
    discs_on_I = 0

    # Initialize the number of discs on the J pole.
    discs_on_J = 0

    # Initialize the number of discs on the K pole.
    discs_on_K = 0

    # Initialize the number of discs on the L pole.
    discs_on_L = 0

    # Initialize the number of discs on the M pole.
    discs_on_M = 0

    # Initialize the number of discs on the N pole.
    discs_on_N = 0

    # Initialize the number of discs on the O pole.
    discs_on_O = 0

    # Initialize the number of discs on the P pole.
    discs_on_P = 0

    # Initialize the number of discs on the Q pole.
    discs_on_Q = 0

    # Initialize the number of discs on the R pole.
    discs_on_R = 0

    # Initialize the number of discs on the S pole.
    discs_on_S = 0

    # Initialize the number of discs on the T pole.
    discs_on_T = 0

    # Initialize the number of discs on the U pole.
    discs_on_U = 0

    # Initialize the number of discs on the V pole.
    discs_on_V = 0

    # Initialize the number of discs on the W pole.
    discs_on_W = 0

    # Initialize the number of discs on the X pole.
    discs_on_X = 0

    # Initialize the number of discs on the Y pole.
    discs_on_Y = 0

    # Initialize the number of discs on the Z pole.
    discs_on_Z = 0

    # Initialize the number of discs on the AA pole.
    discs_on_AA = 0

    # Initialize the number of discs on the AB pole.
    discs_on_AB = 0

    # Initialize the number of
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