from typing import List

def smallest_change(arr: List[int]) -> int:
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    >>> smallest_change([1, 2, 3, 5, 4, 7, 9, 6])
    4
    >>> smallest_change([1, 2, 3, 4, 3, 2, 2])
    1
    >>> smallest_change([1, 2, 3, 2, 1])
    0
    """

    # 1. We can start by getting rid of duplicates
    # 2. We can get rid of any duplicates by swapping them with other duplicates
    # 3. Then we can make it a palindrome by reversing it
    # 4. We can do step 1 and step 2 in O(N)
    # 5. We can do step 3 in O(N)
    # 6. So the overall time complexity is O(N^2)
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    duplicates.difference_update(seen)
    arr[:] = [x for x in arr if x not in duplicates]
    arr.sort()
    if len(arr) % 2 == 0 and arr[-1] == arr[-2]:
        arr.pop()
    arr.reverse()
    return len(arr) - len(set(arr))
