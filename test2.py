# -*- coding: utf-8 -*-

# 读取excel坐标列
# 以整理后的文件格式为准，即地理经度、地理维度排序（之前是维度、经度）

import pandas as pd

excel_path=r'C:\Users\sun\Downloads\坐标-测试.xlsx'

df = pd.read_excel(excel_path,
                   usecols=['唯一编码', '地理经度', '地理纬度'],
                   converters={'唯一编码':str})

line_count=df.shape[0]
# print(df.head())

for index,row in df.iterrows():
    # id_str=str(int(row['唯一编码']).fillna(''))
    # id_str = row['唯一编码'].fillna('nan').astype(str)
    id_str=row['唯一编码']
    print(id_str)


# print(len(df.iterrows()))
# print(df.shape[0])
