"""
test -

Author 
Date 2022/11/20

"""
import numpy as np
from PIL import Image
import os
import cv2 as cv


def get_imge_and_labels(path):
    imagepaths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagepath in imagepaths:
        print(os.path.split(imagepath)[-1])
    print(imagepaths)
get_imge_and_labels('FaceData')