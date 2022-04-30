import akshare as ak
from pixiu import df


def get_code_pre(code):
    if code.startswith('688'):
        return '688'
    if code.startswith('600'):
        return '600'
    if code.startswith('601'):
        return '601'
    if code.startswith('603'):
        return '603'
    if code.startswith('605'):
        return '605'
    if code.startswith('300'):
        return '300'
    if code.startswith('301'):
        return '301'
    if code.startswith('000'):
        return '000'
    if code.startswith('001'):
        return '001'
    if code.startswith('002'):
        return '002'
    if code.startswith('003'):
        return '003'
    if code.startswith('43'):
        return '43'
    if code.startswith('83'):
        return '83'
    if code.startswith('87'):
        return '87'
    return None


def parse(code):
    """
    根据代码前缀解析出交易所和板块
    当前北交所和新三板暂时放在一起，因为我不太关心小盘股
    """
    if code.startswith('688'):
        return '上海', '科创'
    if code.startswith('600'):
        return '上海', '主板'
    if code.startswith('601'):
        return '上海', '主板'
    if code.startswith('603'):
        return '上海', '主板'
    if code.startswith('605'):
        return '上海', '主板'
    if code.startswith('300'):
        return '深圳', '创业板'
    if code.startswith('301'):
        return '深圳', '创业板'
    if code.startswith('000'):
        return '深圳', '主板'
    if code.startswith('001'):
        return '深圳', '主板'
    if code.startswith('002'):
        return '深圳', '主板'
    if code.startswith('003'):
        return '深圳', '主板'
    if code.startswith('43'):
        return '北京_三板', '新三板'
    if code.startswith('83'):
        return '北京_三板', '新三板'
    if code.startswith('87'):
        return '北京_三板', '新三板'
    else:
        return '', ''


def get_code_for_eastmoney(exchange, code):
    '''
    用于东财资产负载表下载
    '''
    if exchange == '上海':
        return 'SH{}'.format(code)
    if exchange == '深圳':
        return 'SZ{}'.format(code)
    return None


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
