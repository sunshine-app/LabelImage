# -*- coding: utf8 -*-
import os
import codecs
from libs.constants import DEFAULT_ENCODING

TXT_EXT = '.txt'
ENCODE_METHOD = DEFAULT_ENCODING


# Yolo格式输出
class YOLOWriter:

    def __init__(self, foldername, filename, imgSize, margin_pixel, databaseSrc='Unknown', localImgPath=None):
        self.foldername = foldername
        self.filename = filename
        self.databaseSrc = databaseSrc
        self.imgSize = imgSize
        self.boxlist = []
        self.localImgPath = localImgPath
        self.verified = False
        self.margin_pixel = margin_pixel

    def addBndBox(self, xmin, ymin, xmax, ymax, name):
        bndbox = {'xmin': xmin - self.margin_pixel, 'ymin': ymin - self.margin_pixel,
                  'xmax': xmax + self.margin_pixel, 'ymax': ymax + self.margin_pixel, 'name': name}
        self.boxlist.append(bndbox)

    def BndBox2YoloLine(self, box, classList=[]):
        xmin = box['xmin']
        xmax = box['xmax']
        ymin = box['ymin']
        ymax = box['ymax']

        xcen = float((xmin + xmax)) / 2 / self.imgSize[1]
        ycen = float((ymin + ymax)) / 2 / self.imgSize[0]

        w = float((xmax - xmin)) / self.imgSize[1]
        h = float((ymax - ymin)) / self.imgSize[0]

        # PR387
        boxName = box['name']
        if boxName not in classList:
            classList.append(boxName)

        classIndex = classList.index(boxName)

        return classIndex, xcen, ycen, w, h

    def save(self, classList=None, targetFile=None):
        if classList is None:
            classList = []
        if targetFile is None:
            out_file = open(self.filename + TXT_EXT, 'w', encoding=ENCODE_METHOD)
            classesFile = os.path.join(os.path.dirname(os.path.abspath(self.filename)), "classes.txt")
            out_class_file = open(classesFile, 'w', encoding=ENCODE_METHOD)
        else:
            out_file = codecs.open(targetFile, 'w', encoding=ENCODE_METHOD)
            classesFile = os.path.join(os.path.dirname(os.path.abspath(targetFile)), "classes.txt")
            out_class_file = open(classesFile, 'w', encoding=ENCODE_METHOD)

        for box in self.boxlist:
            classIndex, xcen, ycen, w, h = self.BndBox2YoloLine(box, classList)
            out_file.write("%d %.6f %.6f %.6f %.6f\n" % (classIndex, xcen, ycen, w, h))

        for c in classList:
            out_class_file.write(c + '\n')

        out_class_file.close()
        out_file.close()


class YoloReader:

    def __init__(self, filepath, image, classListPath=None):
        # shapes type: [labbel, [(x1,y1), (x2,y2), (x3,y3), (x4,y4)], color, color]
        self.shapes = []
        self.filepath = filepath

        if classListPath is None:
            dir_path = os.path.dirname(os.path.realpath(self.filepath))
            self.classListPath = os.path.join(dir_path, "classes.txt")
        else:
            self.classListPath = classListPath

        classesFile = open(self.classListPath, 'r', encoding=ENCODE_METHOD)
        self.classes = classesFile.read().strip('\n').split('\n')

        imgSize = [image.height(), image.width(),
                   1 if image.isGrayscale() else 3]

        self.imgSize = imgSize

        self.verified = False
        self.parseYoloFormat()

    def getShapes(self):
        return self.shapes

    def addShape(self, label, xmin, ymin, xmax, ymax, confidence_level=None):

        points = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
        self.shapes.append((label, points, None, None, confidence_level))

    def yoloLine2Shape(self, classIndex, xcen, ycen, w, h):
        label = self.classes[int(classIndex)]

        xmin = max(float(xcen) - float(w) / 2, 0)
        xmax = min(float(xcen) + float(w) / 2, 1)
        ymin = max(float(ycen) - float(h) / 2, 0)
        ymax = min(float(ycen) + float(h) / 2, 1)

        xmin = int(self.imgSize[1] * xmin)
        xmax = int(self.imgSize[1] * xmax)
        ymin = int(self.imgSize[0] * ymin)
        ymax = int(self.imgSize[0] * ymax)

        return label, xmin, ymin, xmax, ymax

    def parseYoloFormat(self):
        bndBoxFile = open(self.filepath, 'r')
        for bndBox in bndBoxFile:
            single_box_line = bndBox.split(' ')
            classIndex, xcen, ycen, w, h = single_box_line[0:5]
            label, xmin, ymin, xmax, ymax = self.yoloLine2Shape(classIndex, xcen, ycen, w, h)
            if len(single_box_line) == 6:
                confidence_level = single_box_line[5]
                self.addShape(label, xmin, ymin, xmax, ymax, confidence_level)
            else:
                self.addShape(label, xmin, ymin, xmax, ymax)
