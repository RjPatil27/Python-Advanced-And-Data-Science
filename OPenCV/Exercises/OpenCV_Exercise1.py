#When you used matplotlib and opencv for loading color image, then there is a problem of RGB sequence.
#Assignment : try to solve this issue.
'''Discussion : This happen because Matplotlib uses there is slight differnece between pixel ordering in matplotlib and 
                OpenCV. 
                Matplotlib follow RGB order likely OpenCV follows BGR order which is quite reverse according to Matplotlib.
                because of that image that we get as output is different.
'''
'''Answer : So, as a solution for this above problem, we have to convert that image into RGB mode. for further understanding 
            Lets, Check out the code below....!
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img  = cv2.imread('messi.jpg')

'''
As we know, colored image has 3 channel RGB may be vary in order. In this case as Matplotlib uses RGB and OpenCV uses BGR 
order. We will need to split this 3 channel and stored them into 3 different variable using split() function from opencv.
'''
b,g,r = cv2.split(img)

'''
After splitting all three r,g,b channel in different variable. we will merge them into required order whichever we want to
like for opencv its BGR and for matplotlib its RGB.
'''
img2 = cv2.merge([r,g,b])

#starting image before restroing the color order
#plt.subplot(121)
plt.imshow(img)

#Image after restroing order of color.
#plt.subplot(121)
plt.imshow(img2)
