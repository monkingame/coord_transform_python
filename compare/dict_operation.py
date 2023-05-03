# -*- coding: utf-8 -*-

# 字典操作

# 交集
def get_dict_intersection(dict1, dict2):
    # 返回两个字典的交集
    return {k: dict1[k] for k in dict1.keys() & dict2.keys()}



# Symmetric Difference
# 对称差集的英文名为 "Symmetric Difference"，是指两个集合中不重合的元素的集合。
# 可以理解为两个集合的差集去掉交集后得到的集合。在数学中，对称差集可以表示为 A △ B。
def get_symmetric_difference(dict1, dict2):
    diff1 = {k: dict1[k] for k in set(dict1) - set(dict2)}
    diff2 = {k: dict2[k] for k in set(dict2) - set(dict1)}
    return {**diff1, **diff2}


# 差集
def dict_diffefence(dict_parent, dict_child):
    # 返回字典 dict_parent 中存在，但是字典 dict_child 中不存在的键-值对构成的字典
    diff_dict = {k: dict_parent[k] for k in set(dict_parent) - set(dict_child)}
    return diff_dict



# 作废
# 使用 dict_symmetric_difference
def get_unique_dict(a, b):
    unique_dict = {}
    for key in a:
        if key not in b:
            unique_dict[key] = a[key]
    for key in b:
        if key not in a and key not in unique_dict:
            unique_dict[key] = b[key]
    return unique_dict


