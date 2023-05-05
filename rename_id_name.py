# -*- coding: utf-8 -*-

# 根据店铺名称获取唯一编码

import pandas as pd
from coord import coordTransform_utils as util
import os


def find_key_by_value(my_dict, value):
    """
    在字典中查找指定value对应的key，并返回key。
    如果没有找到，返回None。
    """
    for key in my_dict:
        if my_dict[key] == value:
            return key
    return None


excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230428-数据\20230428-淄博本地生活数据-5.xlsx'
df = pd.read_excel(excel_path,converters={'唯一编码':str})
df = df.fillna('')

dict={}

for index,row in df.iterrows():
    id=row['唯一编码']
    name=row['经营店铺名称'].replace(',','').strip()
    region=row['区县'].replace(',','').strip()
    addr=row['详细地址'].replace(',','').strip()
    
    if not pd.isna(id) :
        # data.append([f'{id} {name} {region} {addr}'])
        dict[id]=name


image_path=r'C:\Users\sun\Downloads\428-update'
files = os.listdir(image_path)
# print(files)

for file in files:
    full_path = os.path.join(image_path, file)
    # print(full_path)
    if os.path.isfile(full_path):
        file_name_with_ext = os.path.basename(full_path)
        file_name_no_ext = os.path.splitext(file_name_with_ext)[0]
        extension = os.path.splitext(full_path)[1]
        # print(full_path)
        # print(file_name,file_name_no_ext,extension)
        # pass
        correspond_id=find_key_by_value(dict,file_name_no_ext)
        if correspond_id is not None :
            # print(correspond_id)
            # os.rename(old_file_name, new_file_name)
            new_path = os.path.join(image_path, correspond_id + extension)
            # pass
            # print(new_path)
            os.rename(full_path, new_path)


