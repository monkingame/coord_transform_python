# -*- coding: utf-8 -*-

# 比较两个文件是否一致

import pandas as pd
import coordTransform_utils as util


path_left=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-6.xlsx'
df_left = pd.read_excel(path_left,converters={'唯一编码':str})

path_right=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-8.xlsx'
df_right = pd.read_excel(path_right,converters={'唯一编码':str})


def find_equals_row(row_left, row_right):
    id_l=row_left['唯一编码']
    id_r=row_right['唯一编码']

    result=same_column(id_l,id_r)
    # print(result)
    if result is not None: return result

    result=same_column(row_left['经营店铺名称'],row_right['经营店铺名称'])
    if result is not None: return result

    result=same_column(row_left['营业执照名称'],row_right['营业执照名称'])
    if result is not None: return result

    result=same_column(row_left['统一社会信用代码'],row_right['统一社会信用代码'])
    if result is not None: return result

    result=same_column(row_left['法人名称'],row_right['法人名称'])
    if result is not None: return result

    result=same_column(row_left['法人手机号'],row_right['法人手机号'])
    if result is not None: return result

    result=same_column(row_left['法人身份证号码'],row_right['法人身份证号码'])
    if result is not None: return result

    result=same_column(row_left['食品经营许可证编码'],row_right['食品经营许可证编码'])
    if result is not None: return result

    result=same_column(row_left['营业类型（例如：个人，个体户，企业）'],row_right['营业类型（例如：个人，个体户，企业）'])
    if result is not None: return result

    result=same_column(row_left['行业类型（必吃烧烤、鲁菜鲁味、酒店住宿、景点游玩、淄博好品、苍蝇小馆、博山菜、十大人气榜单）'],row_right['行业类型（必吃烧烤、鲁菜鲁味、酒店住宿、景点游玩、淄博好品、苍蝇小馆、博山菜、十大人气榜单）'])
    if result is not None: return result

    result=same_column(row_left['店铺联系人'],row_right['店铺联系人'])
    if result is not None: return result

    result=same_column(row_left['联系邮箱'],row_right['联系邮箱'])
    if result is not None: return result

    result=same_column(row_left['店铺联系方式（座机）'],row_right['店铺联系方式（座机）'])
    if result is not None: return result

    result=same_column(row_left['店铺联系方式（手机号）'],row_right['店铺联系方式（手机号）'])
    if result is not None: return result

    result=same_column(row_left['区县'],row_right['区县'])
    if result is not None: return result

    result=same_column(row_left['详细地址'],row_right['详细地址'])
    if result is not None: return result

    # if not same_column(id_l,id_r):return False
    # if not same_column(row_left['经营店铺名称'],row_right['经营店铺名称']):return False
    # if not same_column(row_left['营业执照名称'],row_right['营业执照名称']):return False
    # if not same_column(row_left['统一社会信用代码'],row_right['统一社会信用代码']):return False
    # if not same_column(row_left['法人名称'],row_right['法人名称']):return False
    # if not same_column(row_left['法人手机号'],row_right['法人手机号']):return False
    # if not same_column(row_left['法人身份证号码'],row_right['法人身份证号码']):return False
    # if not same_column(row_left['食品经营许可证编码'],row_right['食品经营许可证编码']):return False
    # if not same_column(row_left['营业类型（例如：个人，个体户，企业）'],row_right['营业类型（例如：个人，个体户，企业）']):return False
    # if not same_column(row_left['行业类型（必吃烧烤、鲁菜鲁味、酒店住宿、景点游玩、淄博好品、苍蝇小馆、博山菜、十大人气榜单）'],row_right['行业类型（必吃烧烤、鲁菜鲁味、酒店住宿、景点游玩、淄博好品、苍蝇小馆、博山菜、十大人气榜单）']):return False
    # if not same_column(row_left['店铺联系人'],row_right['店铺联系人']):return False
    # if not same_column(row_left['联系邮箱'],row_right['联系邮箱']):return False
    # if not same_column(row_left['店铺联系方式（座机）'],row_right['店铺联系方式（座机）']):return False
    # if not same_column(row_left['店铺联系方式（手机号）'],row_right['店铺联系方式（手机号）']):return False
    # if not same_column(row_left['区县'],row_right['区县']):return False
    # if not same_column(row_left['详细地址'],row_right['详细地址']):return False
    # if not same_column(row_left['地理经度'],row_right['地理经度']):return False
    # if not same_column(row_left['地理纬度'],row_right['地理纬度']):return False
    
    return None


def same_column(v_l,v_r):
    if  pd.isna(v_l) and pd.isna(v_r):
        return None
    # return v_l==v_r

    if v_l==v_r:
        return None
    else:
        return (v_l,v_r)

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
    is_same=find_equals_row(v_left,v_right)
    # print(same)
    if  is_same is not None:
        # print(key,v_left['经营店铺名称'])
        print(is_same)
        count = count+1

print(count)

