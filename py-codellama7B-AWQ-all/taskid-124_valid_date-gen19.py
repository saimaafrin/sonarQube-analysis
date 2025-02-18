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

    if date == "":
        return False
    if date.count("-") != 2:
        return False
    mm, dd, yyyy = date.split("-")
    if not mm.isdigit() or not dd.isdigit() or not yyyy.isdigit():
        return False
    if int(yyyy) < 1900:
        return False
    if int(yyyy) > 2050:
        return False
    if int(yyyy) % 4 == 0 and int(yyyy) % 100 != 0 and int(yyyy) % 400 == 0:
        days_in_month_feb = 29
    else:
        days_in_month_feb = 28
    if int(mm) not in [1, 3, 5, 7, 8, 10, 12]:
        if int(dd) not in range(1, 31):
            return False
    elif int(mm) in [4, 6, 9, 11]:
        if int(dd) not in range(1, 30):
            return False
    elif int(mm) == 2:
        if int(dd) not in range(1, days_in_month_feb):
            return False
    else:
        return False
    if int(mm) not in range(1, 13):
        return False
    return True
