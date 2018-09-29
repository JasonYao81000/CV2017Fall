# CV2017Fall
Computer Vision I 2017 Fall at NTU.

This course has 10 homeworks. The 10 homeworks are as follows:

1. Basic Image Manipulation
2. Basic Image Manipulation
3. Histogram Equalization
4. Mathematical Morphology - Binary Morphology
5. Mathematical Morphology - Gray Scaled Morphology
6. Yokoi Connectivity Number
7. Thinning
8. Noise Removal
9. General Edge Detection
10. Zero Crossing Edge Detection

# Table of Contents
<!--ts-->
   1. [Basic Image Manipulation](https://github.com/JasonYao81000/CV2017Fall/blob/master/README.md#hw1-basic-image-manipulation)
   2. [Basic Image Manipulation](https://github.com/JasonYao81000/CV2017Fall/blob/master/README.md#hw2-basic-image-manipulation)
<!--te-->

# HW1: Basic Image Manipulation
* Part 1 of this homework is writing a program to generate the following images from lena.bmp.
   * Up-side-down lena.bmp.
   * Right-side-left lena.bmp.
   * Diagonally mirrored lena.bmp.
   * Code: [HW1.1](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW1/HW1.1)
   
* Part 2 of this homework is using any kind of software to do the following things:
   * Rotate lena.bmp 45 degrees clockwise.
   * Shrink lena.bmp in half.
   * Binarize lena.bmp at 128 to get a binary image.
   * Code: [HW1.2](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW1/HW1.2)
         
* [Report](https://github.com/JasonYao81000/CV2017Fall/blob/master/HW1/CV1_HW1_%E5%A7%9A%E5%98%89%E6%98%87_R06922002.pdf)

# HW2: Basic Image Manipulation
* Part 1 of this homework is to binarize lena.bmp with threshold 128 (0-127, 128-255).
   * Code: [HW2.1](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW2/HW2.1)
   
* Part 2 of this homework is to draw the histogram of lena.bmp.
   * Code: [HW2.2](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW2/HW2.2)
   
* Part 3 of this homework is to find connected components with following rules:
   * Draw bounding box of regions.
   * Draw cross at centroid of regions.
   * Omit regions that have a pixel count less than 500.
   * Code: [HW2.3](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW2/HW2.3)
   
* [Report](https://github.com/JasonYao81000/CV2017Fall/blob/master/HW2/CV1_HW2_%E5%A7%9A%E5%98%89%E6%98%87_R06922002.pdf)

# HW3: Histogram Equalization
* This homework is to do histogram equalization with following rules:
   * Adjust the brightness of lena.bmp to one-third.
   * Do histogram equalization on dark image.
   * Show the histogram of the final image.
   * Code: [HW3.1](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW3/HW3.1)
   
* [Report](https://github.com/JasonYao81000/CV2017Fall/blob/master/HW3/CV1_HW3_%E5%A7%9A%E5%98%89%E6%98%87_R06922002.pdf)

# HW4: Mathematical Morphology - Binary Morphology
* This homework is to do binary morphology with following rules:
   * Please use the octagonal 3-5-5-5-3 kernel.
   * Please use the “L” shaped kernel to detect the upper-right corner for hit-and-miss transform.
   * Please process the white pixels (operating on white pixels).
   * Five images should be included in your report: Dilation, Erosion, Opening, Closing, and Hit-and-Miss.
   * Code: [HW4.1](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW4/HW4.1)
   
* [Report](https://github.com/JasonYao81000/CV2017Fall/blob/master/HW4/CV1_HW4_%E5%A7%9A%E5%98%89%E6%98%87_R06922002.pdf)

# HW5: Mathematical Morphology - Gray Scaled Morphology
* This homework is to do gray scaled morphology with following rules:
   * Please use the octagonal 3-5-5-5-3 kernel.
   * Please take the local maxima or local minima respectively.
   * Four images should be included in your report: Dilation, Erosion, Opening, and Closing.
   * Code: [HW5](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW5/HW5)
   
* [Report](https://github.com/JasonYao81000/CV2017Fall/blob/master/HW5/CV1_HW5_%E5%A7%9A%E5%98%89%E6%98%87_R06922002.pdf)

# HW6: Yokoi Connectivity Number
* This homework is to do Yokoi connectivity number with following rules:
   * Please binarize leba.bmp with threshold 128.
   * Please down sampling binary.bmp from 512x512 to 64x64, using 8x8 blocks as unit and take the topmost-left pixel as the down sampling data.
   * Print Yokoi connectivity number to text file.
   * Code: [HW6](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW6/HW6)

* [Report](https://github.com/JasonYao81000/CV2017Fall/blob/master/HW6/CV1_HW6_%E5%A7%9A%E5%98%89%E6%98%87_R06922002.pdf)

# HW7: Thinning
* This homework is to do thinning operation with following rules:
   * Please binarize leba.bmp with threshold 128.
   * Do thinning operation on binary image.
   * Code: [HW7](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW7/HW7)
   
* [Report](https://github.com/JasonYao81000/CV2017Fall/blob/master/HW7/CV1_HW7_%E5%A7%9A%E5%98%89%E6%98%87_R06922002.pdf)

# HW8: Noise Removal
* This homework is to do noise removal with following rules:
   * Generate Gaussian noise with amplitude of 10 and 30.
   * Generate salt-and-pepper noise with probability of 0.1 and 0.05.
   * Use the 3x3 and 5x5 box filter on noise images.
   * Use the 3x3 and 5x5 median filter on noise images.
   * Use opening-then-closing and closing-then-opening filter on noise images.
   * Calculate the signal-to-noise-ratio (SNR) of noise images.
   * Code: [HW8](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW8/HW8)
   
* [Report](https://github.com/JasonYao81000/CV2017Fall/blob/master/HW8/CV1_HW8_%E5%A7%9A%E5%98%89%E6%98%87_R06922002.pdf)

# HW9: General Edge Detection
* This homework is to do general edge detection with following rules:
   * Robert’s operator with threshold of 12.
   * Prewitt’s edge detector with threshold of 24.
   * Sobel’s edge detector with threshold of 38.
   * Frei and Chen’s gradient operator with threshold of 30.
   * Kirsch’s compass operator with threshold of 135.
   * Robinson’s compass operator with threshold of 43.
   * Nevatia-Babu 5x5 operator with threshold of 12500.
   * Code: [HW9](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW9/HW9)

* [Report](https://github.com/JasonYao81000/CV2017Fall/blob/master/HW9/CV1_HW9_%E5%A7%9A%E5%98%89%E6%98%87_R06922002.pdf)

# HW10: Zero Crossing Edge Detection
* This homework is to do zero crossing edge detection with following rules:
   * Laplacian mask 1 with threshold of 15.
   * Laplacian mask 2 with threshold of 15.
   * Minimum variance Laplacian with threshold of 20.
   * Laplacian of Gaussian with threshold of 3000.
   * Difference of Gaussian with threshold of 1.
   * Code: [HW10](https://github.com/JasonYao81000/CV2017Fall/tree/master/HW10/HW10)

* [Report](https://github.com/JasonYao81000/CV2017Fall/blob/master/HW10/CV1_HW10_%E5%A7%9A%E5%98%89%E6%98%87_R06922002.pdf)
