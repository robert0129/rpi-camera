from PyQt5 import QtCore, QtGui, QtWidgets
import sys, time, os
import numpy as np
from WEDUI import WEDUI as WUI

def UpdateUI(status):
    if status == True:
        WUI.UIObj["btnCap"].setEnabled(False)
        WUI.UIObj["btnCamera"].setEnabled(False)
        WUI.UIObj["btnAI"].setEnabled(False)
        WUI.UIObj["TIMECAM"].stop()
        WUI.UIObj["CAP"].release()
        WUI.UIObj["lblShowCam"].clear()
        WUI.UIObj["lblShowCap"].clear()
        dict_dpr = WUI.UIObj["DPRDIOGroup"]
        for d in WUI.UIObj["DPRDIOGroup"].values():
            d.setEnabled(False)
    else:
        WUI.UIObj["btnCap"].setEnabled(True)
        WUI.UIObj["btnCamera"].setEnabled(True)
        WUI.UIObj["btnAI"].setEnabled(True)
        dict_dpr = WUI.UIObj["DPRDIOGroup"]
        for d in WUI.UIObj["DPRDIOGroup"].values():
            d.setEnabled(True)
            
def EventTrigger():
    print("Display Photo")
    dflag = WUI.UIObj["DISPLAYFLAG"]
    cv = WUI.UIObj["CV"]
    cam_num = WUI.UIObj["CAM_NUM"]
    cap = WUI.UIObj["CAP"]
    lblShowCam = WUI.UIObj["lblShowCam"]
    lblShowCap = WUI.UIObj["lblShowCap"]
    width = WUI.UIObj["LFRAME"].width()
    height = WUI.UIObj["LFRAME"].height()
    folder = WUI.UIObj["IMGFOLDER"]
    if dflag > 0:
        print("Displyaing")
        return
    UpdateUI(True)
    WUI.UIObj["DISPLAYFLAG"] = 1
    onlyfiles = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    WUI.UIObj["lblShowCap"].setVisible(True)
    cnt = 0
    fcnt = len(onlyfiles)
    start_time = time.process_time()
    while cnt < fcnt :
        elapsed = int(time.process_time() - start_time)
        img = cv.imread(onlyfiles[cnt])
        if elapsed > 2 :
            cnt = cnt + 1
            start_time = time.process_time()
        show = cv.resize(img, (width, height))
        show = cv.cvtColor(show, cv.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        lblShowCap.setPixmap(QtGui.QPixmap.fromImage(showImage))
        lblShowCap.setGeometry(0, 0, width, height)
        cv.waitKey(1)
    UpdateUI(False)
    WUI.UIObj["DISPLAYFLAG"] = 0
 
def Selected():
    id = WUI.UIObj["btnGroup"].checkedId()
    if id == 1:
        folder = fr"C:\Users\chaol\Downloads\Project\rpi-camera\images\ChungYaun"
    elif id == 2:
        folder = fr"C:\Users\chaol\Downloads\Project\rpi-camera\images\Eighth"
    elif id == 3:
        folder = fr"C:\Users\chaol\Downloads\Project\rpi-camera\images\Register"
    elif id == 4:
        folder = fr"C:\Users\chaol\Downloads\Project\rpi-camera\images\Tracy"
    elif id == 5:
        folder = fr"C:\Users\chaol\Downloads\Project\rpi-camera\images\Cheeses"
    else:
        folder = fr"C:\Users\chaol\Downloads\Project\rpi-camera\images\Live"
    WUI.UIObj["IMGFOLDER"] = folder
