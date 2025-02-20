from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    return numbers[0:1] + [delimeter] + numbers[1:2] + [delimeter] + numbers[2:3] + [delimeter] + numbers[3:4] + [delimeter] + numbers[4:5] + [delimeter] + numbers[5:6] + [delimeter] + numbers[6:7] + [delimeter] + numbers[7:8] + [delimeter] + numbers[8:9] + [delimeter] + numbers[9:10] + [delimeter] + numbers[10:11] + [delimeter] + numbers[11:12] + [delimeter] + numbers[12:13] + [delimeter] + numbers[13:14] + [delimeter] + numbers[14:15] + [delimeter] + numbers[15:16] + [delimeter] + numbers[16:17] + [delimeter] + numbers[17:18] + [delimeter] + numbers[18:19] + [delimeter] + numbers[19:20]
