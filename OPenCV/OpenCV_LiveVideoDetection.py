#Below code is for face detection when live video is capturing .

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(True):
    #Capture Frame by frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #Give path to feature file for face detection.
    face_cascade = cv2.CascadeClassifier("D:\Rajat\Anaconda\envs\opencv-env\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5)
    
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow('frame',frame)
    #wait till press key 'q' for closing the video window.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
