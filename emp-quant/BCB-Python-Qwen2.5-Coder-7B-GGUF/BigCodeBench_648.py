
from dateutil.parser import parse
from datetime import timedelta

def task_func(date_str):
    date_obj = parse(date_str)
    while date_obj.weekday() >= 5:  # 5 and 6 represent Saturday and Sunday respectively
        date_obj += timedelta(days=1)
    return date_obj