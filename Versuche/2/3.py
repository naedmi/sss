import numpy as np
import cv2


def create_white_frame():
    whiteframes = [None] * 10
    # dark frame vectors
    vec0 = vec1 = vec2 = vec3 = vec4 = vec5 = vec6 = vec7 = vec8 = vec9 = np.zeros((480, 640))
    vector = [vec0, vec1, vec2, vec3, vec4, vec5, vec6, vec7, vec8, vec9]
    # average vector
    average = np.zeros((480, 640))

    # for all 10 dark frames
    for x in range(0, 10):
        # load
        whiteframes[x] = cv2.imread(f'data/weissbild{x}.png', cv2.IMREAD_GRAYSCALE)
        # darkframes[x] = darkframes[x].astype('float32')

        for pxl_height in range(0, 480):
            for pxl_width in range(0, 640):
                # fill vector with pixel values
                vector[x][pxl_height, pxl_width] = whiteframes[x][pxl_height, pxl_width]

    for pxl_height in range(0, 480):
        for pxl_width in range(0, 640):
            pxl_sum = 0
            # add pixel values of all 10 dark frames
            for file in range(0, 10):
                pxl_sum += vector[file][pxl_height, pxl_width]
            # get average
            average[pxl_height, pxl_width] = float(pxl_sum / 10)

    # load as grayscale
    image = cv2.imread("data/weissbild_avg.png", 0)
    for x in range(0, 480):
        for y in range(0, 640):
            # create average image
            image[x, y] = average[x, y]

    cv2.imwrite("data/weissbild_avg.png", image)
    cv2.imshow('white frame avg', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def correct_white_frame():
    # load white frame average as grayscale
    white_avg = cv2.imread('data/weissbild_avg.png', 0)
    white_avg = cv2.cvtColor(white_avg, cv2.COLOR_BGR2RGB)
    # load dark frame average
    dark_avg = cv2.imread('data/dunkelbild_avg.png')
    dark_avg = cv2.cvtColor(dark_avg, cv2.COLOR_BGR2RGB)

    # subtract dark frame from white frame
    corrected = cv2.subtract(white_avg, dark_avg)

    cv2.imwrite('data/weissbild_korrigiert.png', corrected)
    cv2.imshow('white frame corrected', corrected)

    # maximize contrast
    corrected = cv2.imread('data/weissbild_korrigiert.png', 0)
    image_contrast = cv2.equalizeHist(corrected, corrected)

    cv2.imwrite('data/weissbild_kontrast.png', image_contrast)
    cv2.imshow('white frame max contrast', image_contrast)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def correct():
    # load grauwertkeil as grayscale
    gray = cv2.imread('data/grauwertkeil0.png', 0)
    # load dark frame average
    dark_avg = cv2.imread('data/dunkelbild_avg.png', 0)
    # load white frame
    white_corrected = cv2.imread('data/weissbild_avg.png', 0)

    # normalize white frame
    white_corrected = cv2.divide(white_corrected, np.mean(white_corrected))
    print(f'white frame mean: {np.mean(white_corrected)}')

    # subtract dark frame from gray image
    corrected = cv2.subtract(gray, dark_avg)

    # divide gray image by white frame
    corrected = cv2.divide(corrected, white_corrected)

    cv2.imwrite("data/grauwertkeil_korrigiert3.png", corrected)
    cv2.imshow('grauwertkeil corrected with dark frame and white frame', corrected)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    create_white_frame()
    correct_white_frame()
    correct()
