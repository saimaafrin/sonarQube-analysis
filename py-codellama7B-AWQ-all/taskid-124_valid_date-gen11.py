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

    # Your code here
    if len(date) == 0:
        return False

    if date[2] == '0' or date[5] == '0':
        return False

    if int(date[2]) < 1 or int(date[2]) > 12:
        return False

    if int(date[0]) == 2 and int(date[2]) != 2:
        if int(date[3]) < 1 or int(date[3]) > 28:
            return False

    if int(date[0]) in [1, 3, 5, 7, 8, 10, 12]:
        if int(date[3]) < 1 or int(date[3]) > 31:
            return False
    elif int(date[0]) in [4, 6, 9, 11]:
        if int(date[3]) < 1 or int(date[3]) > 30:
            return False
    else:
        if int(date[3]) < 1 or int(date[3]) > 29:
            return False

    return True
