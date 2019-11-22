from PIL import ImageEnhance
from PIL import Image

image = Image.open("bikash.JPG")
# enhancer=ImageEnhance.Brightness(image)
images = []
for i in range(0,10):
    # images.append(enhancer.enhance(i/10))
    images.append(image)

#make contact sheet
distance = 150
first_image = images[0]

contact_sheet=Image.new(first_image.mode, ((first_image.width+distance)*3,(first_image.height+distance)*3),(255,255,255))

x=0
y=0
for img in images[1:]:
    contact_sheet.paste(img, (x,y))
    if x+first_image.width+distance == contact_sheet.width:
        x=0
        y=y+first_image.height+distance
    else:
        x=x+first_image.width+distance

contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.save("contact_sheet.jpeg")
