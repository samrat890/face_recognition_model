from graphics import *
import cv2
import numpy as np
import os

cap=cv2.VideoCapture(0)
ret, frame = cap.read(0)
cap.set(3,640)
cap.set(4,480)
win=GraphWin("name",200,200)
background=cv2.imread('D:\\python\\project_odgi\\zaxix\\background.png')
background=cv2.resize(background,(900,650))
print(type(win))
while True:
    
    ret,frame=cap.read()
    frame=cv2.resize(frame,(400,400))
    cv2.imshow('frame',frame)
    cv2.imshow('back',background)
    background[243:243+400 ,10:10+400]=frame
    # background[443+200,490+200]=win
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
  
