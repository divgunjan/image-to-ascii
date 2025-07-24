from PIL import Image,ImageDraw,ImageFont
import sys
import string
import random

system = sys.argv[0]
img = Image.open("testingimage.png")
pixels = img.getdata() #obtain the number of pixels

#resizing the image unwillingly
width,height = img.size
aspect_ratio = height/width #stays constant
new_width = 150
new_height = aspect_ratio*new_width
image = img.resize((new_width,int(new_height)))

grayscale = image.convert('L')
character = [
    "@",
    "#",
    "&",
    "%",
    "$",
    "?",
    "*",
    "!",
    "+",
    "=",
    ":",
    ";",
    ",",
    "'",
    "/",
    "."
]

gray_pixels = list(grayscale.getdata())

new_pixels = [character[pixel // 16] for pixel in gray_pixels]
new_pixels = "".join(new_pixels)

new_pixel_count = len(new_pixels)

final_image=[new_pixels[index: index+new_width] for index in range(0, new_pixel_count, new_width)]
final_image = "\n".join(final_image)

with open("ascii_file.txt","w") as file:
    file.write(final_image)
