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

    # You can use the below line if you want to split the date by '-'
    # date = date.split('-')
    # if len(date) != 3: return False
    # month, day, year = date
    # if int(day) not in [1, 31]:
    #     if int(day) in [31, 28]:
    #         if int(month) not in [3, 5, 8, 10]:
    #             return False
    #         if int(month) == 2 and int(year) % 4 == 0:
    #             return False
    #     else:
    #         if int(month) in [4, 6, 9, 11]:
    #             return False
    #         else:
    #             return False
    # if int(month) < 1 or int(month) > 12:
    #     return False
    # return True

    # or
    # You can use the below line if you want to split the date by '-'
    # date = date.split('-')
    # if len(date) != 3: return False
    # month, day, year = date
    # if not (1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1900 <= int(year) <= 2100):
    #     return False
    # if int(day) not in [31, 28, 30, 31, 30, 31, 31, 30, 31, 30, 31] or int(month) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    #     return False
    # return True

    # or
    month, day, year = date.split("-")
    if not (1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1900 <= int(year) <= 2100):
        return False
    if int(day) not in [31, 28, 30, 31, 30, 31, 31, 30, 31, 30, 31] or int(month) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        return False
    return True
