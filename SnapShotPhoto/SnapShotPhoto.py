from PyQt5 import QtCore, QtGui, QtWidgets
import sys, cv2, time, os
import numpy as np

def EventTrigger(CAM_NUM, CAP, timeCam, cv2):
    print("SnapShot Photo")
    if timeCam.isActive() == False:
            flag = CAP.open(CAM_NUM,  cv2.CAP_DSHOW)
            if flag == False:
                print("Error!")
            else:
                timeCam.start(30)
    else:
        timeCam.stop()
        CAP.release()
        lblShowCam.clear()
        #self.SnapShopBtn.setText("Enable Camera")

def ShowCamera(CAP, cv2, width, height, lblShowCam):
    #    if self.takeFlag == 0:
    flag, image = CAP.read()
    show = cv2.resize(image, (width, height))
    show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
    showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
    lblShowCam.setPixmap(QtGui.QPixmap.fromImage(showImage))
    
def TakePictures(timeCam, takeFlag, CAP, cv2, width, height, seconds, lblShowCam, lblShowCap):
    if timeCam.isActive() == False:
        return
    if takeFlag == 1 :
        return
    #self.CapBtn.setEnabled(False)
    CountDown(takeFlag, cv2, seconds, CAP, width, height, lblShowCam)
    #FName = fr"images\cap{time.strftime('%Y%m%d%H%M%S', time.localtime())}"
    FName = fr"C:\Users\chaol\Downloads\Project\rpi-camera\images\{time.strftime('%Y%m%d%H%M%S', time.localtime())}"
    lblShowCam.setVisible(False)
    #cv2.imwrite(FName + ".jpg", image)
    lblShowCap.setVisible(True)
    takeFlag = 1
    flag, image = CAP.read()
    cv2.putText(image, str("Wedding Day"), (0, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
    show = cv2.resize(image, (width, height))
    show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
    showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
    lblShowCam.setPixmap(QtGui.QPixmap.fromImage(showImage))
    cv2.waitKey(1)
    lblShowCap.setPixmap(QtGui.QPixmap.fromImage(showImage))
    lblShowCap.setGeometry(0, 0, width, height)
    showImage.save(FName + ".jpg", "JPG", 100)
    lblShowCap.setVisible(True)
    time.sleep(5)
    takeFlag = 0
    #CapBtn.setEnabled(True)
    lblShowCam.setVisible(True)
    lblShowCap.setVisible(False)
    lblShowCap.clear()

def CountDown(takeFlag, cv2, seconds, CAP, width, height, lblShowCam):
    takeFlag = 1
    counts = seconds
    start = time.time()
    time.process_time()
    elapsed = 0
    while elapsed < counts:
        elapsed = time.time() - start
        elapsed_time = int(time.time() - start)
        flag, image = CAP.read()
        if elapsed_time < counts :
            cv2.putText(image, str(int(counts - elapsed_time)), (320, 240), cv2.FONT_HERSHEY_SIMPLEX,  5, (0, 255, 255), 5, cv2.LINE_AA)
        show = cv2.resize(image, (width, height))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        lblShowCam.setPixmap(QtGui.QPixmap.fromImage(showImage))
        cv2.waitKey(1)
    takeFlag = 0