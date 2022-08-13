from PIL import Image
import os

# 设定 png 图片目录
path = "D://Users//haoning//Downloads//480//"
files = os.listdir(path)

for file in files:
    img = Image.open(path + file)
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(path + file, "PNG")
    print("Processing, please wait...")

print("All done!")
