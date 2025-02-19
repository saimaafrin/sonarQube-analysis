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


    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    months_29 = [2]

    def valid_month(month):
        return 1 <= month <= 12

    def valid_days(month, day):
        if month in months_31:
            return 1 <= day <= 31
        elif month in months_30:
            return 1 <= day <= 30
        elif month in months_29:
            return 1 <= day <= 29
        return False

    def valid_format(date_str):
        date_parts = date_str.split('-')
        return len(date_parts) == 3 and len(date_parts[0]) == 2 and len(date_parts[1]) == 2 and len(
            date_parts[2]) == 4

    if not date:
        return False

    date_parts = date.split('-')

    if not valid_format(date) or not valid_month(int(date_parts[0])) or not valid_days(int(date_parts[0]),
                                                                                       int(date_parts[1])):
        return False

    return True
