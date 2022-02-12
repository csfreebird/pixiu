from datetime import date, timedelta

import pymongo


def get_date_range(days=-6):
    """
    获取今天以及之前n天(默认为前6天)的日期作为日期范围,
    返回形式如2022-01-01, 2022-01-06
    """
    today = date.today()
    delta = timedelta(days)
    start = today + delta
    return str(start), str(today)


def get_fin_report_dates():
    """
    获得财报日期
    """
    start_year = 2011
    today = date.today()
    this_year = today.year
    report_dates = []
    for y in range(start_year, this_year+1):
        report_dates.append('{}-03-31'.format(y))
        report_dates.append('{}-06-30'.format(y))
        report_dates.append('{}-09-30'.format(y))
        report_dates.append('{}-12-31'.format(y))
    return report_dates


def get_report_dates():
    '''
    分红报告日期
    找到当前日期最近的12-31和06-30的20次日期(10年)
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
        d11 = '{:d}-12-31'.format(this_year-6)
        d13 = '{:d}-12-31'.format(this_year-7)
        d15 = '{:d}-12-31'.format(this_year-8)
        d17 = '{:d}-12-31'.format(this_year-9)
        d19 = '{:d}-12-31'.format(this_year-10)
    d2 = '{:d}-06-30'.format(this_year)
    if d2 > today_str:
        d2 = '{:d}-06-30'.format(this_year-1)
        d4 = '{:d}-06-30'.format(this_year-2)
        d6 = '{:d}-06-30'.format(this_year-3)
        d8 = '{:d}-06-30'.format(this_year-4)
        d10 = '{:d}-06-30'.format(this_year-5)
        d12 = '{:d}-06-30'.format(this_year-6)
        d14 = '{:d}-06-30'.format(this_year-7)
        d16 = '{:d}-06-30'.format(this_year-8)
        d18 = '{:d}-06-30'.format(this_year-9)
        d20 = '{:d}-06-30'.format(this_year-10)
    return [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20]


def get_latest_day(tbl):
    docs = tbl.find({}).sort([('日期', pymongo.DESCENDING)]).limit(1)
    return docs[0]['日期']
