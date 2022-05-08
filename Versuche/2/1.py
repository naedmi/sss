import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def extract_bounds(image):
    height, width = image.shape
    image_blur = cv2.GaussianBlur(image, (5,5), 5)
    image_thresh = cv2.Canny(image_blur, 10,40)
    lines = cv2.HoughLines(image_thresh, 1, np.pi / 180, 150, None, 0, 0)

    line_xs = [[0,0],[width,width]]
    for line in lines:
        [rho, theta] = line[0]
        a = math.cos(theta)
        b = math.sin(theta)

        x0 = int(a * rho)
        x1 = int(x0 + height*b) if a < 0 else int(x0 - height*b)

        line_xs.append([x0,x1])

    line_xs.sort(key=lambda line : line[0])

    bounds = []
    for i in range(1, len(line_xs)):
        prev_xs = line_xs[i-1]
        current_xs = line_xs[i]

        left = max(prev_xs)
        right = min(current_xs)
        top = 5
        bottom = height-5
        bounds.append([top, right, bottom, left])

    return bounds

def print_data(image, bounds, labels):
    steps = []
    for top, right, bottom, left in bounds:
        steps.append(image[top:bottom, left:right])


    for i in range(len(steps)):
        mean = np.mean(steps[i])
        std = np.std(steps[i])
        print("%s    mean: %f std: %f" % (labels[i],mean, std))

    print("\n")


labels = ["white","gray1","gray2","gray3", "black"]
    
image = cv2.imread('./data/grauwertkeil0.png', 0)
bounds = extract_bounds(image)
print("Grauwertkeil:")
print_data(image, bounds, labels)


image_corrected = cv2.imread('./data/grauwertkeil_korrigiert3.png', 0)
bounds_corrected = extract_bounds(image_corrected)
print("Grauwertkeil korrigiert:")
print_data(image_corrected, bounds_corrected, labels)
