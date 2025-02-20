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

    date_list = date.split('-')
    if len(date_list) != 3:
        return False
    else:
        months = ['1','3','5','7','8','10','12']
        days = ['2','4','6','9','11']
        for i in months:
            if date_list[0] == i:
                if date_list[1] > 31:
                    return False
            else:
                pass
        for j in days:
            if date_list[0] == j:
                if date_list[1] > 30:
                    return False
            else:
                pass
        if date_list[0] == '2':
            if date_list[1] > 29:
                return False
        else:
            pass
        if len(date_list[0]) > 2 or len(date_list[1]) > 2 or len(date_list[2]) > 4:
            return False
        else:
            pass
        if date_list[0] < 1 or date_list[0] > 12:
            return False
        else:
            pass
        return True
