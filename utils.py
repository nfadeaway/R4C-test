import datetime


def get_last_week_dates():
    today = datetime.datetime.today().date()
    end_week = today - datetime.timedelta(datetime.datetime.weekday(today))
    start_week = end_week - datetime.timedelta(days=7)

    return start_week, end_week
