from PyQt5 import QtCore, QtGui, QtWidgets
import sys, time, os
import numpy as np
import cv2 as cv

global UIObj
UIObj = dict()
UIObj["CAM_NUM"] = 0
UIObj["CV"] = cv
UIObj["CAP"] = cv.VideoCapture(UIObj["CAM_NUM"])
UIObj["TIMECAM"] = QtCore.QTimer()
UIObj["SNAPFLAG"] = 0
UIObj["DISPLAYFLAG"] = 0
UIObj["SECONDS"] = 3
UIObj["DFAULTFOLDER"] = fr"C:\Users\chaol\Downloads\Project\rpi-camera\images\Live"
#UIObj["lblGroup"] = dict()
#UIObj["btnSSPGroup"] = dict()
#UIObj["btnDPGroup"] = dict()
#UIObj["btnAIPGroup"] = dict()
#UIObj["CAMERA"]= dict()



            