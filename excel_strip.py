# -*- coding: utf-8 -*-

# 将excel内单元格内所有的空格去掉，包括中间的

import pandas as pd
import coordTransform_utils as util
import csv

excel_path=r'C:\Users\sun\OneDrive\数字淄博\开发-淄博烧烤\20230427-数据\市直及区县停车场和厕所\整理-4-区县.xlsx'

df = pd.read_excel(excel_path,)
df = df.fillna('')
