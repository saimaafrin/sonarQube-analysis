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

    if not arr:
        return True
    
    # if there is only one element, return True
    if len(arr) == 1:
        return True
    
    # if the second last element is greater than or equal to the last element,
    # then the array is already sorted, so return True
    if arr[-1] >= arr[-2]:
        return True
    
    # if the last element is greater than the second last element, then check if
    # the second last element is greater than or equal to the third last element
    if arr[-2] < arr[-3]:
        # since the last element is greater than the second last element, then the
        # second last element is the maximum element in the array, so the third
        # last element must be greater than or equal to the second last element to
        # make the array sorted
        return arr[-3] >= arr[-2]
    
    # if the last element is less than the second last element, then check if the
    # second last element is greater than or equal to the third last element
    if arr[-2] > arr[-3]:
        # since the last element is less than the second last element, then the
        # second last element is not the maximum element in the array, so the third
        # last element must be greater than the second last element to make the
        # array sorted
        return arr[-3] > arr[-2]
