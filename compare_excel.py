# -*- coding: utf-8 -*-

# 比较两个文件是否一致

import pandas as pd
import coordTransform_utils as util


path_left=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-6.xlsx'
df_left = pd.read_excel(path_left,converters={'唯一编码':str})

path_right=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-8.xlsx'
df_right = pd.read_excel(path_right,converters={'唯一编码':str})



def find_equals_row(pd,row_left, row_right):
    vl=row_left['经营店铺名称']
    vr=row_right['经营店铺名称']

    if same_column(pd,row_left['经营店铺名称'],row_right['经营店铺名称']):
        return True

    if same_column(pd,row_left['经营店铺名称'],row_right['经营店铺名称']):
        return True
    
    if(row_left['经营店铺名称'] != row_right['经营店铺名称']) :
        print(row_left['经营店铺名称'],row_right['经营店铺名称'])
        return False
    if(row_left['法人名称'] != row_right['法人名称']) :
        # print(row_left['法人名称'],row_right['法人名称'])
        return False
    return True


def same_column(pd,v_left,v_right):
    if pd.isnan(v_left) and pd.isnan(v_right):
        return True
    return v_left==v_right

# count=0

map_left={}
map_right={}

for index,row in df_left.iterrows():
    id=row['唯一编码']
    name=row['经营店铺名称']
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

# print(len(map_left),len(map_right))

count=0
for key in map_left.keys():
    # print(find_equals(map_left[key],map_right[key]))
    v_left=map_left.get(key)
    v_right=map_right.get(key)
    same=find_equals_row(v_left,v_right)
    # print(same)
    if not same:
        # print(key,v_left['经营店铺名称'])
        count = count+1


print(count)

