from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    numbers_length = len(numbers)
    if numbers_length == 0:
        return numbers
    if numbers_length == 1:
        return [numbers[0]]
    result = numbers[:1]
    for i in range(1, numbers_length - 1):
        result.append(numbers[i])
        result.append(delimeter)
    result.append(numbers[-1])
    return result
\end{code}

\section{Example}

\begin{code}
