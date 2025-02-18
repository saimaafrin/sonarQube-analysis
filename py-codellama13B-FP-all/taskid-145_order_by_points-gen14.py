from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    """

    result = []
    points = {}
    for i, num in enumerate(nums):
        if abs(num) not in points:
            points[abs(num)] = [0, i]
        else:
            points[abs(num)][0] += 1
            points[abs(num)][1] = i

    for key in sorted(points, key=points.get):
        result.append(points[key][1])

    return result
