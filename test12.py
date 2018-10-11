from PIL import Image,ImageDraw,ImageFont,ImageFilter

blank = Image.new("RGB", [1024, 768], "white")
drawObject = ImageDraw.Draw(blank)
text = "I love python!"
drawObject.rectangle((100, 100, 600, 600), fill=128)
# 字体对象1为simsunb，字大小为36号
Font1 = ImageFont.truetype("/Library/Fonts/Sana.ttc", 36)
# 字体对象2在ttc中第一个（我也不知道具体是什么字形），字大小为36号
Font2 = ImageFont.truetype("/Library/Fonts/Sana.ttc", 36, index=0)
# 字体对象2在ttc中第二个，字大小为36号
Font3 = ImageFont.truetype("/Library/Fonts/Sana.ttc", 36, index=1)
# 字体对象1为SHOWG，字大小为48号
Font4 = ImageFont.truetype("/Library/Fonts/Sana.ttc", 48)

# 利用text函数添加文字
drawObject.text([200, 200], text, font=Font1)
drawObject.text([200, 250], text, font=Font2)
drawObject.text([200, 300], text, font=Font3)
drawObject.text([200, 400], text, font=Font4)

blank.save('code.jpg','jpeg')

