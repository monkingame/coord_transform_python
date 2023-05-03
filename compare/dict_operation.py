# -*- coding: utf-8 -*-

# 字典操作

# # 交集
# def get_intersection_dict(dict1, dict2):
#     # 返回两个字典的交集
#     # 但是这个不合理，返回了dict1中的值
#     return {k: dict1[k] for k in dict1.keys() & dict2.keys()}

# 取得交集key
def get_intersection_keys(dict1, dict2):
    intersection = set(dict1.keys()) & set(dict2.keys())
    return intersection


# Symmetric Difference
# 对称差集的英文名为 "Symmetric Difference"，是指两个集合中不重合的元素的集合。
# 可以理解为两个集合的差集去掉交集后得到的集合。在数学中，对称差集可以表示为 A △ B。
def get_symmetric_difference_dict(dict1, dict2):
    diff1 = {k: dict1[k] for k in set(dict1) - set(dict2)}
    diff2 = {k: dict2[k] for k in set(dict2) - set(dict1)}
    return {**diff1, **diff2}


# # 差集
# def get_diffefence_dict(dict_big, dict_small):
#     # 返回字典 dict_big 中存在，但是字典 dict_small 中不存在的键-值对构成的字典
#     diff_dict = {k: dict_big[k] for k in set(dict_big) - set(dict_small)}
#     return diff_dict

# 差集
def get_difference_keys(dict_big, set_keys_small):
    # return set(dict_big.keys()).difference(set(set_keys_small.keys()))
    # 转换为集合再取差集
    diff_keys = set(dict_big.keys()) - set_keys_small
    # 返回新字典
    return {k: dict_big[k] for k in diff_keys}

# # 只取回存在于set中的key
# def get_set_difference_keys(dict_big, set_keys_small):
#     # return set(dict_big.keys()).difference(set(set_keys_small.keys()))
#     # 转换为集合再取差集
#     diff_keys = set(dict_big.keys()) - set_keys_small
#     # 返回新字典
#     return {k: dict_big[k] for k in diff_keys}

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


