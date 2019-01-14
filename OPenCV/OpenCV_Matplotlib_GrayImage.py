#Below is the code for how we can use Matplotlib and opencv together for processing on image.
#And its quite intersting...So, give it a try..!!
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("messi.jpg",0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
