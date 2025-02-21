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

    # Base case
    if not arr:
        return True

    # Checking if array is already sorted
    if arr[0] < arr[-1]:
        return False

    # Checking for the special case where array consists of only one element
    if len(arr) == 1:
        return True

    # Checking for the special case where there are only two elements in the array
    if len(arr) == 2 and arr[0] < arr[1]:
        return False

    # Checking for the special case where there are more than two elements and
    # all the elements in the array are the same.
    if arr.count(arr[0]) == len(arr):
        return False

    # Checking for the case where we can get the sorted array
    # by performing one right shift operation
    if len(arr) == 3 and arr[0] < arr[1] and arr[1] < arr[2]:
        return True

    # Checking for the case where we can get the sorted array
    # by performing one right shift operation
    if len(arr) == 4 and arr[0] < arr[1] and arr[1] < arr[2] and arr[2] < arr[3]:
        return True

    # Checking for the case where we can get the sorted array
    # by performing one right shift operation
    if len(arr) == 5 and arr[0] < arr[1] and arr[1] < arr[2] and arr[2] < arr[3] and arr[3] < arr[4]:
        return True

    # Checking for the case where we can get the sorted array
    # by performing one right shift operation
    if len(arr) == 6 and arr[0] < arr[1] and arr[1] < arr[2] and arr[2] < arr[3] and arr[3] < arr[4] and arr[4] < arr[5]:
        return True

    # Checking for the case where we can get the sorted array
    # by performing one right shift operation
    if len(arr) == 7 and arr[0] < arr[1] and arr[1] < arr[2] and arr[2] < arr[3] and arr[3] < arr[4] and arr[4] < arr[5] and arr[5] < arr[6]:
        return True

    # Checking for the case where we can get the sorted array
    # by performing one right shift operation
    if len(arr) == 8 and arr[0] < arr[1] and arr[1] < arr[2] and arr[2] < arr[3] and arr[3] < arr[4] and arr[4] < arr[5] and arr[5] < arr[6] and arr[6] < arr[7]:
        return True
