from datetime import datetime
from datetime import timedelta
import random
from search import Binarysearch

datetimeformat = '%Y-%m-%d %H:%M:%S.%f'
timeformat = '%H:%M:%S.%f'
dateformat = '%Y-%m-%d'
now = datetime.now()


def date():
    curdate = now.strftime(dateformat)
    return curdate
def time():
    curtime = now.strftime(timeformat)
    return curtime
def date_and_time():
    current_login_datetime = now.strftime(datetimeformat)
    return current_login_datetime

