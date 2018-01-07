# -*- coding:utf-8 -*-

import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

BGR_TO_XYZ = cv2.COLOR_BGR2XYZ
BGR_TO_HSV = cv2.COLOR_BGR2HSV
BGR_TO_GRAY = cv2.COLOR_BGR2GRAY

LOW_PASS_FILTER = np.ones((3, 3), np.float32)/9
HIGH_PASS_FILTER = np.array([[1, 1, 1], [1, -9, 1], [1, 1, 1]])


def change_bgr_to_other(image, color_space):
    return cv2.cvtColor(image, color_space)


def change_all_images_from_bgr_to_other(dir_bgr, dir_other, color_space):
    for name_image in listdir(dir_bgr):
        path_image_bgr = join(dir_bgr, name_image)
        path_image_other = join(dir_other, name_image)
        if isfile(path_image_bgr):
            image_bgr = cv2.imread(path_image_bgr)
            image_other = change_bgr_to_other(image_bgr, color_space)
            cv2.imwrite(path_image_other, image_other)


def apply_filter_to_image(image, kernel):
    return cv2.filter2D(image, -1, kernel)


def equalize_bgr_image(image):
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
