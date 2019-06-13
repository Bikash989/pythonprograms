import cv2
import numpy as np
drawingArea = np.zeros((400,400,3), dtype = "uint8") #blank canvas
height = drawingArea.shape[0]
width = drawingArea.shape[1]

x,y = int(width/2), int(height/2)

blue = (255,0,0)

for r in range(0,175,25):
    cv2.circle(drawingArea, (x,y), r, blue)
cv2.imshow("Draw Circle", drawingArea)
cv2.waitKey(0)
