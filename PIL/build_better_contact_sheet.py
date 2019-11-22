
import PIL
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageColor
from PIL import ImageEnhance


# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

w,h = image.size

fontsize=75
def drawImg(text):
    new_image = Image.new(image.mode,((w,fontsize)),(0,0,0))
    draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype("readonly/fanwood-webfont.ttf",fontsize)
    draw.text((0,0), text,(255,255,255),font = font)
    
    return new_image    
    
def threeRows(image,width,height,intensity, val):    
    copyImage = image.copy()
    for x in range(width):
        for y in range(height):
            r,g,b = image.getpixel((x,y))
            # set intensity to r or g or b accordingly
            if(val == 1):
                r = int(intensity * r)
            elif(val == 2):
                g = int(intensity * g)
            else:
                b = int(intensity * b)
            copyImage.putpixel( (x,y), (r,g,b))
    return copyImage

images = []
textImages = [] # text written image is stored here
intensity = [0.1,0.5,0.9]
for i in range(1,10):
    if(i <= 3):
        val = 1
    elif(i <= 6):
        val = 2
    else:
        val = 3
    returnedImage = threeRows(image,w,h,intensity[(i%3)-1],val)
    images.append(returnedImage)
    #for draw
    
    text="channel {} intensity {}".format(val-1,intensity[(i%3)-1])
    drawImage = drawImg(text)
    dw,dh=drawImage.size
    returnedImage = threeRows(drawImage,dw,dh,intensity[(i%3)-1],val)
    textImages.append(returnedImage)

    
distance = 75
first_image = images[0]

contact_sheet=Image.new(first_image.mode, ((first_image.width)*3,(first_image.height+distance)*3))

x=0
y=0
count=1 # this for printing 3 textimages
index = 0
prev = 0
for img in images:
    contact_sheet.paste(img, (x,y))
    if x+first_image.width == contact_sheet.width:
        
        # before adding height, insert textfotos
        
        x=0
        y+=first_image.height
        for textimg in textImages[count-3:count]:  #fix this
            contact_sheet.paste(textimg, (x,y))
            x += first_image.width
        prev=count            
            
        x=0
        y=y+distance
    else:
        x=x+first_image.width
        count += 1

contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))

display(contact_sheet)
  
