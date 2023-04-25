import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.cell import column_index_from_string

# 加载 Excel 文件
book = load_workbook('data.xlsx')
# 获取第一个 sheet
ws = book.active

# 列名列表
columns = ['姓名', '性别', '年龄']

# 遍历 DataFrame，将数据写入到 Excel 文件中
for idx, row in df.iterrows():
    # 获取行索引，行索引从第三行开始（因为第一行是标题行，第二行是数据行）
    row_idx = idx + 3
    for col_name in columns:
        # 获取列索引
        col_idx = column_index_from_string(ws[col_name + '1'].column)
        # 获取单元格
        cell = ws.cell(row=row_idx, column=col_idx)
        # 将数据写入单元格
        cell.value = row[col_name]

# 保存 Excel 文件
book.save('data.xlsx')
