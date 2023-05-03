# -*- coding: utf-8 -*-

# 比较两个文件是否一致

import pandas as pd
import coordTransform_utils as util


# path_left=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-6.xlsx'
# path_right=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-8.xlsx'

path_left=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-8.xlsx'
path_right=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-9.xlsx'


df_left = pd.read_excel(path_left,converters={'唯一编码':str})
df_right = pd.read_excel(path_right,converters={'唯一编码':str})


def find_equals_row(row_left, row_right):
    id_l=row_left['唯一编码']
    id_r=row_right['唯一编码']

    result=same_column(id_l,id_r)
    # print(result)
    if result is not None: return ('唯一编码',*result)

    result=same_column(row_left['经营店铺名称'],row_right['经营店铺名称'])
    if result is not None: return ('经营店铺名称',*result)

    result=same_column(row_left['营业执照名称'],row_right['营业执照名称'])
    if result is not None: return ('营业执照名称',*result)

    result=same_column(row_left['统一社会信用代码'],row_right['统一社会信用代码'])
    if result is not None: return ('统一社会信用代码',*result)

    result=same_column(row_left['法人名称'],row_right['法人名称'])
    if result is not None: return ('法人名称',*result)

    result=same_column(row_left['法人手机号'],row_right['法人手机号'])
    if result is not None: return ('法人手机号',*result)

    result=same_column(row_left['法人身份证号码'],row_right['法人身份证号码'])
    if result is not None: return ('法人身份证号码',*result)

    result=same_column(row_left['食品经营许可证编码'],row_right['食品经营许可证编码'])
    if result is not None: return ('食品经营许可证编码',*result)

    result=same_column(row_left['营业类型（例如：个人，个体户，企业）'],row_right['营业类型（例如：个人，个体户，企业）'])
    if result is not None: return ('营业类型（例如：个人，个体户，企业）',*result)

    result=same_column(row_left['行业类型（必吃烧烤、鲁菜鲁味、酒店住宿、景点游玩、淄博好品、苍蝇小馆、博山菜、十大人气榜单）'],row_right['行业类型（必吃烧烤、鲁菜鲁味、酒店住宿、景点游玩、淄博好品、苍蝇小馆、博山菜、十大人气榜单）'])
    if result is not None: return ('行业类型（必吃烧烤、鲁菜鲁味、酒店住宿、景点游玩、淄博好品、苍蝇小馆、博山菜、十大人气榜单）',*result)

    result=same_column(row_left['店铺联系人'],row_right['店铺联系人'])
    if result is not None: return ('店铺联系人',*result)

    result=same_column(row_left['联系邮箱'],row_right['联系邮箱'])
    if result is not None: return ('联系邮箱',*result)

    result=same_column(row_left['店铺联系方式（座机）'],row_right['店铺联系方式（座机）'])
    if result is not None: return ('店铺联系方式（座机）',*result)

    result=same_column(row_left['店铺联系方式（手机号）'],row_right['店铺联系方式（手机号）'])
    if result is not None: return ('店铺联系方式（手机号）',*result)

    result=same_column(row_left['区县'],row_right['区县'])
    if result is not None: return ('区县',*result)

    result=same_column(row_left['详细地址'],row_right['详细地址'])
    if result is not None: return ('详细地址',*result)

    # 如果经纬度小数点后超过了10位，那么表示的精度已经高到超出实际需要的范围，
    # 因为地球的直径约为12,742公里，在10位小数点的精度下，每个位置的误差已经小于一毫米。
    # 因此，小数点后超过10位的经纬度已经超出了实际需要的精度范围，而且这样高精度的数据通常也难以收集和处理。
    # 在一般情况下，经纬度的小数点后保留6位，精确到小数点后的第6位。
    # 这意味着经度和纬度的精确度为约10米。如果保留更多的小数位，则精度会更高，可以表示更精确的地理位置。
    # 一般来说，经纬度保留小数点后7位已经足够了，能够满足大多数应用场景的需求。
    # 这个精度约为10米左右，可以满足大多数位置标识和导航的需要。

    result=same_column(row_left['地理经度'],row_right['地理经度'])
    if result is not None:
        # print(abs(result[0]-result[1]))
        if abs(result[0]-result[1]) < 1e-8:
            return None
        else:
            return ('地理经度',*result)

    result=same_column(row_left['地理纬度'],row_right['地理纬度'])
    if result is not None: 
        if abs(result[0]-result[1]) < 1e-8:
            return None
        else:
            return ('地理纬度',*result)

    result=same_column(row_left['是否是人气商家'],row_right['是否是人气商家'])
    if result is not None: return ('是否是人气商家',*result)

    result=same_column(row_left['是否在推荐榜单'],row_right['是否在推荐榜单'])
    if result is not None: return ('是否在推荐榜单', *result)

    result=same_column(row_left['评分（满分5分）'],row_right['评分（满分5分）'])
    if result is not None: return ('评分（满分5分）',*result)

    result=same_column(row_left['唯一编码'],row_right['唯一编码'])
    if result is not None: return ('唯一编码', *result)

    result=same_column(row_left['店铺LOGO'],row_right['店铺LOGO'])
    if result is not None: return ('店铺LOGO', *result)

    result=same_column(row_left['门头照片'],row_right['门头照片'])
    if result is not None: return ('门头照片', *result)

    result=same_column(row_left['经营场所内照片'],row_right['经营场所内照片'])
    if result is not None: return ('经营场所内照片', *result)

    result=same_column(row_left['详细地址'],row_right['详细地址'])
    if result is not None: return ('详细地址', *result)

    result=same_column(row_left['经营店铺名称-原始备份'],row_right['经营店铺名称-原始备份'])
    if result is not None: return ('经营店铺名称-原始备份', *result)

    result=same_column(row_left['lat'],row_right['lat'])
    if result is not None: return ('lat', *result)

    result=same_column(row_left['lng'],row_right['lng'])
    if result is not None: return ('lng', *result)

    result=same_column(row_left['子类'],row_right['子类'])
    if result is not None: return ('子类', *result)

    result=same_column(row_left['简介'],row_right['简介'])
    if result is not None: return ('简介', *result)

    result=same_column(row_left['特色'],row_right['特色'])
    if result is not None: return ('特色', *result)

    result=same_column(row_left['营业时间'],row_right['营业时间'])
    if result is not None: return ('营业时间', *result)

    result=same_column(row_left['外部链接'],row_right['外部链接'])
    if result is not None: return ('外部链接', *result)

    result=same_column(row_left['删除标志'],row_right['删除标志'])
    if result is not None: return ('删除标志', *result)

    result=same_column(row_left['数据版本'],row_right['数据版本'])
    if result is not None: return result

    result=same_column(row_left['一店一码'],row_right['一店一码'])
    if result is not None: return result

    result=same_column(row_left['数据来源'],row_right['数据来源'])
    if result is not None: return result
    
    return None


def same_column(v_l,v_r):
    if  pd.isna(v_l) and pd.isna(v_r):
        return None
    # return v_l==v_r

    if v_l==v_r:
        return None
    else:
        return (v_l,v_r)

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

print(len(map_left),len(map_right))

count=0
for key in map_left.keys():
    # print(find_equals(map_left[key],map_right[key]))
    v_left=map_left.get(key)
    v_right=map_right.get(key)
    is_same=find_equals_row(v_left,v_right)
    # print(same)
    if  is_same is not None:
        # print(key,v_left['经营店铺名称'])
        print(key,v_left['经营店铺名称'],is_same)
        count = count+1

print(count)

