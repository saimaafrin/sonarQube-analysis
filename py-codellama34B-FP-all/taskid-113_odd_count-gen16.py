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

    odd = []
    for i in range(len(lst)):
        odd_digit = 0
        for j in range(len(lst[i])):
            if lst[i][j] in ['1', '3', '5', '7', '9']:
                odd_digit += 1
        odd.append('the number of odd elements ' + str(odd_digit) + 'n the str' + str(odd_digit) + 'ng ' + str(odd_digit) + ' of the ' + str(odd_digit) + 'nput.')
    return odd
