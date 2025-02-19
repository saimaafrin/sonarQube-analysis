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


    date_values = date.split('-')
    if len(date_values) != 3:
        return False

    month = int(date_values[0])
    day = int(date_values[1])
    year = int(date_values[2])

    # is month in range 1 to 12?
    if not 1 <= month <= 12:
        return False

    # is day in range 1 to 31?
    if not 1 <= day <= 31:
        return False

    # is year valid?
    if len(str(year)) != 4:
        return False

    # is date in the right format?
    if '-' not in date:
        return False

    # is day in the range for the given month?
    if month == 2:
        if not 1 <= day <= 29:
            return False
    elif month in (4, 6, 9, 11):
        if not 1 <= day <= 30:
            return False
    else:
        if not 1 <= day <= 31:
            return False

    return True
