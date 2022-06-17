from random import randint
from PIL import Image
import numpy as np
from boiler_plate import graphics_c_inicio, graphics_c_final

image = Image.open('images/0.png')
width, heigth = image.size

# Converted image to RGB
image_rgb = image.convert('RGB')

f = open("test.C", 'w')
f.write(graphics_c_inicio)

for i in range(width):
    for j in range(heigth):
      pixel_values = image_rgb.getpixel((i,j))
      if not np.array_equal(pixel_values, [255,255,255]):
        if pixel_values[0] > 150 and pixel_values[1] < 100 and pixel_values[2] < 100:
          f.write(f"setcolor(RED);")
        elif pixel_values[0] < 90 and pixel_values[1] < 90 and pixel_values[2] < 90:
          f.write(f"setcolor(BLACK);")
        f.write(f"circle({i+150},{j+50},1);")
        f.write(f"setcolor(WHITE);")

f.write(graphics_c_final)
f.close()