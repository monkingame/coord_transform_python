# -*- coding: utf-8 -*-

# 将目录下一些列数据总表excel文件，导出为csv文件
# 这些文件是手工整理的地理坐标

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
        #    '唯一编码20148-21196.xlsx',
           ]


# df = pd.read_excel(excel_path,
#                    usecols=['经营店铺名称','唯一编码', '地理经度', '地理纬度','lng','lat'],
#                    converters={'唯一编码':str},)

# wb = openpyxl.load_workbook(excel_path)
# ws = wb.active


# line_count=df.shape[0]
# print(df.head())


data=[]

for index, file_name in enumerate(filenames):
    file_path=f'{excel_dir}\\{file_name}'
    # print(filepath)

    if os.path.isfile(file_path):
        # print('Yes!文件存在')
        df = pd.read_excel(file_path,converters={'唯一编码':str})
        df = df.fillna('')

        for index,row in df.iterrows():
            name=row['经营店铺名称'].replace(',','')
            region=row['区县'].replace(',','')
            addr=row['详细地址'].replace(',','')
            id=row['唯一编码']
            lng=row['地理经度']
            lat=row['地理纬度']

            if not pd.isna(id) and not pd.isna(lng) and not pd.isna(lat):
                # data.append([f'{id},{lng},{lat},{name}-{region}-{addr}'])
                data.append([f'{id},{lng},{lat}'])

        print(file_name,len(data))

        # with open(csv_file_path, 'a', newline='',encoding='utf-8') as file:
        #     writer = csv.writer(file)
        #     writer.writerows(data)
            # pass

    else:
        print('文件不存在')

print('总行数:',len(data))
# df.to_excel(excel_path, index=False)
csv_file_path = f'{excel_dir}\\all_coord.csv'
# with open(csv_file_path, 'w') as f:
#     f.truncate(0)
#     # print('文件已清空')
with open(csv_file_path, 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    pass

