# -*- coding: utf-8 -*-

# 读取5月1号问卷星数据

import pandas as pd
import coordTransform_utils as util

excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-7.xlsx'

df = pd.read_excel(excel_path,converters={'唯一编码':str,'数据版本':str})

# data=[]

count=0

for index,row in df.iterrows():
    name=row['经营店铺名称']
    id=row['唯一编码']
    uniqueid=row['lat']
    stamp=row['数据版本']
    # print(index)

    if not pd.isna(id) and not pd.isna(uniqueid):
        if stamp == '429':
            count=count+1
            print(count)
        # data.append([f'{id},{lng},{lat}'])
        # print(id,name,uniqueid)
        # print(stamp)
        # print(count)
        # print(stamp=='501')

# df.to_excel(excel_path, index=False)

# print(len(data))
