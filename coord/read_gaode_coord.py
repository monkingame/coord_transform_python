# -*- coding: utf-8 -*-

# 将数据总表excel文件，导出为csv文件

import pandas as pd
import coordTransform_utils as util
import csv

excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230426-数据\20230426-淄博本地生活数据-5.xlsx'

df = pd.read_excel(excel_path,converters={'唯一编码':str})
df = df.fillna('')

data=[]

for index,row in df.iterrows():
    id=row['唯一编码']
    lng=row['地理经度']
    lat=row['地理纬度']
    name=row['经营店铺名称'].replace(',','').strip()
    region=row['区县'].replace(',','').strip()
    addr=row['详细地址'].replace(',','').strip()
    
    if not pd.isna(id) and not pd.isna(lng) and not pd.isna(lat):
        data.append([f'{id}   {lng},{lat}   {name}-{region}-{addr}'])

# df.to_excel(excel_path, index=False)

print(len(data))

with open(r'C:\Users\sun\Downloads\coord-test.csv', 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    # pass

