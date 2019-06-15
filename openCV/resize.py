import cv2

#read image
image = cv2.imread('testimage.jpg')
cv2.imshow("image", image)
print(image.shape)

#SYNTAX: cv2.resize(originalImage, dimension)
resized = cv2.resize(image,(300,300))
cv2.imshow("Resized (Wdith)", resized)
cv2.imshow("new image", cv2.resize(image, (300,300), interpolation = cv2.INTER_AREA))

print(resized.shape)
cv2.waitKey(0)
