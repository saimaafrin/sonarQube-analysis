from typing import List

def sort_array(arr: List[int]) -> List[int]:
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4])
    [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6])
    [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4])
    [0, 1, 2, 3, 4]
    """

    # The idea is to sort the array and then use a map to change the numbers back to their original state
    # The values in the map are the bitwise and of the decimal values with a mask that corresponds to the number of bits.
    # This will keep all the bits that are present in the decimal value and 0s for the bits that are not.
    # Then we simply sort the array based on the masked values

    # First sort the array
    arr = sorted(arr)

    # Next we need to create a map of the decimal values to their masked values
    # The mask is the number of bits we want to keep in the decimal value
    # We can get this by taking the number of bits that correspond to the decimal value
    # Example: 15 decimal value has 4 bits, so we only keep the last 4 bits when we mask.
    # The idea is that this will give us the highest bits that correspond to the decimal value.

    # We first find the largest value in the array
    largest = max(arr)

    # Then we create a list of masks that correspond to each value
    # The number of bits we keep in each decimal value is determined by the number of bits that correspond to the largest value
    masks = [2 ** (len(bin(largest)) - 2 - i) for i in range(len(bin(largest)) - 2)]

    # Then we create a map of the decimal values to their masked values
    # This will keep all the bits that are present in the decimal value and 0s for the bits that are not.
    # This is the reason we need to use a map and not just sort directly based on the masked values.
    # This is because there are more than one decimal value with the same masked value
    decimal_to_masked = {d: d & mask for d in arr}

    # Finally we sort the array based on the masked values
    # This will ensure that we have the highest number of ones first and then the next number of ones and so on
    arr.sort(key=lambda x: decimal_to_masked[x])

    return arr
