#This is python code for face detection from first frame of video that we will captured from Video that we are going to capture

import time
import cv2

#VideoCapture() function is for capturing video.
video = cv2.VideoCapture(0)

#here, check work as a boolean function, which means wheather above function captured a video or not.
#frame variable is for reading first image from video.
check,frame = video.read()
print(check)
print(frame)

#we are using time library here because we have to wait for capturing the image otherwise it will just get ON and OFF in an instant.
time.sleep(3)
#cv2.imshow("Webcam",frame) -> we will see frames here in video format.
video.release()

#For seeing the frame that we captured
cv2.imshow("WebCam",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

face_cascade = cv2.CascadeClassifier("D:\Rajat\Anaconda\envs\opencv-env\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

grey_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_image, scaleFactor = 1.05, minNeighbors = 5)

for x,y,w,h in faces:
	frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("WebCam",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
