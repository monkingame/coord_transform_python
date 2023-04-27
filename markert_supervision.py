# -*- coding: utf-8 -*-

# 市场监督局数据处理

import pandas as pd

excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230428-数据\未处理-委办局数据\20230428-市场监督局422去重-2.xlsx'

df = pd.read_excel(excel_path)
# df = pd.read_excel(excel_path,converters={'唯一编码':str})
# df = df.fillna('')

# data=[]

for index,row in df.iterrows():
    name=['餐饮单位名称']
    addr=['地址']
    manager=['负责人']
    tel=['电话']
    region=['所在区县']

    # print(name,addr,manager,tel,region)

# print(len(data))

