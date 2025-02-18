from typing import List

def odd_count(lst: List[str]) -> List[str]:
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ['the number of odd elements 4n the str4ng 4 of the 4nput.']
    >>> odd_count(['3', '11111111'])
    ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 8n the str8ng 8 of the 8nput.']
    """

    odd_count_result = []
    for i in lst:
        odd_count = 0
        for j in i:
            if int(j) % 2 != 0:
                odd_count += 1
        odd_count_result.append(f'the number of odd elements {odd_count}n the str{len(i)}ng {len(i)} of the {len(i)}nput.')
    return odd_count_result
\end{code}
