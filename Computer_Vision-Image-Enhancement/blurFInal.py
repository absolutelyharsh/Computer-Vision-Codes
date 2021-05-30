import numpy as np
import imageio


def vertical_detection(og_img, laplacianFilter):
    # Creating a padded image of zeros
    padded_image = np.zeros((og_img.shape[0] + 2, og_img.shape[1] + 2))
    # leaving first and last row and column. Padded image replaced with orignal image
    padded_image[1:-1, 1:-1] = og_img
    # Creating an array of zeros with padding
    laplacianSmoothning = np.zeros_like(og_img)
    # Moving the filter over the image
    for x in range(og_img.shape[1]):
        for y in range(og_img.shape[0]):
            laplacianSmoothning[y, x] = (laplacianFilter * padded_image[y:y + 3, x:x + 3]).sum()
    return laplacianSmoothning


if __name__ == '__main__':
    # Import image
    im = imageio.imread('blurry-moon.tif')
    im = im.astype('int32')
    # Filter for Smoothning
    # [[ 1  -2    1
    #   -2   5   -2
    #    1  -2    1]]
    laplacianFilter = [[1, -2, 1], [-2, 5, -2], [1, -2, 1]]
    laplacianScore = vertical_detection(im, laplacianFilter)

    imageio.imwrite('blur_output.jpg', laplacianScore)
