import datetime


def now():
    return datetime.date.today()


def begin_of_week(date):
    weekday = date.weekday()
    delta = datetime.timedelta(days=weekday)
    return date - delta


def weekday(date):
    return date.weekday() + 2


def week_date_range(date):
    begin = begin_of_week(date)
    return (begin, begin + datetime.timedelta(days=6))


def from_date(date):
    return date.strftime("%d.%m.%Y")
