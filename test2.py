# -*- coding: utf-8 -*-

# 读取excel坐标列
# 以整理后的文件格式为准，即地理经度、地理维度排序（之前是维度、经度）

import pandas as pd
import coordTransform_utils as util

excel_path=r'C:\Users\sun\Downloads\坐标-测试.xlsx'

df = pd.read_excel(excel_path,
                   usecols=['经营店铺名称','唯一编码', '地理经度', '地理纬度'],
                   converters={'唯一编码':str},)

line_count=df.shape[0]
# print(df.head())

for index,row in df.iterrows():
    name=row['经营店铺名称']
    id=row['唯一编码']
    lng=row['地理经度']
    lat=row['地理纬度']

    # if pd.isna(id) or (len(id)==0): 
    #     pass
    # else:
    #     # print(index, id,name,lng,lat)
    #     gaode=util.bd09_to_gcj02(lng,lat)
    #     print(index, id,name,gaode[0],gaode[1])
    if not pd.isna(id) and not pd.isna(lng) and not pd.isna(lat):
        print(index, id,name,lng,lat)



