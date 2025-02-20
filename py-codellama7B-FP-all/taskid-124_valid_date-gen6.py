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

    month, day, year = date_list
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False

    if len(month) != 2 or len(day) != 2 or len(year) != 4:
        return False

    if month < "01" or month > "12":
        return False

    if day < "01" or day > "31":
        return False

    if year < "1970" or year > "2050":
        return False

    month_int = int(month)
    day_int = int(day)
    year_int = int(year)
    days_in_month = days_in_month(month_int, year_int)
    if day_int > days_in_month:
        return False

    return True
