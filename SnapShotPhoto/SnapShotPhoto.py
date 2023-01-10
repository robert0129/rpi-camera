from PyQt5 import QtCore, QtGui, QtWidgets
import sys, time, os
import numpy as np
from WEDUI import WEDUI as WUI

def EventTrigger():
    print("SnapShot Photo")
    timecam = WUI.UIObj["TIMECAM"]
    cv = WUI.UIObj["CV"]
    cam_num = WUI.UIObj["CAM_NUM"]
    cap = WUI.UIObj["CAP"]
    lblShowCam = WUI.UIObj["lblShowCam"]
    
    if timecam.isActive() == False:
            flag = cap.open(cam_num, cv.CAP_DSHOW)
            if flag == False:
                print("Error!")
            else:
                timecam.start(30)
    else:
        timecam.stop()
        cap.release()
        lblShowCam.clear()
        #self.SnapShopBtn.setText("Enable Camera")

def ShowCamera():
    cv = WUI.UIObj["CV"]
    cam_num = WUI.UIObj["CAM_NUM"]
    cap = WUI.UIObj["CAP"]
    lblShowCam = WUI.UIObj["lblShowCam"]
    snapflag = WUI.UIObj["SNAPFLAG"]
    width = WUI.UIObj["LFRAME"].width()
    height = WUI.UIObj["LFRAME"].height()
    if snapflag == 0:
       flag, image = cap.read()
       if flag == False:
           print("Image read Failure!")
           return
       else:
           show = cv.resize(image, (width, height))
           show = cv.cvtColor(show, cv.COLOR_BGR2RGB)
           showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
           lblShowCam.setPixmap(QtGui.QPixmap.fromImage(showImage))
    
def TakePictures():
    timecam = WUI.UIObj["TIMECAM"]
    cv = WUI.UIObj["CV"]
    cam_num = WUI.UIObj["CAM_NUM"]
    cap = WUI.UIObj["CAP"]
    width = WUI.UIObj["LFRAME"].width()
    height = WUI.UIObj["LFRAME"].height()
    snapflag = WUI.UIObj["SNAPFLAG"]
    seconds = WUI.UIObj["SECONDS"]
    
    btnCap = WUI.UIObj["btnCap"]
    btnCamera = WUI.UIObj["btnCamera"]
    
    lblShowCam = WUI.UIObj["lblShowCam"]
    lblShowCap = WUI.UIObj["lblShowCap"]
    
    if timecam.isActive() == False:
        return
    if snapflag == 1 :
        print("Taking Picture...")
        return
    WUI.UIObj["SNAPFLAG"] = 1
    btnCamera.setEnabled(False)
    lblShowCap.clear()
    CountDown(cv, seconds, cap, width, height, lblShowCam)
    #FName = fr"images\cap{time.strftime('%Y%m%d%H%M%S', time.localtime())}"
    FName = fr"C:\Users\chaol\Downloads\Project\rpi-camera\images\{time.strftime('%Y%m%d%H%M%S', time.localtime())}"
    lblShowCap.setVisible(True)
    flag, image = cap.read()
    if flag == False:
        print("SnapShot Failure !!!!")
    cv.putText(image, str("Wedding Day"), (0, 400), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv.LINE_AA)
    show = cv.resize(image, (width, height))
    show = cv.cvtColor(show, cv.COLOR_BGR2RGB)
    showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
    #lblShowCam.setPixmap(QtGui.QPixmap.fromImage(showImage))
    lblShowCap.setPixmap(QtGui.QPixmap.fromImage(showImage))
    lblShowCap.setGeometry(0, 0, width, height)
    cv.waitKey(1)
    showImage.save(FName + ".jpg", "JPG", 100)
    lblShowCap.setVisible(True)
    lblShowCam.setVisible(False)
    cv.imwrite(FName + ".jpg", image)
    time.sleep(5)
    btnCamera.setEnabled(True)
    lblShowCam.setVisible(True)
    lblShowCap.setVisible(False)
    lblShowCap.clear()
    WUI.UIObj["SNAPFLAG"] = 0
    print("End of TakePictures")

def CountDown(cv, seconds, cap, width, height, lblShowCam):
    print("Start of CountDown")
    start_time = time.process_time()
    elapsed = 0
    while elapsed < seconds:
        current_time = time.process_time()
        elapsed = int(current_time - start_time)
        flag, image = cap.read()
        msg = str(seconds - elapsed)
        if int(msg) > 0:
            cv.putText(image, msg, (320, 240), cv.FONT_HERSHEY_SIMPLEX,  5, (0, 255, 255), 5, cv.LINE_AA)        
        show = cv.resize(image, (width, height))
        show = cv.cvtColor(show, cv.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        lblShowCam.setPixmap(QtGui.QPixmap.fromImage(showImage))
        cv.waitKey(1)
    print("End of CountDown")
    