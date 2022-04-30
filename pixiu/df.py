import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def is_none(v):
    if v != v:
        return True
    if v is None:
        return True
    return False


def print_full(x, num_rows=None):
    if num_rows is None:
        pd.set_option('display.max_rows', len(x))
    else:
        pd.set_option('display.max_rows', num_rows)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')


def to_float_money(e):
    """
    如果值无效，默认为0.0
    如果包含'--'等表示空置的字符，默认为0.0
    如果包含单位元或者','符号，去除掉
    如果本身就是float类型，直接返回
    """
    if is_none(e):
        return 0.0
    if isinstance(e, float):
        return e
    str = e.replace('元', '').replace(',', '').replace('，', '')
    if str in ['--', '-', '', '-']:
        return 0.0
    return float(str)


def to_float(df1, col_name1, col_name2):
    """
    简单版本的修改字段类型
    修改类型，并且替换字段名
    """
    df1[col_name2] = [0 if x == "" else float(x) for x in df1[col_name1]]
    if col_name1 != col_name2:
        df1.pop(col_name1)
    return df1


def percent_to_float(e):
    v = to_float_money(e)
    return v / 100.0


def to_date_str(df, column_name):
    """
    将datetime.datetime类型转换成类似"2020-01-02"的日期字符串
    """
    df[column_name] = df[column_name].map(lambda e: str(e.date()))
    return df


def to_date_str2(df, column_name):
    """
    将datetime.date类型转换成类似"2020-01-02"的日期字符串
    """
    df[column_name] = df[column_name].map(lambda e: str(e))
    return df


def linear_predict(row, data_cols, new_col_name):
    """
    用于dataframe.apply
    data_cols是字段名称列表，包含了该行含有用于线性回归训练的数据
    new_col_name是预测下一个值存放的字段名称
    """
    x = []
    i = 0
    for e in data_cols:
        x.append(i)
        i += 1
    x = np.array(x).reshape((-1, 1))
    y = row[data_cols]
    model = LinearRegression()
    model.fit(x, y)
    y_new = model.predict([max(x) + 1])
    row[new_col_name] = y_new[0]
    return row


def sumColumns(self, rowStart, rowEnd):
    """
    将[rowStart, rowEnd)范围的所有的数值column求和
    @return 返回一个Series对象
    """
    df2 = self.df.iloc[rowStart:rowEnd:]
    sumResult = df2.sum(axis=0, skipna=True)
    return sumResult


def sumColumn(self, rowStart, rowEnd, colName):
    """
    将[rowStart, rowEnd)范围的所有的数值column求和
    @return 返回数值
    """
    df2 = self.df.iloc[rowStart:rowEnd:]
    return sum(df2[colName])


def avgColumn(self, rowStart, rowEnd, colName):
    """
    将[rowStart, rowEnd)范围的所有的数值column求和
    @return 返回一个Series对象
    """
    df2 = self.df.iloc[rowStart:rowEnd:]
    s = 0.0
    for v in df2[colName].values:
        s += v
    return s / len(df2[colName].values)


def to_int(df1, col_name1, col_name2):
    """
    修改类型，并且替换字段名
    """
    df1[col_name2] = [0 if x == "" else int(x) for x in df1[col_name1]]
    df1.pop(col_name1)
    return df1
