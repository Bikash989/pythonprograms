# Motion Blur
'''
  read image.
  create motionblur kernel: averages a pixel in a particular direction
  it's like bidirectional low pass filter.
  a 3x3 motion kernel look like. (make middle row ones)
      [0 0 0]
  M = [1 1 1]
      [0 0 0]
    This blurs the image in the horizontal direction
    amt of blurring depends on the size of the kernel.
    and we use filter2D to apply the kernel to blur the image
'''
import cv2
import numpy as np 
import myLibrary
im = cv2.imread('image.jpg')
newimage = myLibrary.resize(im,500)
cv2.imshow("OriginalImage",newimage)
size = 15

# now generate the kernel
kernel_motion_blur = np.zeros((size,size))  # 15x15
# print(kernel_motion_blur)
# print()
kernel_motion_blur[int((size-1)/2), :] = np.ones(size) #make ones inthe middle rows
# print(kernel_motion_blur)
kernel_motion_blur = kernel_motion_blur/size #only middle row is affected
# print()
# print(kernel_motion_blur)

# applying the kernel to the input image
output = cv2.filter2D(newimage,-1,kernel_motion_blur)
cv2.imshow("Applied Motion Blue",output)
cv2.waitKey(0)