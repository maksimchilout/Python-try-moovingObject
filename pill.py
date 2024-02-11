from PIL import Image, ImageFilter

size = (1920, 1080)
original = Image.open("1.JPG")
original.thumbnail(size)
original.save("2.jpg")
original.show()
print(original.format, original.size, original.mode)
