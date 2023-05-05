# -*- coding: utf-8 -*-

# 查重

import pandas as pd
from ..compare import dict_operation as dop


path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230505-数据\20230505-淄博本地生活数-3.xlsx'
df = pd.read_excel(path,converters={'唯一编码':str,'一店一码':str,'数据版本':str})

for index,row in df.iterrows():
    id=row['唯一编码']
    name=row['经营店铺名称']
    print(id,name)
    if not pd.isna(id):
        # df[id]=row
        pass

