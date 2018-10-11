from PIL import Image,ImageDraw,ImageFilter

im = Image.open('james.jpg')
w,h = im.size
print('Origin image size is : %s,%s'%(w,h))
im.thumbnail((w/2,h/2))
print('Change image size is:%s,%s'%(w,h))
im.save('thum.jpg','jpeg')
image =im.filter(ImageFilter.BLUR)
image.save('thummm.jpg','jpeg')

