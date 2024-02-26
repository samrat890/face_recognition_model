from ctypes.wintypes import POINT
import cv2
import numpy as np
#import cvzone
import face_recognition
import os
from datetime import datetime
from graphics import *

win = GraphWin("name",600,600)

win.setBackground(color_rgb(0,0,0))
txt = Text(Point(300, 300),"Joining Person")
txt2 = Text(Point(300, 200)," ")
txt3 = Text(Point(300, 370),"Time")
txt4 = Text(Point(300,30),"-:Attendence System:-") 

line = Line(Point(0,60),Point(600,60))

line.setOutline(color_rgb(0,200,200))

txt.setTextColor(color_rgb(0,200,200))
txt2.setTextColor(color_rgb(0,200,200))
txt3.setTextColor(color_rgb(0,200,200))
txt4.setTextColor(color_rgb(0,200,200))

txt.setSize(30)
txt2.setSize(30)
txt4.setSize(30)

txt.draw(win)
txt2.draw(win)
txt3.draw(win)
txt4.draw(win)

line.draw(win)
path = 'D:\python\project_odgi\images'
images = []
