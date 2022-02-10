import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def print_full(x):
    pd.set_option('display.max_rows', len(x))
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


def to_float(df1, col_name1, col_name2):
    """
    修改类型，并且替换字段名
    """
    df1[col_name2] = [0 if x == "" else float(x) for x in df1[col_name1]]
    df1.pop(col_name1)
    return df1


def to_int(df1, col_name1, col_name2):
    """
    修改类型，并且替换字段名
    """
    df1[col_name2] = [0 if x == "" else int(x) for x in df1[col_name1]]
    df1.pop(col_name1)
    return df1
