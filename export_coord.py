# -*- coding: utf-8 -*-

# 将数据总表excel文件中的店铺名称及坐标导出，
# 并保存为csv文件，便于处理

import pandas as pd
import coordTransform_utils as util
import csv

excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230427-数据\20230427-淄博本地生活数据-6.xlsx'

df = pd.read_excel(excel_path,converters={'唯一编码':str})
df = df.fillna('')

data=[]

for index,row in df.iterrows():
    id=row['唯一编码']
    name=row['经营店铺名称'].replace(',','').strip()
    lng=row['地理经度']
    lat=row['地理纬度']

    if not pd.isna(id) and not pd.isna(lng) and not pd.isna(lat):
        # data.append([f'{id},{name},{lng},{lat}'])
        data.append([id,name,lng,lat])

print(len(data))

# print(data)

with open(r'C:\Users\sun\Downloads\id_name_coord.csv', 'w', newline='',encoding='utf-8') as file:
    # writer = csv.writer(file,
    #                     quoting=csv.QUOTE_NONE,delimiter='|', quotechar='"')
    writer = csv.writer(file)
    writer.writerows(data)

