import numpy as np
import cv2

mycanvas = np.zeros((400,400,3), dtype= "uint8") #drawing area
green = (0,255,0)
cv2.line(mycanvas, (0,0), (400,400), green, 40)
# cv2.imshow("My Drawing Area", mycanvas)

blue = (255,0,0)
# cv2.line(drawingarea, starting pos, ending pos, color, thickness(in pixel))
cv2.line(mycanvas, (400,0), (0,400), blue, 40)

white = (0,0,255)
cv2.line(mycanvas, (200,200), (200,200), white, 50)



cv2.imshow("My Drawing Area ", mycanvas)

mycanvas2 = np.zeros((400,400,3), dtype="uint8")
cv2.rectangle(mycanvas2,(20,20), (70,70), green)
cv2.rectangle(mycanvas2, (200,50), (225,125), blue, -1) # -ve thickness, fills inside the rectangle
cv2.imshow("Rectangel",mycanvas2)
cv2.waitKey(0)
