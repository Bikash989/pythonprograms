import numpy as np
import cv2

# translate image with value x and y
def translate(img, x, y):
    translationMatrix = np.float32([[1, 0, x], [0, 1, y]])
    shiftedImage = cv2.warpAffine(img, translationMatrix, (img.shape[1], img.shape[0]))
    return shiftedImage

# rotate image
def rotate(image, angle, center = None, scale = 1.0):
    (h,w) = image.shape[:2]

    if center is None:
        center = (w /2, h/2)

    translationMatrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotatedImage = cv2.warpAffine(image, translationMatrix, (w, h))

    return rotatedImage

#resize image
def resize(image, width=None, height=None, inter = cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]

    # resize using either width or height, if none mentioned, return original image
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w*r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resizedImage = cv2.resize(image, dim, interpolation = inter)
    return resizedImage
