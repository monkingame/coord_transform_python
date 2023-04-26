# -*- coding: utf-8 -*-

# 读取excel坐标列
# 以整理后的文件格式为准，即地理经度、地理维度排序（之前是维度、经度）

import pandas as pd
import coordTransform_utils as util
# import openpyxl
import csv
import os

# excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230425-数据\20230425-坐标分别整理\2-整理\1-599-百度坐标系.xlsx'
# excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230425-数据\20230425-坐标分别整理\2-整理\1200-1799-百度坐标系-2.xlsx'

excel_dir=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230426-数据\坐标-整理'
filenames=['1-599.xlsx',
           '600-1199.xlsx',
           '1200-1799.xlsx',
           '1800-2399.xlsx',
           '2400-2999.xlsx',
           '3000-3599.xlsx',
           '3600-4229.xlsx',
           '唯一编码20148-21196.xlsx']


# df = pd.read_excel(excel_path,
#                    usecols=['经营店铺名称','唯一编码', '地理经度', '地理纬度','lng','lat'],
#                    converters={'唯一编码':str},)

# wb = openpyxl.load_workbook(excel_path)
# ws = wb.active


# line_count=df.shape[0]
# print(df.head())


for index, file_name in enumerate(filenames):
    data=[]
    file_path=f'{excel_dir}\\{file_name}'
    # print(filepath)

    if os.path.isfile(file_path):
        # print('Yes!文件存在')
        df = pd.read_excel(file_path,converters={'唯一编码':str})

        for index,row in df.iterrows():
            name=row['经营店铺名称']
            id=row['唯一编码']
            lng=row['地理经度']
            lat=row['地理纬度']

            if not pd.isna(id) and not pd.isna(lng) and not pd.isna(lat):
                data.append([f'{id},{lng},{lat}'])

        print(file_name,len(data))

        with open(f'{excel_dir}\\all_coord.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            # pass

    else:
        print('文件不存在')

# df.to_excel(excel_path, index=False)


# with open(r'C:\Users\sun\Downloads\1200-1799.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#     # pass

