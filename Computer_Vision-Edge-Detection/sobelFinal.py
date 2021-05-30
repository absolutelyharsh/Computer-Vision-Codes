import numpy as np
import cv2
import imageio


def vertical_detection(og_img, verticalFilter):
    # Creating a padded image of zeros
    padded_image = np.zeros((og_img.shape[0] + 2, og_img.shape[1] + 2))
    # leaving first and last row and column. Padded image replaced with orignal image
    padded_image[1:-1, 1:-1] = og_img
    # Creating an array of zeros with padding
    verticalEdge = np.zeros_like(og_img)
    # Moving the filter over the image
    for x in range(og_img.shape[1]):
        for y in range(og_img.shape[0]):
            verticalEdge[y, x] = (verticalFilter * padded_image[y:y + 3, x:x + 3]).sum()
    return verticalEdge


def horizontal_detection(og_img, horizontalFilter):
    # Creating a padded image of zeros
    padded_image = np.zeros((og_img.shape[0] + 2, og_img.shape[1] + 2))
    # leaving first and last row and column. Padded image replaced with orignal image
    padded_image[1:-1, 1:-1] = og_img
    # Creating an array of zeros with padding
    horizontalEdge = np.zeros_like(og_img)
    # Moving the filter over the image
    for x in range(og_img.shape[1]):
        for y in range(og_img.shape[0]):
            horizontalEdge[y, x] = (horizontalFilter * padded_image[y:y + 3, x:x + 3]).sum()
    return horizontalEdge


def gradient_mag(verticalScore, horizontalScore):
    edge_score = (verticalScore ** 2 + horizontalScore ** 2) ** .5
    return edge_score


if __name__ == '__main__':
    # Import image
    img = cv2.imread('test-pattern.tif', cv2.IMREAD_GRAYSCALE)
    # Filter for Row
    # [[-1  2 -1
    #    0  0  0
    #    1  2  1]]
    verticalFilter = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    # Filter for Column
    # [[-1  0  1
    #   -2  0  0
    #   -1  0  1]]
    horizontalFilter = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    # Score For Vertical
    verticalScore = vertical_detection(img, verticalFilter)
    # Score For Horizontal
    horizontalScore = horizontal_detection(img, horizontalFilter)
    # Gradient Magnitude
    gradientMag = gradient_mag(verticalScore, horizontalScore)
    # Saving Image
    imageio.imwrite('sobel_output1.jpg', gradientMag)
