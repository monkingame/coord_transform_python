# -*- coding: utf-8 -*-

# 市场监督局数据处理

import pandas as pd

excel_read=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230428-数据\未处理-委办局数据\20230428-市场监督局422去重-2.xlsx'
excel_save=r'D:\down\excel\模板.xlsx'

df_reader = pd.read_excel(excel_read)
df_writer = pd.read_excel(excel_save)
# df = pd.read_excel(excel_path,converters={'唯一编码':str})
# df = df.fillna('')
# data=[]

for index,row in df_reader.iterrows():
    name=row['餐饮单位名称']
    addr=row['地址']
    manager=row['负责人']
    tel=row['电话']
    region=row['所在区县']

    # print(name,addr,manager,tel,region)
    df_writer.at[index, '经营店铺名称'] = name
    df_writer.at[index, '经营店铺名称-原始备份'] = name
    df_writer.at[index, '详细地址'] = addr
    df_writer.at[index, '店铺联系人'] = manager
    df_writer.at[index, '店铺联系方式（手机号）'] = tel
    df_writer.at[index, '区县'] = region


# print(len(data))

df_writer.to_excel(excel_save, index=False)
