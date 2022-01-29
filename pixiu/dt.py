from datetime import date, timedelta


def get_date_range(days=-6):
    """
    获取今天以及之前n天(默认为前6天)的日期作为日期范围,
    返回形式如2022-01-01, 2022-01-06
    """
    today = date.today()
    delta = timedelta(days)
    start = today + delta
    return str(start), str(today)


def get_report_dates():
    '''
    找到当前日期最近的12-31和06-30的10次日期(5年)
    '''
    today = date.today()
    today_str = str(today)
    this_year = today.year
    d1 = '{:d}-12-31'.format(this_year)
    if d1 > today_str:
        d1 = '{:d}-12-31'.format(this_year-1)
        d3 = '{:d}-12-31'.format(this_year-2)
        d5 = '{:d}-12-31'.format(this_year-3)
        d7 = '{:d}-12-31'.format(this_year-4)
        d9 = '{:d}-12-31'.format(this_year-5)
    d2 = '{:d}-06-30'.format(this_year)
    if d2 > today_str:
        d2 = '{:d}-06-30'.format(this_year-1)
        d4 = '{:d}-06-30'.format(this_year-2)
        d6 = '{:d}-06-30'.format(this_year-3)
        d8 = '{:d}-06-30'.format(this_year-4)
        d10 = '{:d}-06-30'.format(this_year-5)
    return [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
