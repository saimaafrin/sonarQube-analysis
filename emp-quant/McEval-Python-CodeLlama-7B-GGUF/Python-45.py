import heapq
from typing import List 

def minimum_cost_to_merge_fruits(fruit_counts: List[int]) -> int:
    """
    Calculates the minimum total cost to merge multiple heaps of fruits into a single heap.
    The cost of merging two heaps is equal to the sum of their weights. The function utilizes
    a greedy algorithm with a min-heap (priority queue) to ensure the smallest heaps are merged first,
    minimizing the total cost.

    Parameters:
    fruit_counts (List[int]): A list of integers representing the counts of each type of fruit.

    Returns:
    int: The minimum total cost required to merge all heaps of fruits.

    Examples:
    >>> minimum_cost_to_merge_fruits([1, 2, 9])
    15
    >>> minimum_cost_to_merge_fruits([10, 20, 30, 40, 50])
    300 .
    """
    # Initialize a min-heap with the fruit counts.
    min_heap = []
    for fruit_count in fruit_counts:
        heapq.heappush(min_heap, fruit_count)

    # Initialize the total cost to zero.
    total_cost = 0

    # While there are still fruits to merge.
    while len(min_heap) > 1:
        # Pop the smallest fruit from the min-heap.
        smallest_fruit = heapq.heappop(min_heap)

        # If there are still fruits to merge.
        if len(min_heap) > 0:
            # Pop the next smallest fruit from the min-heap.
            next_smallest_fruit = heapq.heappop(min_heap)

            # Calculate the total cost of merging the two fruits.
            total_cost += smallest_fruit + next_smallest_fruit

            # Push the merged fruit back into the min-heap.
            heapq.heappush(min_heap, smallest_fruit + next_smallest_fruit)

    # Return the total cost.
    return total_cost
def test_minimum_cost_to_merge_fruits():
    # Test case 1: As provided in the problem statement example
    fruits1 = [1, 2, 9]
    assert minimum_cost_to_merge_fruits(fruits1) == 15, "Test case 1 failed"

    # Test case 2: Simple case with only two types of fruits
    fruits2 = [5, 5]
    assert minimum_cost_to_merge_fruits(fruits2) == 10, "Test case 2 failed"

    # Test case 3: More complex case with multiple types of fruits
    fruits3 = [10, 20, 30, 40, 50]
    assert minimum_cost_to_merge_fruits(fruits3) == 330, "Test case 3 failed"

    # Test case 4: Case with fruits having the same count
    fruits4 = [3, 3, 3, 3]
    assert minimum_cost_to_merge_fruits(fruits4) == 24, "Test case 4 failed"

    # Test case 5: Case with a single type of fruit
    fruits5 = [7]
    assert minimum_cost_to_merge_fruits(fruits5) == 0, "Test case 5 failed"

    print("All test cases passed.")

# Run the test function
test_minimum_cost_to_merge_fruits()