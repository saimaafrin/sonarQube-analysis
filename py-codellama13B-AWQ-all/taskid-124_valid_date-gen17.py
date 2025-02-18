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

    date_list = date.split("-")

    if len(date_list) != 3:
        return False

    if date_list[0].isdigit() and date_list[1].isdigit() and date_list[2].isdigit():
        if int(date_list[0]) in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= int(date_list[1]) <= 31:
                return True
            else:
                return False
        if int(date_list[0]) in [4, 6, 9, 11]:
            if 1 <= int(date_list[1]) <= 30:
                return True
            else:
                return False
        if int(date_list[0]) == 2:
            if int(date_list[2]) % 4 == 0:
                if 1 <= int(date_list[1]) <= 29:
                    return True
                else:
                    return False
            else:
                if 1 <= int(date_list[1]) <= 28:
                    return True
                else:
                    return False
        if 1 <= int(date_list[0]) <= 12:
            return True
        else:
            return False

    return False
