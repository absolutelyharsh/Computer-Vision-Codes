import numpy as np
import imageio


def mean_filter(og_img, meanFilter):
    # Creating a padded image of zeros
    padded_image = np.zeros((og_img.shape[0] + 2, og_img.shape[1] + 2))
    # leaving first and last row and column. Padded image replaced with orignal image
    padded_image[1:-1, 1:-1] = og_img
    # Creating an array of zeros with padding
    meanNoiseCancellation = np.zeros_like(og_img)
    # Moving the filter over the image
    for x in range(og_img.shape[1]):
        for y in range(og_img.shape[0]):
            meanNoiseCancellation[y, x] = (meanFilter * padded_image[y:y + 3, x:x + 3]).sum()
    return meanNoiseCancellation


def median_filter(og_img):
    # Creating a padded image of zeros
    padded_image = np.zeros((og_img.shape[0] + 2, og_img.shape[1] + 2))
    # leaving first and last row and column. Padded image replaced with orignal image
    padded_image[1:-1, 1:-1] = og_img
    # Creating an array of zeros with padding
    medianNoiseCancellation = np.zeros_like(og_img)
    for x in range(og_img.shape[1]):
        for y in range(og_img.shape[0]):
            medianNoiseCancellation[y, x] = np.median(padded_image[y:y + 3, x:x + 3])
    return medianNoiseCancellation


if __name__ == '__main__':
    # Import image
    image = imageio.imread('image/ckt-board-saltpep.tif')
    image = image.astype('int32')
    # Filter for mean
    # [[1/9   1/9    1/9
    #   1/9   1/9    1/9
    #   1/9   1/9    1/9]]
    meanFilter = [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]
    meanScore = mean_filter(image, meanFilter)
    imageio.imwrite('image/mean_output.jpg', meanScore)
    medianScore = median_filter(image)
    imageio.imwrite('image/median_output.jpg', medianScore)
