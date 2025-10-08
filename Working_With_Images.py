from PIL import Image, ImageFilter

# WORKING WITH IMAGES
jay = Image.open("jay.jpg")
print(jay.size)
print(jay.format)
jay.show()


# Crop Image
area = (100, 100, 300, 375)
new = Image.crop(area)
new.show()


# Pasting image on another
jay = Image.open("jay.jpg")
kay = Image.open("kay.jpg")
jay.paste(kay)
jay.show()

# Breaking and seperating image channels
jay = Image.open("jay.jpg")
print(jay.mode) #RGB
r, g, b = jay.split()

r.show()
g.show()
b.show()


# Merging Images
jay = Image.open("jay.jpg")
kay = Image.open("kay.jpg")

r1, g1, b1  = jay.split()
r2, g2, b2  = kay.slit()

new = Image.merge("RGB", (r2, g1, b1))
new.show()


# Resize, flip, rotate
jay = Image.open("jay.jpg")
square = jay.resize((250, 250))
square.show()
# flip = jay.transpose(Image.FLIP_TOP_BOTTOM)
flip = jay.transpose(Image.FLIP_LEFT_RIGHT)
flip.show()
spin = jay.transpose(Image.ROTATE_90)
spin.show()


# Modes & Filters
jay = Image.open("jay.jpg")
black_white = jay.convert("L")
blur = jay.filter(ImageFilter.BLUR)
detail = jay.filter(ImageFilter.DETAIL)
edge = jay.filter(ImageFilter.FIND_EDGES)

detail.show()
blur.show()
black_white.show()
