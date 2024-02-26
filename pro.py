import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime




cap=cv2.VideoCapture(0)

while (True):
    ret,frame= cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKeyEx(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()