import os
from PIL import Image


directory = "z:\\Python\\All_python\\foto\\"

resize_in_percent = 50
resize_x_to_min = 700
resize_y_to_min = 1000
if resize_x_to_min+ resize_y_to_min != 0:
    resize_in_percent = False

with os.scandir(path=directory) as it:
    for entry in it:
        if not entry.is_file():
            print("dir:\t" + entry.name)
        else:
            print("file:\t" + entry.name)
            img_obj = Image.open(directory + entry.name)
            width_size = height_size = 0
            if resize_in_percent:
                percent = 100 / resize_in_percent
                width_size = int(float(img_obj.size[0])/percent)
                height_size = int(float(img_obj.size[1])/percent)
            else:
                if resize_x_to_min:
                    delta = resize_x_to_min / float(img_obj.size[0])
                    width_size = int(float(img_obj.size[0]) * delta)
                    height_size = int(float(img_obj.size[1]) * delta)
                else:
                    delta = resize_y_to_min / float(img_obj.size[1])
                    width_size = int(float(img_obj.size[0]) * delta)
                    height_size = int(float(img_obj.size[1]) * delta)
            img_obj = img_obj.resize((width_size, height_size), Image.ANTIALIAS)
            img_obj.save(directory + entry.name)

