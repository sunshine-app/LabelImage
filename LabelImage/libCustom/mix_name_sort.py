# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 13:09
# @Author  : shine
# @File    : mix_name_sort.py
"""
基于字符数字混合排序的Python脚本
"""
from natsort import natsorted
# images.sort(key=lambda x: x.lower())
# 按创建时间排序
# images.sort(key=lambda x: os.path.getctime(x))
# 按创建时间，精确到ns排序
# images.sort(key=lambda x: os.stat(x).st_ctime_ns)


def sort_list_by_name(image_path_list):
    return natsorted(image_path_list)
