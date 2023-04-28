# -*- coding: utf-8 -*-

# 根据店铺名称获取唯一编码

import pandas as pd
import coordTransform_utils as util

excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230428-数据\20230428-淄博本地生活数据-5.xlsx'

df = pd.read_excel(excel_path,converters={'唯一编码':str})
df = df.fillna('')

data=[]

for index,row in df.iterrows():
    id=row['唯一编码']
    name=row['经营店铺名称'].replace(',','').strip()
    region=row['区县'].replace(',','').strip()
    addr=row['详细地址'].replace(',','').strip()
    
    # if not pd.isna(id) and not pd.isna(lng) and not pd.isna(lat):
    #     # data.append([f'{id} {name} {region} {addr}'])
    #     data.append([f'{id} {name} {region} {addr}'])
    if not pd.isna(id) and not pd.isna(id):
        data.append([f'{id} {name} {region} {addr}'])

print(len(data))


