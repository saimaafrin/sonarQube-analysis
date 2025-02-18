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


    # Check if the date is in the format: mm-dd-yyyy
    if len(date) == 10 and date[2] == "-" and date[5] == "-":
        months = int(date[0:2])
        days = int(date[3:5])
        years = int(date[6:10])

        if years >= 1900 and years <= 2100:
            if months >= 1 and months <= 12:
                if months == 1 or months == 3 or months == 5 or months == 7 or months == 8 or months == 10 or months == 12:
                    if days >= 1 and days <= 31:
                        return True
                elif months == 2:
                    if days >= 1 and days <= 29:
                        return True
                elif months == 4 or months == 6 or months == 9 or months == 11:
                    if days >= 1 and days <= 30:
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
