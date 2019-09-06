import cv2
import numpy as np
import myLibrary
im = cv2.imread('image.jpg')
newimage = myLibrary.resize(im,500)
cv2.imshow("OriginalImage",newimage)
# cv2.imsave("newImage.jpg",newimage)
'''
    Blur an image Apply low pass filter kernel
    kernal basically a matrix 3x3 for eg all 3 and normalized i.e divided by 9
    kernel = 
'''
kernel_identity = np.array([[0,0,0],[0,1,0],[0,0,0]])
kernel_3x3 = np.ones((3,3), np.float32) / 9.0
kernel_5x5 = np.ones((5,5),np.float32)/25.0

output = cv2.filter2D(newimage, -1, kernel_identity)
cv2.imshow('Identity filtered applied',output)

output = cv2.filter2D(newimage,-1,kernel_3x3)
cv2.imshow('3x3 filter', output)
print(kernel_3x3)
print(kernel_5x5)
output = cv2.filter2D(newimage, -1, kernel_5x5)
cv2.imshow('5x5 filter',output)

''' if you don't want to use your own kernel, use blur functino
   eg: cv2.blue(img, (3,3))
'''
# output_blur = cv2.blur(newimage,(7,7))
# cv2.imshow('7x7 filter',output_blur)
cv2.waitKey(0)



cv2.waitKey(0)
