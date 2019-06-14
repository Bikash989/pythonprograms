import cv2
import numpy as np
import myLibrary

#read the image
image = cv2.imread('testimage.jpg')
#show the Image
cv2.imshow("Original Image", image) # pass 2 args, name and image object

height = image.shape[0]
width  = image.shape[1]
# 30px to shift right and 20 px to shift down
M = np.float32([[1,0,30],[0,1,20]])

print(M)
shift = cv2.warpAffine(image, M, (width , height))
cv2.imshow("Shifted Down {} and Right {}".format(20,30), shift)

newImage = myLibrary.translate(image, 0, 100)
cv2.imshow("new image", newImage)

cv2.waitKey(0)
