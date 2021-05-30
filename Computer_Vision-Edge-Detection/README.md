# Edge Detection

## What are Edges ? 

- Edges are significant local changes in an image and are important features for analyzing images.
- They typically occur on the boundary between two different regions in an image. 
- It is considered as the first step in recovering information from images. 
- Any significant local change in image intensity usually associated with a discontinuity in either image intensity or first derivative of the image intensity is considered to be an edge. 
- Discontinuities in images can be of two types:
    - **Step Discontinuities:** Image intensity abruptly changes from one value on onside of discontinuity to a different value on the    
        opposite side.
    - **Line Discontinuities:** Image intensity abruptly changes value but then returns to the starting value within some short distance. 
- Step and line edges are rare in real images, because of low-frequency components or smoothning introduced by most sensing devices, sharp discontinuities rarely exist in real signals. 
- Step changes become ramp edges and line edges become roof edges where intensity changes are not instantaneous but occur over a finite distance. 
- Illustration for these edges are as below


<p align="center">
  <img src="https://github.com/absolutelyharsh/Computer_Vision-Edge-Detection/blob/master/Image/fig.%201.png" alt="One-dimensional edge profiles"/>
</p>


## Different Types Of Edges:

1. Horizontal Edges
2. Vertical Edges
3. Diagonal Edges


## Steps In Edge Detection

Algorithms for edge detection has three steps:

**Filtering:** Since gradient computation based on intensity values of only two points are susceptible to noise and other variances in discrete computations, it is used to improve the performance of an edge detector with respect to noise. Trade-Off between edge strength and noise reduction exists. More filtering to reduce noise results in a loss of edge strength. 

**Enhancement:** In order to facilitate the detection of edges, it is essential to determine changes in intensity in neighborhood of a point. Enhancement emphasizes pixels where there is a significant change in local intensity values and is usually performed by computing the gradient magnitude. 

**Detection:** Only points with strong edge content are required. Many points have a nonzero vavlue for the gradient, and not all of these points are edges for particular applications. Some method is required to determine which points are edge points. Thresholding provides the criterion used for detection. 

It is important to note that detection merely indicates that an edge is present near a pixel in an image,but does not necessarily provide an accurate estimate of edge location or orientation. The errors in edge detection are errors of misclassification:false edges and missing edges.

## Sobbel Edge Detector

The sobel operator is used to detect two kinds of edges in an image
  - Vertical Detection
  - Horizontal Detection
  
 - The operator uses two 3x3 kernels which are convolved with the original image to calculate approximations of the derivates one for 
   horizontal changes and the other for vertical changes. 
- If we define **A** as source image and **Gx** and **Gy** as two images which at every point contain the vertical and horizontal 
  derivative approximations respectively, the computations can be done as follows
  
  
<p align="center">
  <img src="https://github.com/absolutelyharsh/Computer_Vision-Edge-Detection/blob/master/Image/fig.%202.png"/>
</p>

- Here * denotes the convolution process. 
- At each point in the image the resulting gradient approximations can be combined to give the gradient magnitude using:

<p align="center">
  <img src=https://github.com/absolutelyharsh/Computer_Vision-Edge-Detection/blob/master/Image/fig.3.png/>
</p>


## Output of Sobel Operator 

<p align="center">
  <img src=https://github.com/absolutelyharsh/Computer_Vision-Edge-Detection/blob/master/Image/fig.4.png>
</p>
  
  
