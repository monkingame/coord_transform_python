# -*- coding: utf-8 -*-


def get_unique_dict(a, b):
    unique_dict = {}
    for key in a:
        if key not in b:
            unique_dict[key] = a[key]
    for key in b:
        if key not in a and key not in unique_dict:
            unique_dict[key] = b[key]
    return unique_dict

