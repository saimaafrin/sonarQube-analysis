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
        date_split = date.split('-')
        if len(date_split) == 3:
            month = date_split[0]
            day = date_split[1]
            year = date_split[2]
        else:
            return False

        if 1 <= int(month) <= 12:
            if (int(month) in [1, 3, 5, 7, 8, 10, 12] and 1 <= int(day) <= 31) or (int(month) in [4, 6, 9, 11] and 1 <= int(day) <= 30) or (int(month) == 2 and 1 <= int(day) <= 29):
                if len(year) == 4:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    except ValueError:
        return False
    except TypeError:
        return False
