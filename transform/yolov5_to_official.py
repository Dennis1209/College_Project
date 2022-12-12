from PIL import Image
import math
for i in range(1001,2001) : #圖片編號
    print(i)
    in_file = "/home/u2339555/yolov5/runs/detect/yolov5_5fold/origin_labels/img"  #原labels(yolov5)所在路徑/img
    out_file = "/home/u2339555/yolov5/runs/detect/yolov5_5fold/labels/img"        #新labels(官方版本)所在路徑/img
    img_file = "/home/u2339555/yolov5/runs/detect/yolov5_5fold/img"               #圖片所在路徑/img
    b = str(i)
    b = b.zfill(4)
    in_filename = in_file + b + ".txt"
    out_filename = out_file + b + ".txt"
    img_filename = img_file + b + ".png"
    img = Image.open(img_filename)

    with open(in_filename,"r") as in_f: 
        for line in in_f: 
            l1 = line.replace('\n','')
            l1 = line.split(' ')
            num1 = math.floor((float(l1[1]) - float(l1[3])/2) * img.width)
            num2 = math.floor((float(l1[2]) - float(l1[4])/2) * img.height)
            num3 = math.floor(float(l1[3]) * img.width)
            num4 = math.floor(float(l1[4]) * img.height)
            num5 = num1 + num3
            num6 = num2 + num4
            if(num1 < 0):
                num1 = 0
                num3 = num5
            if(num2 < 0):
                num2 = 0
                num4 = num6
            if(num5 > img.width):
                num3 = img.width - num1
            if(num6 > img.height):
                num4 = img.height- num2
            with open(out_filename, 'a') as out_f:
                out_f.write(f"{int(l1[0])},{num1},{num2},{num3},{num4}\n")