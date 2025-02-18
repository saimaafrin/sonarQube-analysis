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

    n = len(arr)
    if n == 0:
        return True
    if n == 1:
        return False
    if arr[0] <= arr[1]:
        return False
    # Since all the elements in the list are unique, there will be only one
    # occurrence of the element that is less than or equal to the other element
    # in the list
    right_shift = n - 1
    for i in range(n - 1):
        if arr[i] <= arr[i + 1]:
            right_shift = i
            break
    left_shift = 0
    for i in range(n - 1, 0, -1):
        if arr[i] <= arr[i - 1]:
            left_shift = i
            break
    if right_shift == 0 and left_shift == n - 1:
        return False
    if left_shift == 0:
        # Shift the element to the right by n - 1 positions
        for i in range(n - 1, right_shift, -1):
            arr[i] = arr[i - 1]
        arr[right_shift] = arr[n - 1]
        return True
    # Shift the element to the left by n - 1 positions
    for i in range(left_shift, n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = arr[right_shift]
    return True
