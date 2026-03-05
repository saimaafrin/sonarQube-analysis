
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


    # Helper function to calculate the energy of merging two beads
    def merge_energy(i, j):
        return beads[i] * beads[j] * beads[(i + 1) % len(beads)]

    # Initialize a 2D list to store the maximum energy for merging subproblems
    dp = [[0] * len(beads) for _ in range(len(beads))]

    # Fill the dp table using a bottom-up approach
    for length in range(2, len(beads) + 1):
        for i in range(len(beads) - length + 1):
            j = i + length - 1
            for k in range(i, j):
                dp[i][j] = max(dp[i][k] + dp[k + 1][j] + merge_energy(i, k, k + 1), dp[i][j])

    # The maximum energy for merging all beads is stored in dp[0][len(beads) - 1]
    return dp[0][len(beads) - 1]
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()