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

    date_split = date.split('-')

    if len(date_split) != 3:
        return False

    if date_split[0] == '02' and int(date_split[1]) == 29:
        return True

    if date_split[0] == '02' and int(date_split[1]) != 29:
        return False

    months = ['01', '03', '05', '07', '08', '10', '12']

    if date_split[0] in months and int(date_split[1]) >= 31:
        return False

    months = ['04', '06', '09', '11']

    if date_split[0] in months and int(date_split[1]) >= 30:
        return False

    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    if date_split[0] in months and int(date_split[1]) >= 32:
        return False

    if date_split[0] not in months:
        return False

    if int(date_split[1]) < 1:
        return False

    return True
