import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt
from PIL import Image
import random
import math

WIDTH = 50
HEIGHT = 50
CHANNELS = 3
NUM_OF_COLORS = 5

CRITICAL_DISTANCE = 10


def color_constraint(image, color, x, y):
    x_min = x - CRITICAL_DISTANCE
    x_max = x + CRITICAL_DISTANCE
    y_min = y - CRITICAL_DISTANCE
    y_max = y + CRITICAL_DISTANCE

    for kernel_x in range(x_min, x_max):
        for kernel_y in range(y_min, y_max):
            if kernel_x >= 0 and kernel_x < WIDTH and kernel_y >= 0 and kernel_y < HEIGHT:
                if int(math.sqrt(
                        abs(kernel_x - x) ** 2 + abs(kernel_y - y) ** 2)) == CRITICAL_DISTANCE:
                    if np.array_equal(color, image[kernel_y][kernel_x]):
                        return False

    return True


def get_pixel_by_NH(image, colors, x, y):
    pixel = np.zeros((CHANNELS), dtype=np.uint8)

    for i in range(NUM_OF_COLORS):
        if color_constraint(image, colors[i], x, y):
            return colors[i]

    return pixel


def get_dist_color_list(num_of_colors):
    colors = np.zeros((NUM_OF_COLORS, CHANNELS), dtype=np.uint8)

    for i in range(num_of_colors):
        colors[i][0] = int(random.random() * 256)
        colors[i][1] = int(random.random() * 256)
        colors[i][2] = int(random.random() * 256)

    return colors


def get_HN_image(num_of_colors=3):
    image = np.zeros((HEIGHT, WIDTH, CHANNELS), dtype=np.uint8)
    colors = get_dist_color_list(num_of_colors)

    # for x in range(WIDTH):
    # for y in range(HEIGHT):
    for i in range(10000):
        x = int(random.random() * WIDTH)
        y = int(random.random() * HEIGHT)
        image[y][x] = get_pixel_by_NH(image, colors, x, y)

    return image


def main():
    disp_img = Image.fromarray(get_HN_image(NUM_OF_COLORS), 'RGB')
    disp_img.show()
    disp_img.save("test.bmp", "bmp")

  
if __name__== "__main__":
  main()
