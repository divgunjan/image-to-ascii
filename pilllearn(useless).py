from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from collections import Counter

# Load and resize image
img = Image.open("adams.jpg")
width, height = img.size
aspect_ratio = height / width
new_width = 150
new_height = int(aspect_ratio * new_width * 0.85)
image = img.resize((new_width, new_height))

# Enhance contrast
image = ImageEnhance.Contrast(image).enhance(1.5)

# ASCII chars (dark -> light)
ascii_chars = "■$@%•*/|()[]2?1-_+~<>i!lI;:,'."

def brightness(pixel):
    r, g, b = pixel
    return 0.299*r + 0.587*g + 0.114*b

def color_distance(c1, c2):
    return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)**0.5

pixels = list(image.getdata()) #g

# Find dominant color
dominant_color = Counter(pixels).most_common(1)[0][0]
print("Dominant color:", dominant_color)

# Settings (best settin: 45,15)
dark_threshold = 40
dominant_threshold = 15

ascii_map = []
for p in pixels:
    b = brightness(p)
    if b < dark_threshold: # darkest areas are left blank 
        ascii_map.append((" ", p)) 
    elif color_distance(p, dominant_color) < dominant_threshold:
        ascii_map.append((".", p))  
    else:
        index = int(b * len(ascii_chars) / 256)
        ascii_map.append((ascii_chars[index], p))

# Create blank output image
font = ImageFont.load_default()  # or truetype
bbox = font.getbbox("A")
char_width = bbox[2] - bbox[0]
char_height = bbox[3] - bbox[1]
output_img = Image.new("RGB", (new_width * char_width, new_height * char_height), "black")
draw = ImageDraw.Draw(output_img)

# Draw ASCII characters
for y in range(new_height):
    for x in range(new_width):
        char, color = ascii_map[y * new_width + x]
        if char != " ":  # Skip drawing blanks
            draw.text((x * char_width, y * char_height), char, fill=color, font=font)

output_img.save("ascii_art.jpg")
print("Colored ASCII image saved as 'ascii_art.jpg'")