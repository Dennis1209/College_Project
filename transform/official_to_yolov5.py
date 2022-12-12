from PIL import Image
for i in range(1,1001) :
    print(i)
    in_file = "/content/drive/MyDrive/yolov5/dataset/old_labels/train/img" #原labels(官方版本)所在路徑/img
    out_file = "/content/drive/MyDrive/yolov5/dataset/labels/train/img"    #新labels(yolov5)所在路徑/img
    img_file = "/content/drive/MyDrive/yolov5/dataset/images/train/img"    #圖片所在路徑/img
    b = str(i)
    b = b.zfill(4)
    in_filename = in_file + b + ".txt"
    out_filename = out_file + b + ".txt"
    img_filename = img_file + b + ".png"
    img = Image.open(img_filename)
    with open(in_filename,"r") as in_f: 
        for line in in_f: 
            l1 = line.replace('\n','')
            l1 = line.split(',')
            with open(out_filename, 'a') as out_f:
                out_f.write(f"{l1[0]} {round(float((float(l1[1]) + float(l1[3])/2)/img.width),6)} {round(float((float(l1[2]) + float(l1[4])/2)/img.height),6)} {round(float(float(l1[3])/img.width),6)} {round(float(float(l1[4])/img.height),6)}\n")