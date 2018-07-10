from PIL import Image
from PIL import ImageFilter

im = Image.open("image.png")
assert isinstance(im, Image.Image)
size = (256, 144)
box = (500, 100, 1300, 900)
_box = (400, 0, 1200, 800)
print(im.format, im.size, im.mode)
# im.show()
# im.thumbnail(size)
# im.save("thumbnail.png", "PNG")
# re = im.resize(size)
# im.show()
# # re.show()
# region = im.crop(box)
# im.paste(region, _box)
# im.show()
# # region.show()
# for i in range(0, 8):
#     out = region.rotate(45 * i)
#     out.show()
# for i in range(1, 10, 2):
#     out = region.resize((100*i, 100*i))
#     out.show()
# r, g, b, a = im.split()
# r.show()
# im = Image.merge("RGB", (b, g, b))
# im.show()
# out = im.point(lambda i: i * 0.1)
# split the image into individual bands
source = im.split()

R, G, B = 0, 1, 2

# select regions where red is less than 100
mask = source[R].point(lambda i: i < 100 and 255)

# process the green band
out = source[G].point(lambda i: i * 0.1)

# paste the processed band back, but only where red was < 100
source[G].paste(out, None, mask)

# build a new multiband image
im = Image.merge(im.mode, source)
im.show()