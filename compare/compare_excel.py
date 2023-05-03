# -*- coding: utf-8 -*-

# 比较两个文件是否一致

import pandas as pd
from find_same_row_column import find_equals_row
import dict_operation as dop

# path_left=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-6.xlsx'
# path_right=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-8.xlsx'

path_left=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-6.xlsx'
path_right=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-8.xlsx'

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

# dict_intersection=
keys_intersection=dop.get_intersection_keys(map_left,map_right)
print(len(keys_intersection))
# set_left=dop.get_set_difference_keys(map_left,keys_intersection)
# set_right=dop.get_set_difference_keys(map_right,keys_intersection)
# print(len(set_left),len(set_right))

# unique_dict=get_unique_dict(map_left,map_right)
# # print(len(unique_dict))
# for key, value in unique_dict.items():
#     print(key, value['经营店铺名称'])


count=0
for key in map_left.keys():
    # print(find_equals(map_left[key],map_right[key]))
    v_left=map_left.get(key)
    v_right=map_right.get(key)
    is_same=find_equals_row(v_left,v_right)
    # print(same)
    if  is_same is not None:
        # print(key,v_left['经营店铺名称'])
        # print(key,v_left['经营店铺名称'],is_same)
        count = count+1

print('不同数据总量：',count)

