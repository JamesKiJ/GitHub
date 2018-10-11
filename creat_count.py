from PIL import Image,ImageDraw,ImageFilter,ImageFont
import random

def randchar():
    return  chr(random.randint(60,90))

def rand_color():
    return  (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rand_cyc():
    return (random.randint(-90,90))

def rand_color2():
    return  (random.randint(32,127),random.randint(32,127),random.randint(32,127))


weight =60*4
height =90
image = Image.new('RGB',(weight,height),(255,255,255))
front =ImageFont.truetype('Arial.ttf',36)
draw = ImageDraw.Draw(image)


for x in range(weight):
    for y in range(height):
        draw.point((x,y),fill=rand_color())

for  i in range(4):
    draw.text((60*i+10,10),randchar(),font=front,fill=rand_color2())

image =image.filter(ImageFilter.BLUR)
image1 =image.rotate(rand_cyc())
image.save('yes.jpg','jpeg')
