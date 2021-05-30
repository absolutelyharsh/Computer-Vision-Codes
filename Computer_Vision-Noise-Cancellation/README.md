# Noise Cancellation

## What is Noise in Image?

- Image noise is random variation of brightness, color information in images, and is ususally an aspect of electronic noise.
- This noise is undesirable byproduct of image capture that obscures the desired information. 

## Different Types of Noise:
1. Gaussian Noise
2. Salt and Pepper Noise
3. Shot Noise
4. Quantization Noise
5. Film Grain
6. Periodic Noise

- Noise cancellation can be done using various filters, the basic and most common filters are mean, media and laplacian filter. This repo contains Mean and Median filter.

## Working Of Mean Filters

- Mean filter is simple, intutive and easy to implement for smoothning of images, i.e. reduces the amount of intensity variation between one pixel and the next. 
- It replaces each pixel value in an image with mean value of its neighbors including itself.
- This eliminates every pixel values which are unrepresentative of their surroundings. 
- Mean filter is similar to convolution and  is based around a kernel representing shape and size of neighborhood to be sampled when calculating the mean. 
- Usuall a 3x3 kernel is used, although a larger kernel(5x5) can be used for more severe smoothning. 

<p align="center">
  <img src="https://github.com/absolutelyharsh/Computer_Vision-Noise-Cancellation/blob/main/Image/mean.png"/>
</p>
<p align="center">Mean Kernel</p>

## Working Of Median Filters

- Median filter usually used to reduce noise in an image, similar to the mean filter.
- It still does a better job than the mean filter of preserving useful detail in the image. 
- Like the mean, the median considers each pixel in the image and looks at nearby neighbors to decide whether or not it is representative of its surroundings. 
- Instead of simply replacing the pixel value with the mean of neighboring pixel values, it replaces it with the median of those values.
- The median is calculated by first sorting all the pixel values from the surrounding neighborhood into numerical order and then replacing the pixel being considered with the middle pixel value. (If the neighborhood under consideration contains an even number of pixels, the average of the two middle pixel values is used.)

<p align="center">
  <img src="https://github.com/absolutelyharsh/Computer_Vision-Noise-Cancellation/blob/main/Image/median.png"/>
</p>
<p align="center">Median Process</p>

- Calculating the median value of a pixel neighborhood. As can be seen, the central pixel value of 150 is rather unrepresentative of the surrounding pixels and is replaced with the median value: 124. A 3×3 square neighborhood is used here --- larger neighborhoods will produce more severe smoothing.

## Output of Sobel Operator 

<p align="center">
  <img src="https://github.com/absolutelyharsh/Computer_Vision-Noise-Cancellation/blob/main/Image/output.png"/>
</p>
