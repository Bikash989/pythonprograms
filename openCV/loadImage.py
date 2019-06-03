import cv2
print("OpenCV version:")
print(cv2.__version__)
img = cv2.imread("testimage.jpg")  #reading image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting to gray scale

cv2.imshow("Over the clouds", img) #showing image
cv2.imshow("Over the clouds - gray", gray)

cv2.imwrite('output.jpg', gray) #writing a new file with gray
cv2.waitKey(0)
cv2.destroyAllWindows()
