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

    valid_date = True
    month, day, year = date.split("-")
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) < 1 or int(day) > 31:
            valid_date = False
    elif int(month) in [4, 6, 9, 11]:
        if int(day) < 1 or int(day) > 30:
            valid_date = False
    elif int(month) == 2:
        if int(day) < 1 or int(day) > 29:
            valid_date = False
    elif int(month) > 12:
        valid_date = False
    elif int(month) < 1:
        valid_date = False

    if len(date.split("-")) != 3:
        valid_date = False

    return valid_date
