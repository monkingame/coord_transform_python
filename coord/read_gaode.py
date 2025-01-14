# -*- coding: utf-8 -*-

# 将数据总表excel文件，导出为csv文件

import pandas as pd
import coordTransform_utils as util
# import openpyxl
import csv

# excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230425-数据\20230425-坐标分别整理\2-整理\1-599-百度坐标系.xlsx'
excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230425-数据\20230425-坐标分别整理\2-整理\3600-4229.xlsx'

# df = pd.read_excel(excel_path,
#                    usecols=['经营店铺名称','唯一编码', '地理经度', '地理纬度','lng','lat'],
#                    converters={'唯一编码':str},)
df = pd.read_excel(excel_path,converters={'唯一编码':str})

# wb = openpyxl.load_workbook(excel_path)
# ws = wb.active

line_count=df.shape[0]
# print(df.head())

data=[]


for index,row in df.iterrows():
    name=row['经营店铺名称']
    id=row['唯一编码']
    lng=row['地理经度']
    lat=row['地理纬度']
    lng_save=row['lng']
    lat_save=row['lat']

    if not pd.isna(id) and not pd.isna(lng) and not pd.isna(lat):
        # gcj=util.bd09_to_gcj02(lng,lat)
        # df.at[index, 'lng'] = gcj[0]
        # df.at[index, 'lat'] = gcj[1]
        data.append([f'{id},{lng},{lat}'])

# df.to_excel(excel_path, index=False)

print(len(data))

with open(r'C:\Users\sun\Downloads\3600-4229.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    # pass

