#Below program loads an image in grayscale, displays it, save the image if you press 's' and exit, or
# simply exit without saving if you press ESC key.
import cv2

img = cv2.imread("C:\\Users\\Test\\Desktop\\CodeOpenCV\\messi.jpg",0)

cv2.imshow("MessiB&W",img)
k = cv2.waitKey(0) & 0xFF            # 0xFF for 64 bit machine if only waitKey() function will not work.
if k==27:   #wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  #wait for 's' key to save and exit
    cv2.imwrite("C:\\Users\\Test\\Desktop\\C &odeOpenCV\\MessB&W.png",img)
    cv2.destroyAllWindows()
