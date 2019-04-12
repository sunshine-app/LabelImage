# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 17:20
# @Author  : shine
# @File    : adjustLight.py
from PIL import ImageEnhance, ImageQt

# enhance(factor)增强器，
# 这个方法会返回一个被加强过的image对象，
# 参数factor为一个大于0的浮点数，1表示返回原始图片
# 图片颜色增强
# enhancer = ImageEnhance.Color(img)
# 图片亮度
# enhancer = ImageEnhance.Brightness(img)
# 图片对比度
# enhancer = ImageEnhance.Contrast(img)
# 图片锐化
# enhancer = ImageEnhance.Sharpness(img)


def adjust_image_light(qimage, factor):
    image = ImageQt.fromqimage(qimage)
    res_qimg = ImageQt.ImageQt(add_light(image, factor))
    return res_qimg


def add_light(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)
