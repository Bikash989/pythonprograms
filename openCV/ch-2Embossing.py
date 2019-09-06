# take each pixel and replace it with a shadow or a highlight
# if lot of contrast is present in the image, then we will
# either replace it with a white pixel(highlight) or a dark pixel(shadow)
# and it depends on which direction we are embossing
import cv2
import numpy as np 
import myLibrary
image = cv2.imread('image.jpg')
newimage = myLibrary.resize(image,500)

#generating the kernels
emboss_south_west = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
emboss_south_east = np.array([[-1,-1,0],[-1,0,1],[-0,1,1]])
emboss_north_west = np.array([[1,0,0],[0,0,0],[0,0,-1]])

print(emboss_south_west)
print(emboss_south_east)
print(emboss_north_west)

# convert the image to grayscale
gray_img = cv2.cvtColor(newimage,cv2.COLOR_BGR2GRAY)

# apply ther kernels to the grayscale image and adding the offset
output_1 = cv2.filter2D(gray_img,-1,emboss_south_west)
output_2 = cv2.filter2D(gray_img,-1,emboss_south_east)
output_3 = cv2.filter2D(gray_img,-1,emboss_north_west)

cv2.imshow("Embossing-South West",output_1)
cv2.imshow("Embossing-South East",output_2)
cv2.imshow("Embossing-North West",output_3)
cv2.waitKey(0)