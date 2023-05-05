# -*- coding: utf-8 -*-

# 查重
import io
import sys
sys.path.append("..")

import pandas as pd
# from compare import dict_operation as dop
from compare import dict_operation as dop


path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230505-数据\20230505-淄博本地生活数-3.xlsx'
df = pd.read_excel(path,converters={'唯一编码':str,'一店一码':str,'数据版本':str})

map={}

for index,row in df.iterrows():
    id=row['唯一编码']
    name=row['经营店铺名称']
    deleted=row['删除标志']
    # print(id,name)
    # print(deleted)
    # 注意删除标志 不为空则应该删除（一般是Y）
    if not pd.isna(id) and pd.isna(deleted):
        # df[id]=row
        map[id]=name

# names=list(set(map.values()))
names=list(map.values())
# print(names)


# 在打开文件时，指定编码方式为utf-8
with io.open(r'C:\Users\sun\Downloads\test\1.txt', 'w', encoding='utf-8') as f:
    for item in names:
        f.write(item + '\n')

