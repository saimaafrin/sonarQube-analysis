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

    # Base condition
    if len(arr) <= 1:
        return True
    
    # Step 1: If the first element of the array is greater than the last element
    # then we can sort the array by performing a right shift operation.
    if arr[0] > arr[-1]:
        return True
    
    # Step 2: Find the maximum element in the given array.
    max_element = max(arr)
    max_element_index = arr.index(max_element)
    
    # Step 3: Find the minimum element in the given array.
    min_element = min(arr)
    min_element_index = arr.index(min_element)
    
    # Step 4: If the first element of the array is greater than the minimum
    # element of the array then we can sort the array by performing a right
    # shift operation.
    if arr[0] > min_element:
        return True
    
    # Step 5: If the maximum element of the array is greater than the last 
    # element of the array then we can sort the array by performing a right
    # shift operation.
    if max_element > arr[-1]:
        return True
    
    # Step 6: If the maximum element of the array is greater than the first
    # element of the array then we can sort the array by performing a right
    # shift operation.
    if max_element > arr[0]:
        return True
    
    # Step 7: If the maximum element of the array is greater than the minimum
    # element of the array then we can sort the array by performing a right
    # shift operation.
    if max_element > min_element:
        return True
    
    # Step 8: If the maximum element of the array is greater than the first
    # element of the array then we can sort the array by performing a right
    # shift operation.
    if max_element > arr[0]:
        return True
    
    # Step 9: If the minimum element of the array is greater than the last
    # element of the array then we can sort the array by performing a right
    # shift operation.
    if min_element > arr[-1]:
        return True
    
    # Step 10: Return False if the above conditions are not met.
    return False
