# -*- coding: utf-8 -*-

# 比较两个文件是否一致

import pandas as pd
from find_same_row_column import find_equals_row
import dict_operation as dop

# path_left=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-6.xlsx'
# path_right=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-8.xlsx'

path_left=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-6.xlsx'
path_right=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230503-数据\20230503-淄博本地生活数-1.xlsx'

df_left = pd.read_excel(path_left,converters={'唯一编码':str,'一店一码':str,'数据版本':str})
df_right = pd.read_excel(path_right,converters={'唯一编码':str,'一店一码':str,'数据版本':str})


map_left={}
map_right={}

for index,row in df_left.iterrows():
    id=row['唯一编码']
    # name=row['经营店铺名称']
    if not pd.isna(id):
        # if not row.equals(df_right.iloc[index]):
        map_left[id]=row

for index,row in df_right.iterrows():
    id=row['唯一编码']
    # name=row['经营店铺名称']
    if not pd.isna(id):
        map_right[id]=row

print('两个表各自数量：',len(map_left),len(map_right))

# 将两个表再取交集，保证对比时大小完全相等
# keys交集
keys_intersection=dop.get_intersection_keys(map_left,map_right)

# 相同keys部分
intersect_left=dop.filter_dict_by_keys(map_left,keys_intersection)
intersect_right=dop.filter_dict_by_keys(map_right,keys_intersection)
print('经筛选唯一编码相同数量：',len(intersect_left),len(intersect_right))
# print(dop.is_dict_keys_equal(remain_left,remain_right))

count=0
for key in intersect_left.keys():
    v_left=intersect_left.get(key)
    v_right=intersect_right.get(key)
    compare=find_equals_row(v_left,v_right)
    if  compare is not None:
        # print(key,v_left['经营店铺名称'],compare)
        count = count+1

print('唯一编码相同，但该行数据不同的总量：',count)


print('=====================================')

# 分别不同的部分
diff_left=dop.get_difference(map_left,keys_intersection)
diff_right=dop.get_difference(map_right,keys_intersection)
print('各自多余数量：',len(diff_left),len(diff_right))

print('前者特有数据')
for key,value in diff_left.items():
    # print(key,value['经营店铺名称'])
    pass

print('后者特有数据')
for key,value in diff_right.items():
    # print(key,value['经营店铺名称'])
    pass


