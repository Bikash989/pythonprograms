#2d transformation
import cv2,time
import numpy as np
import myLibrary

image = cv2.imread('testimage.jpg')
myLibrary.showOriginal(image)
cv2.waitKey(0)
print()
# # time.sleep(2)
print("Demonstration Translation (shifting of an object along x and y axis) ")
n = input("Enter x and y (seperated by space): ")
val = n.split(' ')
a = int(val[0])
b = int(val[1])
translatedImage = myLibrary.translate(image,a,b)
cv2.imshow("Translated Image",translatedImage)
cv2.waitKey(0)
print()

print("Demonstration of Rotation by an angle")
n = int(input("Enter an angle "))
rotatedImage = myLibrary.rotate(image,n)
cv2.imshow("Rotated Image",rotatedImage)
cv2.waitKey(0)

print()
print("Demonstration of Resizing")
n = input("Enter new width and height (seperated by space): ")
val = n.split(' ')
width = int(val[0])
height = int(val[1])
resizedImage = myLibrary.resize(image,width,height)
cv2.imshow("resizedImage",resizedImage)
cv2.waitKey(0)
