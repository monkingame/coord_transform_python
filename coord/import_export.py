# -*- coding: utf-8 -*-

# 导入委办局或12345投诉的数据，
# 并导入到模板中
# 作废，暂时不用了

import pandas as pd
import coordTransform_utils as util

path_import=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230427-数据\20230427-外部数据更新-12345投诉-1.xlsx'
path_export=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230427-数据\20230427-总表数据模板.xlsx'

# excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230425-数据\20230425-坐标分别整理\2-整理\1-599-百度坐标系.xlsx'
# excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230425-数据\20230425-坐标分别整理\2-整理\1200-1799-百度坐标系-2.xlsx'


df_import = pd.read_excel(path_import,converters={'唯一编码':str})
df_import = df_import.fillna('')

data=[]

for index,row in df_import.iterrows():
    name=row['经营店铺名称']
    id=row['唯一编码']
    lng=row['地理经度']
    lat=row['地理纬度']

    if not pd.isna(id) and not pd.isna(lng) and not pd.isna(lat):
        # print(index, id,name,lng,lat)
        gcj=util.bd09_to_gcj02(lng,lat)
        # print(index, id,name,baidu[0],baidu[1])
        df_import.at[index, 'lng'] = gcj[0]
        df_import.at[index, 'lat'] = gcj[1]
        # if index<100:
        #     print(id,name,gcj[0],gcj[1],lng,lat)
        data.append([f'{id},{gcj[0]},{gcj[1]}'])

# df.to_excel(excel_path, index=False)

print(len(data))
