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


    # This function will check for the format of the date
    def check_format(date_str):
        date_format = "mm-dd-yyyy"
        if len(date_str) != len(date_format):
            return False
        for x, y in zip(date_format, date_str):
            if x != y:
                return False
        return True

    # This function will check if the month and days are valid
    def check_month_days(month, days):
        if (
            month in ["01", "03", "05", "07", "08", "10", "12"]
            and not 1 <= int(days) <= 31
        ):
            return False
        if (
            month in ["04", "06", "09", "11"]
            and not 1 <= int(days) <= 30
        ):
            return False
        if month == "02" and not 1 <= int(days) <= 29:
            return False
        return True

    # This function will check if the date is in the format mm-dd-yyyy
    if not check_format(date):
        return False

    # This function will check if the month is valid
    month, days, year = date.split("-")
    if not 1 <= int(month) <= 12:
        return False

    # This function will check if the day is valid
    if not check_month_days(month, days):
        return False

    return True
