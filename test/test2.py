# -*- coding: utf-8 -*-

# 测试
# 读取excel坐标列
# 以整理后的文件格式为准，即地理经度、地理维度排序（之前是维度、经度）

import pandas as pd
from ..coord import coordTransform_utils as util
# import openpyxl

excel_path=r'C:\Users\sun\Downloads\坐标-测试.xlsx'

# df = pd.read_excel(excel_path,
#                    usecols=['经营店铺名称','唯一编码', '地理经度', '地理纬度','lng','lat'],
#                    converters={'唯一编码':str},)
df = pd.read_excel(excel_path,converters={'唯一编码':str})

# wb = openpyxl.load_workbook(excel_path)
# ws = wb.active

line_count=df.shape[0]
# print(df.head())

for index,row in df.iterrows():
    name=row['经营店铺名称']
    id=row['唯一编码']
    lng=row['地理经度']
    lat=row['地理纬度']
    lng_save=row['lng']
    lat_save=row['lat']

    if not pd.isna(id) and not pd.isna(lng) and not pd.isna(lat):
        # print(index, id,name,lng,lat)
        baidu=util.gcj02_to_bd09(lng,lat)
        # print(index, id,name,baidu[0],baidu[1])
        df.at[index, 'lng'] = baidu[0]
        df.at[index, 'lat'] = baidu[1]

# df.to_excel(excel_path, index=False)


