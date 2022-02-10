import akshare as ak
from pixiu import df


class Stock:
    def __init__(self, code, name, exchange, bankuai):
        self.code = code
        self.name = name
        self.exchange = exchange
        self.bankuai = bankuai

    def get_code(self):
        if self.exchange == '上海':
            return 'sh.{}'.format(self.code)
        if self.exchange == '深圳':
            return 'sz.{}'.format(self.code)
        return None


def remove_prefix(code):
    """
    去除代码中的sh.和sz.前缀
    """
    return code.replace('sh.', '').replace('sz.', '')


def get_price_from_eastmoney(stock, start, end):
    """
    获取前复权数据, akshare东财接口,更及时，更准确
    start, end参数日期格式: '2020-01-12'
    """
    df1 = ak.stock_zh_a_hist(symbol=stock.code, period="daily", start_date=start.replace('-', ''), end_date=end.replace('-', ''), adjust="qfq")
    print(df1)
    df.to_float(df1, '开盘', '开盘价')
    df.to_float(df1, '最高', '最高价')
    df.to_float(df1, '最低', '最低价')
    df.to_float(df1, '收盘', '收盘价')
    df1['代码'] = remove_prefix(stock.code)
    df1['简称'] = stock.name
    df1['交易所'] = stock.exchange
    df1['板块'] = stock.bankuai
    return df1
