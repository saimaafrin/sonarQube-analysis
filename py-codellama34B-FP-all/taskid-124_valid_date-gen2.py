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

    if not date or len(date) != 10:
        return False

    if '-' not in date:
        return False

    day, month, year = date.split('-')

    if year.isdigit() and len(year) == 4:
        year = int(year)
    else:
        return False

    if day.isdigit() and len(day) == 2:
        day = int(day)
    else:
        return False

    if month.isdigit() and len(month) == 2:
        month = int(month)
    else:
        return False

    if (month < 1 or month > 12) or (day < 1 or day > 31) or (
            day > 30 and (month == 4 or month == 6 or month == 9 or month == 11)):
        return False

    if (month == 2 and day > 28) or (month == 2 and day > 29 and (year % 4 != 0)):
        return False

    return True
