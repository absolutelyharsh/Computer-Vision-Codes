# Image Enhancement

## What is Image Enhancement ?

- Image enhancement is the procedure of improving the quality and information content of original data before processing. 
- They can be divided into two parts:
  1. Spatial Domain Methods (Operating on image pixels directly)
  2. Frequency Domain Methods (Operating on fourier transform of an image)
  
- The main aim in image sharpening is to highlight fine detail in the image, or to enhance detail that has been blurred (perhaps due to noise or other effects, such as motion).
- They mainly enhance the appearance of images, primarily by sharpening edges, corners and other fine details. 
- A simple spatial filter that acheives image sharpening is given by 

<p align="center">
  <img width="200" src="https://github.com/absolutelyharsh/Computer_Vision-Image-Enhancement/blob/main/Image/spatial_filter.png">
</p>

## Different Type Of Filters ?

### 1. High Pass Filter

- The High Pass filter is a linear convolution filter that selectively enhances local features(high spatial-frequency components) of an iage  while  maintaining the larger-scale features.
- This  filter  subtracts  anaveraged  (smoothed)version  of  the  image surroundings fromeach image cell, accentuating  local  features.
- The default filter kernel has filter weight values of –0.5 for allcells except the center cell, which is assigned a high positiveweight whose value depends on the filter window size (5.5 fora 3 by 3 filter window).

### 2. High Boost Filter
- The High Boost filter is a milder form of the High Pass filter. 
- The default weighting coefficient for non-central cells is –1.00,while the center cell is asigned a uch higher positive value (20.0 for a 3 by 3 ker-nel) than for a High Pass filter of the same size.  
- Because of the greater difference in weights between the center and non-cen-ter cell positions in the kernel, the High Boost filter emphasizes the raw image values much more than the local average being subtracted.

## Filter used in code ?

The following filter was used in the code:

<p align="center">
  <https://github.com/absolutelyharsh/Computer_Vision-Image-Enhancement/blob/main/Image/Filter%20Used%20In%20code.png>
</p>

## Outputs of Sharpening Filter
Blurred Image             |  Enhanced Image
:-------------------------:|:-------------------------:
![](https://github.com/absolutelyharsh/Computer_Vision-Image-Enhancement/blob/main/Image/blurry-moon.png)  |  ![](https://github.com/absolutelyharsh/Computer_Vision-Image-Enhancement/blob/main/Image/blur_output.jpg)

