"""
Author:Viktoria Denys
Program:half_birthday.py
function to compute a half birthday.
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta


def half_birthday(date): # Returns the a date 6 months later--half-birthday!
    """As far as I understand, timedelta only supports days (and weeks),
     while relativedelta adds support for periods defined in terms of years,
     months, weeks or days, as well as defining absolute values for year, month or day. """
    half_birthday_date = date + relativedelta(months=+6)
    return half_birthday_date


if __name__ == '__main__':
    birthday = datetime(2020, 9, 29)
    print(half_birthday(birthday))