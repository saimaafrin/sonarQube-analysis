
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
    # Initialize a dictionary to store the maximum energy for each possible merge order
    # The key is a tuple of the form (i, j) where i and j are the indices of the beads to be merged
    # The value is the maximum energy that can be obtained by merging the beads at indices i and j
    # The dictionary is initialized with the maximum energy for the trivial case of merging only one bead
    dp = {(0, 0): beads[0]}

    # Loop through all possible merge orders
    for i in range(1, len(beads)):
        for j in range(i, len(beads)):
            # Calculate the maximum energy for merging the beads at indices i and j
            # The maximum energy is the maximum of the following:
            # 1. The energy for merging the beads at indices i-1 and j
            # 2. The energy for merging the beads at indices i and j-1
            # 3. The energy for merging the beads at indices i-1 and j-1
            # The energy for merging the beads at indices i-1 and j is the maximum of the following:
            # 1. The energy for merging the beads at indices i-2 and j
            # 2. The energy for merging the beads at indices i-2 and j-1
            # 3. The energy for merging the beads at indices i-2 and j-2
            # The energy for merging the beads at indices i and j-1 is the maximum of the following:
            # 1. The energy for merging the beads at indices i-1 and j-2
            # 2. The energy for merging the beads at indices i-1 and j-3
            # 3. The energy for merging the beads at indices i-1 and j-4
            # The energy for merging the beads at indices i-1 and j-2 is the maximum of the following:
            # 1. The energy for merging the beads at indices i-2 and j-3
            # 2. The energy for merging the beads at indices i-2 and j-4
            # 3. The energy for merging the beads at indices i-2 and j-5
            # The energy for merging the beads at indices i-1 and j-3 is the maximum of the following:
            # 1. The energy for merging the beads at indices i-2 and j-4
            # 2. The energy for merging the beads at indices i-2 and j-5
            # 3. The energy for merging the beads at indices i-2 and j-6
            # The energy for merging the beads at indices i-1 and j-4 is the maximum of the following:
            # 1. The energy for merging the beads at indices i-2 and j-5
            # 2. The energy for merging the beads at indices i-2 and j-6
            # 3
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()