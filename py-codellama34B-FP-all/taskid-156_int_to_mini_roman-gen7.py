def int_to_mini_roman(number: int) -> str:
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19)
    'xix'
    >>> int_to_mini_roman(152)
    'clii'
    >>> int_to_mini_roman(426)
    'cdxxvi'
    """

    if number > 1000 or number < 1:
        raise ValueError("Value should be in range [1, 1000].")
    if number == 1:
        return "i"
    if number == 5:
        return "v"
    if number == 10:
        return "x"
    if number == 50:
        return "l"
    if number == 100:
        return "c"
    if number == 500:
        return "d"
    if number == 1000:
        return "m"

    number_str = str(number)
    result = ""
    for i, char in enumerate(number_str):
        if char == "1":
            if number_str[i + 1] == "0":
                result += "i"
            else:
                result += "x"
        elif char == "5":
            result += "v"
        elif char == "9":
            result += "x"
        elif char == "0":
            result += "l"
        elif char == "4":
            result += "l"
        elif char == "8":
            result += "l"
        elif char == "3":
            result += "x"
        elif char == "7":
            result += "l"
        elif char == "2":
            result += "x"
        elif char == "6":
            result += "l"
    return result
