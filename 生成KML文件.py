# -*- coding: utf-8 -*-

"""
填入相关信息，生成 KML 文件

最后，将生成后的 KML 文件放到图片目录下，然后打 ZIP 压缩包，重命名为 KMZ 格式即可
"""

# 信息
name = "1979年1月至2018年12月的中国逐日太阳辐射"
begin_year = 1979
begin_month = 1
end_year = 2018
end_month = 12
num = 1

# 开始写入
with open(name + ".kml", "w", encoding="utf-8") as f:
    # KML 头部文件写入
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    f.write('<Folder>\n')
    f.write('<name>' + name + '</name>\n\n')

    # 循环写入每个数据
    for year in range(begin_year, end_year+1):
        for month in range(begin_month, end_month+1):
            f.write('<GroundOverlay>\n')

            if month < 10:
                f.write('<name>' + str(year) + '-0' + str(month) + '</name>\n')
                f.write('<TimeSpan>\n')
                f.write('<begin>'+ str(year) + '-0' + str(month) + '</begin>\n')
            else:
                f.write('<name>' + str(year) + '-' + str(month) + '</name>\n')
                f.write('<TimeSpan>\n')
                f.write('<begin>'+ str(year) + '-' + str(month) + '</begin>\n')

            f.write('</TimeSpan>\n')
            f.write('<Icon><href>' + str(num) + '.png</href></Icon>\n')
            f.write('<LatLonBox>\n')
            f.write('<west>-180.0</west>\n')
            f.write('<north>90.0</north>\n')
            f.write('<east>180.0</east>\n')
            f.write('<south>-90.0</south>\n')
            f.write('</LatLonBox>\n')
            f.write('</GroundOverlay>\n\n')
            num = num + 1

    # KML 尾部文件写入
    f.write('</Folder>\n')
    f.write('</kml>\n')

f.close()
print("All done!")