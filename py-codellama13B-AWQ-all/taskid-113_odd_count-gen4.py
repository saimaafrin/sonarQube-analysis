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

    # You can use str.count(sub) to count how many times the substring "1" appears in s.

    # Solution 1
    # return [f"the number of odd elements in the string {i} of the input.".replace("1", str(s.count("1"))) for i, s in enumerate(lst, 1)]

    # Solution 2
    return [f"the number of odd elements in the string {i} of the input.".replace("1", str(len([x for x in s if x == "1"]) or 0)) for i, s in enumerate(lst, 1)]
