from PIL import Image
import os

# 设定 png 图片目录，不要使用 C 盘路径，在 Windows 下 C 盘路径会受到保护。
path = "D://yourpath//"
files = os.listdir(path)

for file in files:
    img = Image.open(path + file)
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for item in datas:
        # 移除白色以及附近色彩
        if item[0] > 246 and item[1] > 246 and item[2] > 246:
            newData.append((255, 255, 255, 0))
        # 移除黑色以及附近色彩
        elif item[0] < 64 and item[1] < 64 and item[2] < 64:
            newData.append((0, 0, 0, 0))
        # 移除顶部的线条
        elif item[0] == 223 and item[1] == 223 and item[2] == 223:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(path + file, "PNG")
    print("Processing, please wait...")

print("All done!")
