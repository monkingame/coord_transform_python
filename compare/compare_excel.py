# -*- coding: utf-8 -*-

# 比较两个文件是否一致

import pandas as pd
from find_same_row_column import find_equals_row
import dict_operation as dop

# path_left=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-6.xlsx'
# path_right=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-8.xlsx'

path_left=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-8.xlsx'
path_right=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-6.xlsx'

df_left = pd.read_excel(path_left,converters={'唯一编码':str,'一店一码':str,'数据版本':str})
df_right = pd.read_excel(path_right,converters={'唯一编码':str,'一店一码':str,'数据版本':str})


map_left={}
map_right={}

for index,row in df_left.iterrows():
    id=row['唯一编码']
    # name=row['经营店铺名称']
    # print(index)
    if not pd.isna(id):
        # if not row.equals(df_right.iloc[index]):
        #     # print(index)
        #     count=count+1
        map_left[id]=row

for index,row in df_right.iterrows():
    id=row['唯一编码']
    # name=row['经营店铺名称']
    if not pd.isna(id):
        map_right[id]=row

print('两个表各自数量：',len(map_left),len(map_right))

# 将两个表再取交集，保证对比时大小完全相等
keys_intersection=dop.get_intersection_keys(map_left,map_right)
# print(len(keys_intersection))
remain_left=dop.filter_dict_by_keys(map_left,keys_intersection)
remain_right=dop.filter_dict_by_keys(map_right,keys_intersection)
# print(len(map_left),len(map_right))
# print(dop.is_dict_keys_equal(map_left,map_right))


count=0
for key in remain_left.keys():
    # print(find_equals(map_left[key],map_right[key]))
    v_left=remain_left.get(key)
    v_right=map_right.get(key)
    compare=find_equals_row(v_left,v_right)
    # print(same)
    if  compare is not None:
        print(key,v_left['经营店铺名称'],compare)
        count = count+1

print('不同数据总量：',count)

