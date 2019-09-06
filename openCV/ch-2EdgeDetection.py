# detect sharp edges and produce binary output
# think of it as high pass filtering operation ->
# it allows high frequency content to pass through and blocks
# the low frequency content
# build a kernel of a high pass filter
# we will use sobel filter, whose kernel is 
# Sx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
# Sy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

import cv2 
import numpy as np
import myLibrary
image = cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)
newimage = myLibrary.resize(image,500)
# get the shape (height and width)
rows,cols = newimage.shape

sobel_h = cv2.Sobel(newimage, cv2.CV_64F, 1, 0, ksize=5)
sobel_v = cv2.Sobel(newimage, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow('Original Image', newimage)
cv2.imshow('Sobel Horizontal', sobel_h)
cv2.imshow('Sobel Vertical', sobel_v)

# you can also use laplacian filter

laplacian = cv2.Laplacian(newimage,cv2.CV_64F)
cv2.imshow('Laplacian filter',laplacian)
# laplacian give rise to noise in the picture
# to overcome that we can use Canny edge detector
# a =[]
# b =[]
# for i in range(0,100):
#     a.append(i)
# for i in range(100,200):
#     b.append(i)
# for i,j in zip(a,b):
#     canny = cv2.Canny(newimage,i,j)
#     cv2.imshow('Canny filter {}{}'.format(i,j),canny)

canny = cv2.Canny(newimage,50,240) 
# takes two number to indicate the threshold
# 50 = low threshold, 2nd arg
# 240 = high threshold, 3rd arg
cv2.imshow('Canny filter',canny)
cv2.waitKey(0)

