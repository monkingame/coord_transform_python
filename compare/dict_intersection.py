# -*- coding: utf-8 -*-

# 交集
def get_dict_intersection(dict1, dict2):
    """
    返回两个字典的交集
    """
    return {k: dict1[k] for k in dict1.keys() & dict2.keys()}
