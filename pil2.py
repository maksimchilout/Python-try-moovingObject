from PIL import Image, ImageFilter

original = Image.open("1.JPG")
img = original.filter(ImageFilter.CONTOUR) # CONTOUR doing only contour of image; EMBOSS - tesnenie; FIND_EDGES - obvodka edges
img.save("6.jpg")
img.show()

