from datetime import datetime, timedelta, time, date
import calendar

def _first_workday_of_month(start, month_number):
    if start.month < month_number:
        year = start.year
    else:
        year = start.year + 1

    first_day = date(year, month_number, 1)
    while first_day.weekday() >= 5:
        first_day += timedelta(days=1)
    result = datetime.combine(first_day, time(8, 0))
    return datetime.isoformat(result)

def _last_workday_of_quarter(start, quarter_number):
    last_month = quarter_number * 3

    if start.month <= last_month:
        year = start.year
    else:
        year = start.year + 1

    last_day_num = calendar.monthrange(year, last_month)[1]
    last_day_date = date(year, last_month, last_day_num)
    while last_day_date.weekday() >= 5:
        last_day_date -= timedelta(days=1)
    result = datetime.combine(last_day_date, time(8, 0))
    return datetime.isoformat(result)

def delivery_date(start, description):
    start = datetime.fromisoformat(start)
    
    if description == "NOW":
        result = start + timedelta(hours=2)
        return datetime.isoformat(result)
    if description == "ASAP" and start.time() < time(13, 0):
        result = datetime.combine(start.date(), time(17,0))
        return datetime.isoformat(result)
    if description == "ASAP" and start.time() >= time(13, 0):
        result = datetime.combine(start.date() + timedelta(days=1), time(13,0))
        return datetime.isoformat(result)
    if description == "EOW" and start.weekday() in {0, 1, 2}:
        result = datetime.combine(start.date() + timedelta(days=4 - start.weekday()), time(17,0))
        return datetime.isoformat(result)
    if description == "EOW" and start.weekday() in {3, 4}:
        result = datetime.combine(start.date() + timedelta(days=6 - start.weekday()), time(20,0))
        return datetime.isoformat(result)
    if description.endswith("M"):
        month_number = int(description[:description.index("M")])
        return _first_workday_of_month(start, month_number)
    if description.startswith("Q"):
        quarter_number = int(description[description.index("Q") + 1:])
        return _last_workday_of_quarter(start, quarter_number)
    return None