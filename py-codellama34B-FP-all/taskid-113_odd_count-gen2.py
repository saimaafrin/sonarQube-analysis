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

    odd_count = []
    for string in lst:
        odd_nums = 0
        for num in string:
            if int(num) % 2 == 1:
                odd_nums += 1
        odd_count.append(f"the number of odd elements {odd_nums}n the str{odd_nums}ng {odd_nums} of the {odd_nums}nput.")
    return odd_count
