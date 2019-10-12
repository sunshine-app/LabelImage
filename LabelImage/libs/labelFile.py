# -*- coding: utf-8 -*-
from PyQt5.QtGui import QImage

from libs.yolo_io import YOLOWriter
from libs.yolo_io import TXT_EXT
import os.path


class LabelFileError(Exception):
    pass


class LabelFile(object):
    suffix = TXT_EXT

    def __init__(self):
        self.shapes = ()
        self.imagePath = None
        self.imageData = None
        self.verified = False

    def saveYoloFormat(self, filename, shapes, imagePath, classList, margin_pixel):
        imgFolderPath = os.path.dirname(imagePath)
        imgFolderName = os.path.split(imgFolderPath)[-1]
        imgFileName = os.path.basename(imagePath)
        image = QImage()
        image.load(imagePath)
        imageShape = [image.height(), image.width(), 1 if image.isGrayscale() else 3]
        writer = YOLOWriter(imgFolderName, imgFileName, imageShape, margin_pixel, localImgPath=imagePath)
        writer.verified = self.verified
        for shape in shapes:
            points = shape['points']
            label = shape['label']
            bndbox = LabelFile.convertPoints2BndBox(points)
            writer.addBndBox(bndbox[0], bndbox[1], bndbox[2], bndbox[3], label)
        writer.save(targetFile=filename, classList=classList)

    def toggleVerify(self):
        self.verified = not self.verified

    @staticmethod
    def isLabelFile(filename):
        fileSuffix = os.path.splitext(filename)[1].lower()
        return fileSuffix == LabelFile.suffix

    @staticmethod
    def convertPoints2BndBox(points):
        xmin = float('inf')
        ymin = float('inf')
        xmax = float('-inf')
        ymax = float('-inf')
        for p in points:
            x = p[0]
            y = p[1]
            xmin = min(x, xmin)
            ymin = min(y, ymin)
            xmax = max(x, xmax)
            ymax = max(y, ymax)

        if xmin < 1:
            xmin = 1

        if ymin < 1:
            ymin = 1
        return (int(xmin), int(ymin), int(xmax), int(ymax))
