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

    months_31 = ['01', '03', '05', '07', '08', '10', '12']
    months_30 = ['04', '06', '09', '11']
    months_29 = ['02']

    if date == '':
        return False
    if '-' not in date:
        return False

    if date[0:2] not in months_31 + months_30 + months_29:
        return False
    if date[3:5] not in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                         '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']:
        return False
    if date[6:10] not in ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001',
                          '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
                          '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024',
                          '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035',
                          '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046',
                          '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057',
                          '2058', '
