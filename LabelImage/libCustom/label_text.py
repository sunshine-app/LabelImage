# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 16:10
# @Author  : shine
# @File    : label_text.py
import os


def text_is_exist(image_path, text_suffix):
    if image_path is None:
        return False
    bool_exist = False
    text_path = os.path.splitext(image_path)[0] + text_suffix
    if os.path.exists(text_path):
        bool_exist = text_content_size(text_path)
    return bool_exist


def text_content_size(text_path):
    bool_size = False
    if os.path.getsize(text_path) > 1:
        bool_size = True
    return bool_size
