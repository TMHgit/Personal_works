"""
main_funct -

Author 
Date 2022/11/20

"""

import cv2 as cv
import numpy as np
import os
import time
import numpy
from PIL import Image, ImageDraw, ImageFont
import  face_collection
import face_recognition_training

# 语音说话
import pyttsx3
engine = pyttsx3.init()

engine.say('开始人脸采集，请看向摄像头')
face_collection.face_coellection()
engine.say('开始人训练数据集')
face_recognition_training.face_recognition_trai()




