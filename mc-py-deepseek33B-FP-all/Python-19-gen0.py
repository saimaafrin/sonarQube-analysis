
def max_energy(beads):
    """
    Calculate the maximum energy that can be released by merging beads on a necklace.

    The function takes a list of integers representing the energy beads on a necklace, where
    each bead has a head and a tail value. The head value of each bead must match the tail
    value of the next bead in the sequence. The necklace is circular, and merging two adjacent
    beads releases energy equal to the product of the head value of the first bead, the matching
    value, and the tail value of the second bead.

    To find the maximum energy release, the function considers all possible orders of merging beads
    and uses dynamic programming to compute the maximum energy obtainable.

    Args:
        beads: A list of integers where each integer represents the head value of a bead and
               the tail value of the previous bead. The tail value of the last bead is assumed
               to match the head value of the first bead due to the circular nature of the necklace.

    Returns:
        An integer representing the maximum energy that can be obtained by optimally merging all beads.

    Examples:
        >>> max_energy([2, 3, 5, 10])
        710
        >>> max_energy([1, 2, 3, 4])
        48
    """
    n = len(beads)

    # Initialize dp table
    dp = [[0] * n for _ in range(n)]

    # Base case: length 1
    for i in range(n):
        dp[i][i] = 0

    # Base case: length 2
    for i in range(n - 1):
        dp[i][i + 1] = beads[i] * beads[i + 1] * beads[(i + 2) % n]

    # DP calculation
    for length in range(3, n + 1):
        for i in range(n):
            j = (i + length - 1) % n
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[(k + 1) % n][j] + beads[i] * beads[(k + 1) % n] * beads[(j + 1) % n])

    # The maximum energy is the maximum value in the first row of the dp table
    return max(dp[0])
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()