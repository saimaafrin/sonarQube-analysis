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

    import re

    # 1. The date string is not empty.
    if not date:
        return False

    # 2. The number of days is not less than 1 or higher than 31 days for
    # months 1,3,5,7,8,10,12. And the number of days is not less than 1 or
    # higher than 30 days for months 4,6,9,11. And, the number of days is not
    # less than 1 or higher than 29 for the month 2.
    m, d, y = re.split(r'[-\/]', date)

    if len(m) != 2 or len(d) != 2 or len(y) != 4:
        return False

    m = int(m)
    d = int(d)
    y = int(y)

    if not (1 <= m <= 12) or not (1 <= d <= 31):
        return False

    if (
            m in (1, 3, 5, 7, 8, 10, 12)
            and not (1 <= d <= 31)
    ) or (
            m in (4, 6, 9, 11)
            and not (1 <= d <= 30)
    ):
        return False

    if m == 2 and not (1 <= d <= 29):
        return False

    # 3. The months should not be less than 1 or higher than 12.
    # 4. The date should be in the format: mm-dd-yyyy
    if not re.match(r'^\d\d-\d\d-\d\d\d\d$', date):
        return False

    return True
