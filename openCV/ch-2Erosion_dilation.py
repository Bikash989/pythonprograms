''' modifying geometric structure in the image '''
import cv2
import numpy as np 
im = cv2.imread('im_ero_dil.png')
kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(im,kernel,iterations=1)
img_dilation = cv2.dilate(im, kernel, iterations=5)

cv2.imshow('input',im)
cv2.imshow('erosion',img_erosion)
cv2.imshow('Dilation',img_dilation)

cv2.waitKey(0)