# -*- coding: utf-8 -*-

# Symmetric Difference
# 对称差集的英文名为 "Symmetric Difference"，是指两个集合中不重合的元素的集合。
# 可以理解为两个集合的差集去掉交集后得到的集合。在数学中，对称差集可以表示为 A △ B。

def get_symmetric_difference(dict1, dict2):
    diff1 = {k: dict1[k] for k in set(dict1) - set(dict2)}
    diff2 = {k: dict2[k] for k in set(dict2) - set(dict1)}
    return {**diff1, **diff2}

