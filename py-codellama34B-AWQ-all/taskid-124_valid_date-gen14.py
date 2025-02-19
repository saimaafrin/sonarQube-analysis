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

    # Return False if the date string is empty
    if not date:
        return False

    # Split the string by '-' to get the month, day, and year
    month, day, year = date.split('-')

    # Return False if the date doesn't have three parts
    if not (month and day and year):
        return False

    # Return False if any part can't be converted to an integer
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    # Return False if the year is less than 1 or greater than 31
    if not (1 <= month <= 12):
        return False

    # Return False if the month is less than 1 or greater than 31
    if not (1 <= day <= 31):
        return False

    # Return False if the year is less than 1 or greater than 31
    if not (1 <= year <= 31):
        return False

    # Return False if the year is less than 1 or greater than 31
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not (1 <= day <= 31):
            return False
    elif month in [4, 6, 9, 11]:
        if not (1 <= day <= 30):
            return False
    elif month == 2:
        if not (1 <= day <= 29):
            return False

    return True
