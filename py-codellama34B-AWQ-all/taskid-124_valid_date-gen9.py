def valid_date(date: str) -> bool:
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    >>> valid_date('03-11-2000')
    True

    >>> valid_date('15-01-2012')
    False

    >>> valid_date('04-0-2040')
    False

    >>> valid_date('06-04-2020')
    True

    >>> valid_date('06/04/2020')
    False
    """


    month_day_dict = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    # Checking if date string is empty.
    if not date:
        return False

    # Checking if the date string is in format: mm-dd-yyyy
    if not (date.count("-") == 2 and date.count("-") == date.count("/") + date.count("-")):
        return False

    month, day, year = date.split("-")

    # Checking if the month is between 1 and 12
    if not (1 <= int(month) <= 12):
        return False

    # Checking if the day is between 1 and the number of days for the month.
    if not (1 <= int(day) <= month_day_dict[int(month)]):
        return False

    # Checking if the year is 4 digits long
    if not (len(year) == 4):
        return False

    # If the date is valid
    return True
