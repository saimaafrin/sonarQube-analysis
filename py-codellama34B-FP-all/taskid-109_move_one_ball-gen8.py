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

    # First we need to find the index of the largest element in the list and
    # the index of the smallest element in the list. If the smallest element
    # is in position 0, then we know that the list is sorted. Otherwise, we
    # need to check if there are any elements that are out of order, such
    # that they are not in their sorted positions.
    largest_element_index = arr.index(max(arr))
    smallest_element_index = arr.index(min(arr))
    # If the smallest element is in position 0, then the list is sorted.
    if smallest_element_index == 0:
        return True
    # If the largest element is in position N - 1, then the list is not sorted.
    if largest_element_index == len(arr) - 1:
        return False
    # If the smallest element is not in position 0, then it must be in the
    # largest element's position.
    if smallest_element_index != largest_element_index:
        return False
    # If we have not returned yet, then we know that the smallest element is
    # in the largest element's position. We can perform a right shift on the
    # array. If the smallest element ends up in position 0 after the right
    # shift, then the list is sorted.
    arr.append(arr.pop(0))
    return arr.index(min(arr)) == 0
