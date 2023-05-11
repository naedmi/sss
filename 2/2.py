import numpy as np
import cv2


def create_dark_frame():
    darkframes = [None] * 10
    # dark frame vectors
    vec0 = vec1 = vec2 = vec3 = vec4 = vec5 = vec6 = vec7 = vec8 = vec9 = np.zeros((480, 640))
    vector = [vec0, vec1, vec2, vec3, vec4, vec5, vec6, vec7, vec8, vec9]
    # average vector
    average = np.zeros((480, 640))

    # for all 10 dark frames
    for x in range(0, 10):
        # load
        darkframes[x] = cv2.imread(f'data/dunkelbild{x}.png', cv2.IMREAD_GRAYSCALE)
        # darkframes[x] = darkframes[x].astype('float32')

        for pxl_height in range(0, 480):
            for pxl_width in range(0, 640):
                # fill vector with pixel values
                vector[x][pxl_height, pxl_width] = darkframes[x][pxl_height, pxl_width]

    for pxl_height in range(0, 480):
        for pxl_width in range(0, 640):
            pxl_sum = 0
            # add pixel values of all 10 dark frames
            for file in range(0, 10):
                pxl_sum += vector[file][pxl_height, pxl_width]
            # get average
            average[pxl_height, pxl_width] = float(pxl_sum / 10)

    # load as grayscale
    image = cv2.imread('data/dunkelbild_avg.png', 0)
    for x in range(0, 480):
        for y in range(0, 640):
            # create average image
            image[x, y] = average[x, y]

    cv2.imwrite('data/dunkelbild_avg.png', image)
    cv2.imshow('image', image)

    # maximize contrast
    image_contrast = cv2.equalizeHist(image, image)

    cv2.imwrite('data/dunkelbild_kontrast.png', image_contrast)
    cv2.imshow('image_contrast', image_contrast)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def correct():
    # load grauwertkeil as grayscale
    gray = cv2.imread('data/grauwertkeil0.png', 0)
    # load dark frame average
    dark_avg = cv2.imread('data/dunkelbild_avg.png')

    # subtract dark frame from gray image
    corrected = cv2.subtract(gray, dark_avg)

    cv2.imwrite("data/grauwertkeil_korrigiert.png", corrected)
    cv2.imshow('corrected', corrected)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    create_dark_frame()
    # correct()
