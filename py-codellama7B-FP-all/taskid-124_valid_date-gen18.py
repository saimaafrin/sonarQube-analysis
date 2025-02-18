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

    if not date:
        return False
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False

    if not month or not day or not year:
        return False

    if int(month) > 12 or int(month) < 1:
        return False

    if int(year) < 1:
        return False

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
        month_days[1] = 29

    if int(month) in (1, 3, 5, 7, 8, 10, 12) and int(day) > 31 or int(day) < 1:
        return False

    if int(month) in (4, 6, 9, 11) and int(day) > 30 or int(day) < 1:
        return False

    if int(month) == 2 and int(day) > month_days[1] or int(day) < 1:
        return False

    if int(day) > month_days[int(month) - 1] or int(day) < 1:
        return False

    return True
