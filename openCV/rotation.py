import numpy as np
import cv2
import myLibrary

#read image
image = cv2.imread('testimage.jpg')

# get height and width
(h, w) = image.shape[:2]

#get center of testImage
center = (w/2, h/2)  # will rotate around center, we can take any point

#get Rotation Matrix, 45 deg rotation around center
M = cv2.getRotationMatrix2D(center, 45, 1.0)

#apply M to testImage
newImage = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", newImage)


cv2.imshow("New Image", myLibrary.rotate(image, 180))

cv2.waitKey(0)
