# -*- coding: utf-8 -*-

# 将数据总表excel中的百度地理坐标转换为gcj02坐标，
# 并存回原来的excel文件

import pandas as pd
import coordTransform_utils as util
# import openpyxl
# import csv

# excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230425-数据\20230425-坐标分别整理\2-整理\1-599-百度坐标系.xlsx'
excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230426-数据\坐标-整理\1200-1799-百度坐标系-2.xlsx'

# df = pd.read_excel(excel_path,
#                    usecols=['经营店铺名称','唯一编码', '地理经度', '地理纬度','lng','lat'],
#                    converters={'唯一编码':str},)
df = pd.read_excel(excel_path,converters={'唯一编码':str})

# wb = openpyxl.load_workbook(excel_path)
# ws = wb.active

line_count=df.shape[0]
# print(df.head())
# data=[]

for index,row in df.iterrows():
    # name=row['经营店铺名称']
    id=row['唯一编码']
    lng=row['地理经度']
    lat=row['地理纬度']
    # lng_save=row['lng']
    # lat_save=row['lat']

    if not pd.isna(id) and not pd.isna(lng) and not pd.isna(lat):
        # print(index, id,name,lng,lat)
        gcj=util.bd09_to_gcj02(lng,lat)
        # print(index, id,name,baidu[0],baidu[1])
        df.at[index, '地理经度'] = gcj[0]
        df.at[index, '地理纬度'] = gcj[1]
        # if index<100:
        #     print(id,name,gcj[0],gcj[1],lng,lat)
        # data.append([f'{id},{gcj[0]},{gcj[1]}'])

df.to_excel(excel_path, index=False)

# print(len(data))

# with open(r'C:\Users\sun\Downloads\1200-1799.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#     # pass

