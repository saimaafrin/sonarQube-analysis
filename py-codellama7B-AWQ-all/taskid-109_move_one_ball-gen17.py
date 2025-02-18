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

    N = len(arr)
    if N == 0:
        return True
    if N == 1:
        return True
    if N == 2:
        if arr[1] > arr[0]:
            return False
        else:
            return True
    
    # Step 1: find the last non decreasing sub array
    max_arr = []
    for i in range(N-1, -1, -1):
        if arr[i] < arr[i-1]:
            break
        else:
            max_arr.append(arr[i])
    
    # Step 2: find the next non decreasing sub array
    min_arr = []
    for j in range(0, N):
        if arr[j] < arr[j+1]:
            break
        else:
            min_arr.append(arr[j])
    min_arr.reverse()
    
    # Step 3: check for the possibility
    if max_arr == arr or min_arr == arr:
        return True
    else:
        return False
