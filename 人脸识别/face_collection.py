"""
face_recognition_v1.0 -

Author 
Date 2022/4/22

"""
import time

import cv2 as cv

def face_coellection():
    # 一，采集人脸
    cap = cv.VideoCapture(0)  # 读入摄像头源

    # 读取图片，路径中不能有中文，否则图片加载失败
    recognizer = cv.face.LBPHFaceRecognizer_create()
    face_detector = cv.CascadeClassifier(r"./opencv-4.6.0/data/haarcascades/haarcascade_frontalface_default.xml")

    face_id = input('\n 请输入姓名序号:')
    print('\n 初始化面临捕获。看着镜头，等待 ...')
    count = 0
    while True:
        # 读取摄像头当前这一帧的画面  success:True False   image:当前这一帧画面
        success, img = cap.read()
        if not success:  # ok 是判断你有没有得到数据
            break
        # 转为灰度图片
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # 检测人脸
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                # 画出矩形框
                cv.rectangle(img, (x, y), (x + w, y + w), (0, 0, 255))
                count += 1
                # 保存图像
                cv.imwrite("FaceData/User_" + str(face_id) + '_' + str(count) + '.jpg', img[y: y + h, x: x + w])
                time.sleep(1)
                cv.imshow('image', img)
                # 显示当前捕捉到了多少人脸图片了，这样站在那里被拍摄时心里有个数，不用两眼一抹黑傻等着
                font = cv.FONT_HERSHEY_SIMPLEX
                cv.putText(img, 'num:%d' % count, (x + w, y + w), font, 1, (255, 0, 255), 4)
                print(f'保存---第{count}张图片')
        k = cv.waitKey(5)
        if k == 27:  # 通过esc键退出摄像
            break
        elif count >= 20:  # 得到20个样本后退出摄像
            break
    # 关闭摄像头
    cap.release()
    # 销毁窗口
    cv.destroyAllWindows()

