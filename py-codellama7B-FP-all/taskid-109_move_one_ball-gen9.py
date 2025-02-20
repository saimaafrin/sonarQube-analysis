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

    # Sort the array in ascending order
    arr.sort()
    # If the array is sorted in ascending order then we return True
    if arr == sorted(arr):
        return True
    # If the array is not sorted in ascending order then we check if the first
    # element of the array is greater than the last element of the array
    # If the first element of the array is greater than the last element of the
    # array then we return False
    if arr[0] > arr[-1]:
        return False
    # If the first element of the array is less than or equal to the last
    # element of the array then we check if the remaining elements of the array
    # are in descending order or not
    for i in range(1, len(arr)):
        # If the ith element of the array is less than or equal to the (i-1)th
        # element of the array then we return False
        if arr[i] <= arr[i-1]:
            return False
    # If we reach this point then we return True
    return True
