def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    numbers = numbers.split(" ")
    numbers_sorted = sorted(numbers, key=lambda x: x.strip("one").strip("two").strip("three").strip("four").strip("five").strip("six").strip("seven").strip("eight").strip("nine"))
    return " ".join(numbers_sorted)
