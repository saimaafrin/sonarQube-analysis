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
    date_parts = date.split('-')
    if not len(date_parts) == 3:
        return False
    try:
        year = int(date_parts[2])
        month = int(date_parts[0])
        day = int(date_parts[1])
        if (month > 12 or month < 1 or year > 2020 or year < 2000):
            return False
        if (month in [1,3,5,7,8,10,12] and (day > 31 or day < 1)):
            return False
        if (month in [4,6,9,11] and (day > 30 or day < 1)):
            return False
        if (month == 2 and (day > 29 or day < 1)):
            return False
    except ValueError:
        return False
    return True
