#This is python code for FaceDetection from image using OpenCV. I just learning image processing, So, it is on starting phase.

#Import cv2 library for opencv
import cv2 as cv

#imread function is used to read the image, as a parameter, you can send path of image.
img = cv.imread("messi.jpg")
#resize function is used to change size of image for better working.
resized = cv.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

#Below code is for showing image.
cv.imshow("MessiFace",resized)
cv.waitKey(0)
cv.destroyAllWindows()

#A Haar Cascade is basically a classifier which is used to detect particular objects from the source. 
#The haarcascade_frontalface_default.xml is a haar cascade designed by OpenCV to detect the frontal face.

face_cascade = cv.CascadeClassifier("D:\Rajat\Anaconda\envs\opencv-env\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

#Below code is used to convert colored image into grey_image.
grey_image = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)

#using detectMultiScale() function, we will collects the faces from image.
#here, scaleFactor is 5% which means it will resize tha image untill face gets detetcted.
faces = face_cascade.detectMultiScale(grey_image, scaleFactor = 1.05, minNeighbors = 5)

#Below code is for creating ractangle around the faces that we detected.

for x,y,w,h in faces:
	resized = cv.rectangle(resized,(x,y),(x+w,y+h),(0,255,0),3)

# Code for showing our real output.... yeee!!!

cv.imshow("LEGEND_FACE",resized)
cv.waitKey(0)
cv.destroyAllWindows()
