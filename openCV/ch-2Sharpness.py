import cv2
import numpy as np 
import myLibrary
im = cv2.imread('image.jpg')
newimage = myLibrary.resize(im,500)
cv2.imshow("OriginalImage",newimage)

#generating the kernels
kernel1 = np.array([[-1,-1,-1,],[-1,9,-1],[-1,-1,-1]])
kernel2 = np.array([[1,1,1],[1,-7,1],[1,1,1]])
kernel3 = np.array([[-1,-1,-1,-1,-1],
                    [-1,2,2,2,-1],
                    [-1,2,8,2,-1],
                    [-1,2,2,2,-1],
                    [-1,-1,-1,-1,-1]])/8.0
# apply kernels
output_1 = cv2.filter2D(newimage, -1, kernel1)
output_2 = cv2.filter2D(newimage, -1, kernel1)
output_3 = cv2.filter2D(newimage, -1, kernel1)

cv2.imshow('Sharpening', output_1)
cv2.imshow('Excessive Sharpening', output_2)
cv2.imshow('Edge Enhancement', output_3)

cv2.waitKey(0)

                    