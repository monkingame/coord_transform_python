# -*- coding: utf-8 -*-

# 读取5月1号问卷星数据

import pandas as pd
import coordTransform_utils as util


###############################################################################

# excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-7.xlsx'
# df_table = pd.read_excel(excel_path,converters={'唯一编码':str,'数据版本':str})

# for index,row in df.iterrows():
#     name=row['经营店铺名称']
#     id=row['唯一编码']
#     uniqueid=row['lat']
#     stamp=row['数据版本']
#     # print(index)
#     if not pd.isna(id) and not pd.isna(uniqueid):
#         if stamp == '429':
#             # count=count+1
#             # print(count)
#             # print
#             df.at[index, '数据来源'] = '问卷星'
#             df.at[index, '一店一码'] = uniqueid
# df.to_excel(excel_path, index=False)

###############################################################################

# all_wenjuanxing=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-1430-问卷星全纪录.xlsx'
# df_wenjuan = pd.read_excel(all_wenjuanxing,converters={r'1、“一店一码”商户编码':str,
#                                                        r'7、法定代表人身份证号':str})

# dict={}
# for index,row in df_wenjuan.iterrows():
#     code=row[r'1、“一店一码”商户编码']
#     idNo=row[r'7、法定代表人身份证号']
#     # print(index)
#     if not pd.isna(code) and not pd.isna(idNo):
#         # df_wenjuan.at[index, '数据来源'] = '问卷星'
#         # df_wenjuan.at[index, '一店一码'] = uniqueid
#         # print(code,idNo)
#         dict[idNo]=code
# # df_wenjuan.to_excel(excel_path, index=False)

# path_xuquan=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-问卷星-许权-0430.xlsx'
# df_xuquan = pd.read_excel(path_xuquan,converters={'lat':str})

# for index,row in df_xuquan.iterrows():
#     code=row['lat'] # 可能有身份证
#     new_code=dict.get(code)
#     if  new_code is not None:
#         # print(new_code)
#         df_xuquan.at[index, 'lat'] = new_code

# df_xuquan.to_excel(path_xuquan, index=False)

###############################################################################

all_wenjuanxing=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\截止到20230502-问卷星导入记录.xlsx'
df_wenjuan = pd.read_excel(all_wenjuanxing, sheet_name='20230430-许权-新整理',
                           converters={'唯一编码':str,'lat':str})

dict={}
for index,row in df_wenjuan.iterrows():
    id=row[r'唯一编码'] #唯一编码
    code=row[r'lat'] #一店一码
    # print(index)
    if not pd.isna(id) and not pd.isna(code):
        # print(code,idNo)
        dict[id]=code
# df_wenjuan.to_excel(excel_path, index=False)

# print(dict)

excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230502-数据\20230502-淄博本地生活数-7.xlsx'
df_table = pd.read_excel(excel_path,converters={'唯一编码':str,'数据版本':str})

for index,row in df_table.iterrows():
    name=row['经营店铺名称']
    id=row['唯一编码']
    # uniqueid=row['lat']
    uniqueid=dict.get(id)
    # stamp=row['数据版本']
    # print(index)
    if not pd.isna(id) and not pd.isna(uniqueid):
        # if stamp == '429':
        df_table.at[index, '数据来源'] = '问卷星'
        df_table.at[index, '一店一码'] = uniqueid
        df_table.at[index, '数据版本'] = '430'
        # print(id,uniqueid)

df_table.to_excel(excel_path, index=False)

