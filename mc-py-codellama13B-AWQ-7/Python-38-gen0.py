from typing import List
def min_remaining_space(V: int, n: int, volumes: List[int]) -> int:
    """
    Calculate the minimum remaining space in a box after trying to fit a number of items with given volumes.
    
    This function uses a dynamic programming approach to determine the maximum volume that can be occupied
    in the box by any subset of the given items. It then returns the difference between the box's total capacity
    and this maximum occupied volume, which is the minimum remaining space.

    Args:
    - V (int): The total capacity of the box.
    - n (int): The number of items to consider for packing into the box.
    - volumes (List[int]): A list of the volumes of the n items.

    Returns:
    - int: The minimum remaining space in the box after fitting the items.

    Examples:
    - min_remaining_space(24, 6, [8, 3, 12, 7, 9, 7]) -> 0
    - min_remaining_space(5, 3, [6, 7, 8]) -> 5

    """
    # Initialize a 2D table with dimensions (n + 1) x (V + 1), with all values set to 0.
    # Note: We add one to n and V to accommodate the extra row and column for the initial values.
    table = [[0] * (V + 1) for _ in range(n + 1)]

    # The values in the first row and column of the table are initialized to 0.
    # These values represent the minimum remaining space in the box when no items are present,
    # and when the box is empty, respectively.

    # For each item, we iterate from the second row to the nth row.
    # In each iteration, we iterate from the second column to the Vth column.
    # For each item and capacity, we compute the maximum volume that can be occupied by any subset of the
    # items, and then update the value of the cell in the table to be the maximum volume that can be
    # occupied by the current item and capacity.
    for item in range(1, n + 1):
        for capacity in range(1, V + 1):
            # Compute the maximum volume that can be occupied by any subset of the items, where the current
            # item is present or absent.
            table[item][capacity] = max(table[item - 1][capacity], table[item - 1][capacity - volumes[item - 1]] + volumes[item - 1])

    # Return the difference between the box's total capacity and the maximum occupied volume.
    # This is the minimum remaining space in the box after trying to fit the items.
    return V - table[n][V]
def test_min_remaining_space():
    # Test case 1: Sample provided in the problem statement where all items can fit perfectly
    V1, n1 = 24, 6
    volumes1 = [8, 3, 12, 7, 9, 7]
    expected1 = 0
    assert min_remaining_space(V1, n1,
                               volumes1) == expected1, f"Test case 1 failed: expected {expected1}, got {min_remaining_space(V1, n1, volumes1)}"

    # Test case 2: Some space is expected to remain in the box
    V2, n2 = 10, 4
    volumes2 = [3, 5, 3, 2]
    expected2 = 0  # Possible packing: 3, 5, and 3, leaves 2 units of space
    assert min_remaining_space(V2, n2,
                               volumes2) == expected2, f"Test case 2 failed: expected {expected2}, got {min_remaining_space(V2, n2, volumes2)}"

    # Test case 3: No items can fit due to the items being larger than the box capacity
    V3, n3 = 5, 3
    volumes3 = [6, 7, 8]
    expected3 = 5  # No items fit, so all 5 units of space remain
    assert min_remaining_space(V3, n3,
                               volumes3) == expected3, f"Test case 3 failed: expected {expected3}, got {min_remaining_space(V3, n3, volumes3)}"

    # If all tests pass, print this:
    print("All test cases passed!")


# Run the test function
test_min_remaining_space()