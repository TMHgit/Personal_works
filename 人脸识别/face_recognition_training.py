"""
face_recognition_v1.0 -

Author 
Date 2022/11/20

"""

# 人脸数据训练
import numpy as np
from PIL import Image
import os
import cv2 as cv

def face_recognition_trai():
    # 人脸数据路径
    recognizer = cv.face.LBPHFaceRecognizer_create()
    detector = cv.CascadeClassifier("./opencv-4.6.0/data/haarcascades/haarcascade_frontalface_default.xml")


    def get_imge_and_labels(path):
        imagepaths = [os.path.join(path, f) for f in os.listdir(path)]  # join函数的作用？拼接路径
        facesamples = []
        ids = []
        for imagepath in imagepaths:
            PIL_img = Image.open(imagepath).convert('L')   # convert it to grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagepath)[-1].split("_")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                facesamples.append(img_numpy[y:y + h, x: x + w])
                ids.append(id)
        return facesamples, ids


    print('训练数据集中 需要几秒钟。等待……')
    faces, ids = get_imge_and_labels('FaceData')
    recognizer.train(faces, np.array(ids))

    recognizer.write(r'FaceTrainer\trainer.yml')

