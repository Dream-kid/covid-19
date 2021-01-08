# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
print('temp')
img = cv2.imread('temp.jpg')
cv2.imshow('ll',img)
print(img.shape)
cv2.waitKey(0)