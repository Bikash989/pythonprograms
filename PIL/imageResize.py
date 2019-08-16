'''
We will make use of Python Imaging Library to resize an image
'''
from PIL import Image

res_size = (300,300)          # a 300 by 300 size for the image
filename = 'alladin.png'      # put your file name here
image = Image.open(filename)  # open the image
image.thumbnail(res_size)     # use thumbnail method to resize
image.save('alladin_300.png') # save the new image
