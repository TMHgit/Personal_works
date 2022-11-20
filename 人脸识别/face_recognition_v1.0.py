"""
face_recognition -

Author 
Date 2022/11/20

"""


# 人脸识别
# coding=utf-8
import time

import cv2 as cv
import numpy
from PIL import Image, ImageDraw, ImageFont
# 语音说话
import pyttsx3


engine = pyttsx3.init()
# 解决cv2.putText绘制中文乱码
def cv_img_add_text(img2, text, left, top, textColor=(0, 0, 255), textSize=20):
    if isinstance(img2, numpy.ndarray):  # 判断是否OpenCV图片类型
        img2 = Image.fromarray(cv.cvtColor(img2, cv.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img2)
    # 字体的格式
    fontStyle = ImageFont.truetype(r"./FONTS/Fonts/MSYH.TTC", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv.cvtColor(numpy.asarray(img2), cv.COLOR_RGB2BGR)

# 导入数据模型
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('FaceTrainer/trainer.yml')
cascadePath = "./opencv-4.6.0/data/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascadePath)
font = cv.FONT_HERSHEY_SIMPLEX

num = 0
names = ['金狗', '田茂海', '宋小宝', '赵四']
cam = cv.VideoCapture(0)
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    ret, img = cam.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 加载为灰度图像加快检测速度；

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH))
    )

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 画出人脸的框
        num, confidence = recognizer.predict(gray[y:y + h, x:x + w])  # 获取到置信区间

        if confidence < 100:
            name = names[num]

        else:
            name = "unknown"
        # 解决cv2.putText绘制中文乱码
        img = cv_img_add_text(img, name, x + 5, y - 30)
        if name == "unknown":
            engine.say('识别失败')
            engine.runAndWait()
        else:
            engine.say(name + '同学，你好')
            engine.runAndWait()
        time.sleep(4)


    key = cv.waitKey(1) & 0xFF  # 其他系统下，waitkey()返回的值可能不是ascii码（就是没法直接判断它按的是哪个按钮了），通过& 0xFF取其低八位（字符的最后一个字节）就能判断了
    cv.imshow('result', img)
    if key == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
