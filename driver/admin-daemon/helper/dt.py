
import datetime

TIME_FORMAT = "%Y/%m/%d %H-%M-%S.%f %z"
JST = datetime.timezone(datetime.timedelta(hours=9))

def now():
    return datetime.datetime.now(tz=JST).strftime(TIME_FORMAT)
