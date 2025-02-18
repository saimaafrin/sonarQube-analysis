from typing import List

def move_one_ball(arr: List[int]) -> bool:
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    >>> move_one_ball([3, 4, 5, 1, 2])
    True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    >>> move_one_ball([3, 5, 4, 1, 2])
    False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """

    # Base condition: If array has only 1 element, return true.
    if len(arr) <= 1:
        return True
    
    # If first element is greater than last element then not possible to
    # arrange in non-decreasing order.
    if arr[0] >= arr[-1]:
        return False

    # We'll try all possible combinations to arrange in non-decreasing order.
    # We'll start with first element and try all possible combinations.
    # We'll maintain a flag to check if it's possible to arrange.
    can_arrange = False
    for i in range(1, len(arr)):
        # If current element is greater than previous element then check if
        # arranging in non-decreasing order by shifting elements after current
        # element.
        if arr[i] > arr[i-1]:
            temp_arr = arr[i:]
            temp_arr.reverse()
            temp_arr.append(arr[i])
            temp_arr = temp_arr[:len(arr)]
            # Check if arranging in non-decreasing order
            if move_one_ball(temp_arr):
                can_arrange = True
                break

    # If after trying all possible combinations, it's still not possible to 
    # arrange in non-decreasing order then return False
    return can_arrange
