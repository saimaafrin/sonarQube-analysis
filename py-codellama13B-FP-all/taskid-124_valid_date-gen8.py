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

    date_formats = ["mm-dd-yyyy", "dd-mm-yyyy", "yyyy-mm-dd"]
    if len(date) < 1:
        return False
    for fmt in date_formats:
        if "-" in fmt:
            splitter = "-"
        else:
            splitter = "/"
        date_parts = date.split(splitter)
        if len(date_parts) != 3:
            continue
        if date_parts[0].isdigit() and date_parts[1].isdigit() and date_parts[2].isdigit():
            year = int(date_parts[2])
            month = int(date_parts[0])
            day = int(date_parts[1])
            if month >= 1 and month <= 12:
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    if day >= 1 and day <= 31:
                        return True
                elif month in [4, 6, 9, 11]:
                    if day >= 1 and day <= 30:
                        return True
                elif month == 2:
                    if year % 4 == 0:
                        if day >= 1 and day <= 29:
                            return True
                    else:
                        if day >= 1 and day <= 28:
                            return True
            break
    return False
