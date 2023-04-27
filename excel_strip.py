# -*- coding: utf-8 -*-

# 将excel内单元格内所有的空格去掉，包括中间的

import pandas as pd
import re

excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230427-数据\市直及区县停车场和厕所\整理-4-区县.xlsx'

df = pd.read_excel(excel_path,)
# df = df.fillna('')

for index,row in df.iterrows():
    index=row['序号']
    depart=re.sub(r"\s+", "",row['单位'])
    addr=re.sub(r"\s+", "",row['地址'])
    park=re.sub(r"\s+", "",row['停车场'])
    toilet=re.sub(r"\s+", "",row['厕所'])
    # print(index,depart,addr,park,toilet)
    df.at[index, '单位'] = depart
    df.at[index, '地址'] = addr
    df.at[index, '停车场'] = park
    df.at[index, '厕所'] = toilet

df.to_excel(excel_path, index=False)

