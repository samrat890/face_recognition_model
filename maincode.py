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
path = './project_odgi/images'
images = []

personNames = []
myList = os.listdir(path)
#print(myList)
for cu_img in myList:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_Img)
    personNames.append(os.path.splitext(cu_img)[0])
print(personNames)


def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def attendance(name):
    with open('D:\\python\\project_odgi\\Attendance.csv', '+r') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        # if name not in nameList:
        #     time_now = datetime.now()
        #     tStr = time_now.strftime('%H:%M:%S')
        #     dStr = time_now.strftime('%d/%m/%Y')
        #     f.writelines(f'\n{name},{tStr},{dStr}')
            if name == nameList:
                s=True
                if s==True:
                    time_now = datetime.now()
                    tStr = time_now.strftime('%H:%M:%S')
                    dStr = time_now.strftime('%d/%m/%Y')
                    f.writelines(f'\n{name},{tStr},{dStr},{"in"}')
                else:
                    time_now = datetime.now()
                    tStr = time_now.strftime('%H:%M:%S')
                    dStr = time_now.strftime('%d/%m/%Y')
                    f.writelines(f'\n{name},{tStr},{dStr},{"out"}')



encodeListKnown = faceEncodings(images)
print('All Encodings Complete!!!')
#print(os.getcwd())

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)

    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(faces)
    encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = personNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            #cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 0, 0), cv2.FILLED)
            #cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
            attendance(name)
            txt.setText(name)
            txt2.setText("Welcome")
            txt3.setText(datetime.now().isoformat())
            
        

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()