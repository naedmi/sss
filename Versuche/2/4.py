import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

weissbild = cv2.imread('./data/weissbild_avg.png', 0)
dunkelbild = cv2.imread('./data/dunkelbild_avg.png', 0)

#deadpixels
height, width = weissbild.shape

deadpixel_image = cv2.cvtColor(weissbild, cv2.COLOR_GRAY2BGR)
dead_pixels = []

for y in range(height):
    for x in range(width):
        pixel = weissbild[y,x]
        if(pixel == 0):
            dead_pixels.append([x,y])

if(len(dead_pixels) == 0): print("keine deadpixel")
else: print(dead_pixels)

for x,y in dead_pixels:
    cv2.circle(deadpixel_image, (x,y), 10, (255,0,0), 1)

plt.title("dead pixels")
plt.imshow(deadpixel_image)
plt.show()


#stuckpixels
height, width = dunkelbild.shape

stuckpixel_image = cv2.cvtColor(dunkelbild, cv2.COLOR_GRAY2BGR)
stuck_pixels = []

for y in range(height):
    for x in range(width):
        pixel = dunkelbild[y,x]
        if(pixel == 255):
            stuck_pixels.append([x,y])


if(len(stuck_pixels) == 0): print("keine stuckpixel")
else: print(stuck_pixels)

for x,y in stuck_pixels:
    cv2.circle(stuckpixel_image, (x,y), 10, (255,0,0), 1)

plt.title("stuck pixels")
plt.imshow(stuckpixel_image)
plt.show()