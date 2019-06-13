#load image and display it's dimension
import cv2
image = cv2.imread("openCV/output.jpg")
print(image.shape) #displays dimension
cv2.imshow("Image", image)
(b,g,r) = image[10,20]
print(b,g,r)
corner = image[0:100, 0:100] #slicing an area from image 100 X 100
cv2.imshow("corner: ", corner)

image[0:100, 0:100] = (128,0,0) #100X100 area is turned into Blue
cv2.imshow("Changed", image)
cv2.waitKey(0)
