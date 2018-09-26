def getGaussianNoiseImage(originalImage, amplitude):
    """
    :type originalImage: Image (from PIL)
    :type amplitude: float
    :return type: Image (from PIL)
    """
    from PIL import Image
    import random
    # Copy image from origianl image.
    gaussianNoiseImage = originalImage.copy()
    # Scan each column in original image.
    for c in range(originalImage.size[0]):
        # Scan each row in original image.
        for r in range(originalImage.size[1]):
            # Get pixel value with gaussian noise.
            noisePixel = int(originalImage.getpixel((c, r)) + amplitude * random.gauss(0, 1))
            # Limit pixel value at 255.
            if noisePixel > 255:
                noisePixel = 255
            # Put pixel to noise image.
            gaussianNoiseImage.putpixel((c, r), noisePixel)
    return gaussianNoiseImage

def getSaltAndPepperImage(originalImage, probability):
    """
    :type originalImage: Image (from PIL)
    :type probability: float
    :return type: Image (from PIL)
    """
    from PIL import Image
    import random
    # Copy image from origianl image.
    saltAndPepperImage = originalImage.copy()
    # Scan each column in original image.
    for c in range(originalImage.size[0]):
        # Scan each row in original image.
        for r in range(originalImage.size[1]):
            # Get random value.
            randomValue = random.uniform(0, 1)
            if (randomValue <= probability):
                # Put black pixel(pepper) to image.
                saltAndPepperImage.putpixel((c, r), 0)
            elif (randomValue >= 1 - probability):
                # Put white pixel(salt) to image.
                saltAndPepperImage.putpixel((c, r), 255)
            else:
                # Put origianl pixel to image.
                saltAndPepperImage.putpixel((c, r), originalImage.getpixel((c, r)))
    return saltAndPepperImage

def boxFilter(originalImage, boxWidth, boxHeight):
    """
    :type originalImage: Image (from PIL)
    :type boxWidth: integer
    :type boxHeight: integer
    :return type: Image (from PIL)
    """
    # Calculate center of kernel.
    centerKernel = (boxWidth // 2, boxHeight // 2)
    # Copy image from origianl image.
    boxFilterImage = originalImage.copy()
    # Scan each column in original image.
    for c in range(originalImage.size[0]):
        # Scan each row in original image.
        for r in range(originalImage.size[1]):
            # Create empty list.
            boxPixels = []
            # Scan each column in box.
            for x in range(boxWidth):
                # Scan each row in box.
                for y in range(boxHeight):
                    # Calculate destination x, y position.
                    destX = c + (x - centerKernel[0])
                    destY = r + (y - centerKernel[1])
                    # Avoid out of image range.
                    if ((0 <= destX < originalImage.size[0]) and \
                        (0 <= destY < originalImage.size[1])):
                        # Get pixel value in original image at (destX, destY).
                        originalPixel = originalImage.getpixel((destX, destY))
                        # Append pixel to list.
                        boxPixels.append(originalPixel)
            boxFilterImage.putpixel((c, r), int(sum(boxPixels) / len(boxPixels)))
    return boxFilterImage

def medianFilter(originalImage, boxWidth, boxHeight):
    """
    :type originalImage: Image (from PIL)
    :type boxWidth: integer
    :type boxHeight: integer
    :return type: Image (from PIL)
    """
    # Calculate center of kernel.
    centerKernel = (boxWidth // 2, boxHeight // 2)
    # Copy image from origianl image.
    medianFilterImage = originalImage.copy()
    # Scan each column in original image.
    for c in range(originalImage.size[0]):
        # Scan each row in original image.
        for r in range(originalImage.size[1]):
            # Create empty list.
            boxPixels = []
            # Scan each column in box.
            for x in range(boxWidth):
                # Scan each row in box.
                for y in range(boxHeight):
                    # Calculate destination x, y position.
                    destX = c + (x - centerKernel[0])
                    destY = r + (y - centerKernel[1])
                    # Avoid out of image range.
                    if ((0 <= destX < originalImage.size[0]) and \
                        (0 <= destY < originalImage.size[1])):
                        # Get pixel value in original image at (destX, destY).
                        originalPixel = originalImage.getpixel((destX, destY))
                        # Append pixel to list.
                        boxPixels.append(originalPixel)
            # Sort pixels in box.
            boxPixels.sort()
            # Get Median pixel.
            medianPixel = boxPixels[len(boxPixels) // 2]
            # Put median pixel to image.
            medianFilterImage.putpixel((c, r), medianPixel)
    return medianFilterImage

def dilation(originalImage, kernel, centerKernel):
    """
    :type originalImage: Image (from PIL)
    :type kernel: numpy array
    :type centerKernel: tuple
    :return type: Image (from PIL)
    """
    from PIL import Image
    # New image with the same size and 'grayscale' format.
    dilationImage = Image.new('L', originalImage.size)
    # Scan each column in original image.
    for c in range(originalImage.size[0]):
        # Scan each row in original image.
        for r in range(originalImage.size[1]):
            # Record local max. pixel value.
            localMaxPixel = 0
            # Scan each column in kernel.
            for x in range(kernel.shape[0]):
                # Scan each row in kernel.
                for y in range(kernel.shape[1]):
                    # Only check value '1' in kernel.
                    if (kernel[x, y] == 1):
                        # Calculate destination x, y position.
                        destX = c + (x - centerKernel[0])
                        destY = r + (y - centerKernel[1])
                        # Avoid out of image range.
                        if ((0 <= destX < originalImage.size[0]) and \
                            (0 <= destY < originalImage.size[1])):
                            # Get pixel value in original image at (destX, destY).
                            originalPixel = originalImage.getpixel((destX, destY))
                            # Update local max. pixel value.
                            localMaxPixel = max(localMaxPixel, originalPixel)
            # Paste local max. pixel value on original image.
            dilationImage.putpixel((c, r), localMaxPixel)
    # Return dilation image.
    return dilationImage

def erosion(originalImage, kernel, centerKernel):
    """
    :type originalImage: Image (from PIL)
    :type kernel: numpy array
    :type centerKernel: tuple
    :return type: Image (from PIL)
    """
    from PIL import Image
    # New image with the same size and 'grayscale' format.
    erosionImage = Image.new('L', originalImage.size)
    # Scan each column in original image.
    for c in range(originalImage.size[0]):
        # Scan each row in original image.
        for r in range(originalImage.size[1]):
            # Record local min. pixel value.
            localMinPixel = 255
            # Scan each column in kernel.
            for x in range(kernel.shape[0]):
                # Scan each row in kernel.
                for y in range(kernel.shape[1]):
                    # Only check value '1' in kernel.
                    if (kernel[x, y] == 1):
                        # Calculate destination x, y position.
                        destX = c + (x - centerKernel[0])
                        destY = r + (y - centerKernel[1])
                        # Avoid out of image range.
                        if ((0 <= destX < originalImage.size[0]) and \
                            (0 <= destY < originalImage.size[1])):
                            # Get pixel value in original image at (destX, destY).
                            originalPixel = originalImage.getpixel((destX, destY))
                            # Update local min. pixel value.
                            localMinPixel = min(localMinPixel, originalPixel)
            # Paste local min. pixel value on original image.
            erosionImage.putpixel((c, r), localMinPixel)
    # Return erosion image.
    return erosionImage

def opening(originalImage, kernel, centerKernel):
    """
    :type originalImage: Image (from PIL)
    :type kernel: numpy array
    :type centerKernel: tuple
    :return type: Image (from PIL)
    """
    return dilation(erosion(originalImage, kernel, centerKernel), kernel, centerKernel)

def closing(originalImage, kernel, centerKernel):
    """
    :type originalImage: Image (from PIL)
    :type kernel: numpy array
    :type centerKernel: tuple
    :return type: Image (from PIL)
    """
    return erosion(dilation(originalImage, kernel, centerKernel), kernel, centerKernel)

def openingThenClosing(originalImage, kernel, centerKernel):
    """
    :type originalImage: Image (from PIL)
    :type kernel: numpy array
    :type centerKernel: tuple
    :return type: Image (from PIL)
    """
    return closing(opening(originalImage, kernel, centerKernel), kernel, centerKernel)

def closingThenOpening(originalImage, kernel, centerKernel):
    """
    :type originalImage: Image (from PIL)
    :type kernel: numpy array
    :type centerKernel: tuple
    :return type: Image (from PIL)
    """
    return opening(closing(originalImage, kernel, centerKernel), kernel, centerKernel)

def getSNR(signalImage, noiseImage):
    """
    :type signalImage: Image (from PIL)
    :type noiseImage: Image (from PIL)
    :return type: float
    """
    import math
    # Clear mu and power of signal and noise.
    muSignal = 0
    powerSignal = 0
    muNoise = 0
    powerNoise = 0

    # Scan each column in signal image.
    for c in range(signalImage.size[0]):
        # Scan each row in signal image.
        for r in range(signalImage.size[1]):
            muSignal = muSignal + signalImage.getpixel((c, r))
    # Average mu of signal.
    muSignal = muSignal / (signalImage.size[0] * signalImage.size[1])

    # Scan each column in noise image.
    for c in range(noiseImage.size[0]):
        # Scan each row in noise image.
        for r in range(noiseImage.size[1]):
            muNoise = muNoise + (noiseImage.getpixel((c, r)) - signalImage.getpixel((c, r)))
    # Average mu of noise.
    muNoise = muNoise / (noiseImage.size[0] * noiseImage.size[1])

    # Scan each column in signal image.
    for c in range(signalImage.size[0]):
        # Scan each row in signal image.
        for r in range(signalImage.size[1]):
            powerSignal = powerSignal + math.pow(signalImage.getpixel((c, r)) - muSignal, 2)
    # Average power of signal.
    powerSignal = powerSignal / (signalImage.size[0] * signalImage.size[1])

    # Scan each column in noise image.
    for c in range(noiseImage.size[0]):
        # Scan each row in noise image.
        for r in range(noiseImage.size[1]):
            powerNoise = powerNoise +  math.pow((noiseImage.getpixel((c, r)) - signalImage.getpixel((c, r))) - muNoise, 2)
    # Average mu of noise.
    powerNoise = powerNoise / (noiseImage.size[0] * noiseImage.size[1])

    return 20 * math.log(math.sqrt(powerSignal) / math.sqrt(powerNoise), 10)

if __name__ == '__main__':
    from PIL import Image
    import numpy as np
    # Fix random seed for reproducibility.
    seed = 777
    np.random.seed(seed)

    # Define kernel for opening and closing.
    kernel = np.array([\
        [0, 1, 1, 1, 0], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [0, 1, 1, 1, 0]])
    # Define center of kernel for opening and closing.
    centerKernel = (2, 2)

    # Load image from file.
    originalImage = Image.open('lena.bmp')
    
    # Get gaussian noise image with amplitude of 10.
    gaussianNoise_10_Image = getGaussianNoiseImage(originalImage, 10)
    # Get gaussian noise image with amplitude of 30.
    gaussianNoise_30_Image = getGaussianNoiseImage(originalImage, 30)

    # Get salt-and-pepper image with probability of 0.10.
    saltAndPepper_0_10_Image = getSaltAndPepperImage(originalImage, 0.10)
    # Get salt-and-pepper image with probability of 0.05.
    saltAndPepper_0_05_Image = getSaltAndPepperImage(originalImage, 0.05)

    # Use 3x3 box filter on gaussian noise image with amplitude of 10.
    gaussianNoise_10_box_3x3_Image = boxFilter(gaussianNoise_10_Image, 3, 3)
    # Use 3x3 box filter on gaussian noise image with amplitude of 30.
    gaussianNoise_30_box_3x3_Image = boxFilter(gaussianNoise_30_Image, 3, 3)
    # Use 3x3 box filter on salt-and-pepper image with probability of 0.10.
    saltAndPepper_0_10_box_3x3_Image = boxFilter(saltAndPepper_0_10_Image, 3, 3)
    # Use 3x3 box filter on salt-and-pepper image with probability of 0.05.
    saltAndPepper_0_05_box_3x3_Image = boxFilter(saltAndPepper_0_05_Image, 3, 3)

    # Use 5x5 box filter on gaussian noise image with amplitude of 10.
    gaussianNoise_10_box_5x5_Image = boxFilter(gaussianNoise_10_Image, 5, 5)
    # Use 5x5 box filter on gaussian noise image with amplitude of 30.
    gaussianNoise_30_box_5x5_Image = boxFilter(gaussianNoise_30_Image, 5, 5)
    # Use 5x5 box filter on salt-and-pepper image with probability of 0.10.
    saltAndPepper_0_10_box_5x5_Image = boxFilter(saltAndPepper_0_10_Image, 5, 5)
    # Use 5x5 box filter on salt-and-pepper image with probability of 0.05.
    saltAndPepper_0_05_box_5x5_Image = boxFilter(saltAndPepper_0_05_Image, 5, 5)

    # Use 3x3 median filter on gaussian noise image with amplitude of 10.
    gaussianNoise_10_median_3x3_Image = medianFilter(gaussianNoise_10_Image, 3, 3)
    # Use 3x3 median filter on gaussian noise image with amplitude of 30.
    gaussianNoise_30_median_3x3_Image = medianFilter(gaussianNoise_30_Image, 3, 3)
    # Use 3x3 median filter on salt-and-pepper image with probability of 0.10.
    saltAndPepper_0_10_median_3x3_Image = medianFilter(saltAndPepper_0_10_Image, 3, 3)
    # Use 3x3 median filter on salt-and-pepper image with probability of 0.05.
    saltAndPepper_0_05_median_3x3_Image = medianFilter(saltAndPepper_0_05_Image, 3, 3)

    # Use 5x5 median filter on gaussian noise image with amplitude of 10.
    gaussianNoise_10_median_5x5_Image = medianFilter(gaussianNoise_10_Image, 5, 5)
    # Use 5x5 median filter on gaussian noise image with amplitude of 30.
    gaussianNoise_30_median_5x5_Image = medianFilter(gaussianNoise_30_Image, 5, 5)
    # Use 5x5 median filter on salt-and-pepper image with probability of 0.10.
    saltAndPepper_0_10_median_5x5_Image = medianFilter(saltAndPepper_0_10_Image, 5, 5)
    # Use 5x5 median filter on salt-and-pepper image with probability of 0.05.
    saltAndPepper_0_05_median_5x5_Image = medianFilter(saltAndPepper_0_05_Image, 5, 5)

    # Opening then closing on gaussian noise image with amplitude of 10.
    gaussianNoise_10_openingThenClosing_Image = openingThenClosing(gaussianNoise_10_Image, kernel, centerKernel)
    # Opening then closing on gaussian noise image with amplitude of 30.
    gaussianNoise_30_openingThenClosing_Image = openingThenClosing(gaussianNoise_30_Image, kernel, centerKernel)
    # Opening then closing on salt-and-pepper image with probability of 0.10.
    saltAndPepper_0_10_openingThenClosing_Image = openingThenClosing(saltAndPepper_0_10_Image, kernel, centerKernel)
    # Opening then closing on salt-and-pepper image with probability of 0.05.
    saltAndPepper_0_05_openingThenClosing_Image = openingThenClosing(saltAndPepper_0_05_Image, kernel, centerKernel)

    # Closing then opening on gaussian noise image with amplitude of 10.
    gaussianNoise_10_closingThenOpening_Image = closingThenOpening(gaussianNoise_10_Image, kernel, centerKernel)
    # Closing then opening on gaussian noise image with amplitude of 30.
    gaussianNoise_30_closingThenOpening_Image = closingThenOpening(gaussianNoise_30_Image, kernel, centerKernel)
    # Closing then opening on salt-and-pepper image with probability of 0.10.
    saltAndPepper_0_10_closingThenOpening_Image = closingThenOpening(saltAndPepper_0_10_Image, kernel, centerKernel)
    # Closing then opening on salt-and-pepper image with probability of 0.05.
    saltAndPepper_0_05_closingThenOpening_Image = closingThenOpening(saltAndPepper_0_05_Image, kernel, centerKernel)

    # Save gaussian noise image with amplitude of 10 fo file.
    gaussianNoise_10_Image.save('gaussianNoise_10.bmp')
    # Save gaussian noise image with amplitude of 30 fo file.
    gaussianNoise_30_Image.save('gaussianNoise_30.bmp')
    # Save salt-and-pepper image with probability of 0.10 fo file.
    saltAndPepper_0_10_Image.save('saltAndPepper_0_10.bmp')
    # Save salt-and-pepper image with probability of 0.05 fo file.
    saltAndPepper_0_05_Image.save('saltAndPepper_0_05.bmp')

    # Save 3x3 box filtered gaussian noise image with amplitude of 10 fo file.
    gaussianNoise_10_box_3x3_Image.save('gaussianNoise_10_box_3x3.bmp')
    # Save 3x3 box filtered gaussian noise image with amplitude of 30 fo file.
    gaussianNoise_30_box_3x3_Image.save('gaussianNoise_30_box_3x3.bmp')
    # Save 3x3 box filtered salt-and-pepper image with probability of 0.10 fo file.
    saltAndPepper_0_10_box_3x3_Image.save('saltAndPepper_0_10_box_3x3.bmp')
    # Save 3x3 box filtered salt-and-pepper image with probability of 0.05 fo file.
    saltAndPepper_0_05_box_3x3_Image.save('saltAndPepper_0_05_box_3x3.bmp')

    # Save 5x5 box filtered gaussian noise image with amplitude of 10 fo file.
    gaussianNoise_10_box_5x5_Image.save('gaussianNoise_10_box_5x5.bmp')
    # Save 5x5 box filtered gaussian noise image with amplitude of 30 fo file.
    gaussianNoise_30_box_5x5_Image.save('gaussianNoise_30_box_5x5.bmp')
    # Save 5x5 box filtered salt-and-pepper image with probability of 0.10 fo file.
    saltAndPepper_0_10_box_5x5_Image.save('saltAndPepper_0_10_box_5x5.bmp')
    # Save 5x5 box filtered salt-and-pepper image with probability of 0.05 fo file.
    saltAndPepper_0_05_box_5x5_Image.save('saltAndPepper_0_05_box_5x5.bmp')

    # Save 3x3 median filtered gaussian noise image with amplitude of 10 fo file.
    gaussianNoise_10_median_3x3_Image.save('gaussianNoise_10_median_3x3.bmp')
    # Save 3x3 median filtered gaussian noise image with amplitude of 30 fo file.
    gaussianNoise_30_median_3x3_Image.save('gaussianNoise_30_median_3x3.bmp')
    # Save 3x3 median filtered salt-and-pepper image with probability of 0.10 fo file.
    saltAndPepper_0_10_median_3x3_Image.save('saltAndPepper_0_10_median_3x3.bmp')
    # Save 3x3 median filtered salt-and-pepper image with probability of 0.05 fo file.
    saltAndPepper_0_05_median_3x3_Image.save('saltAndPepper_0_05_median_3x3.bmp')

    # Save 5x5 median filtered gaussian noise image with amplitude of 10 fo file.
    gaussianNoise_10_median_5x5_Image.save('gaussianNoise_10_median_5x5.bmp')
    # Save 5x5 median filtered gaussian noise image with amplitude of 30 fo file.
    gaussianNoise_30_median_5x5_Image.save('gaussianNoise_30_median_5x5.bmp')
    # Save 5x5 median filtered salt-and-pepper image with probability of 0.10 fo file.
    saltAndPepper_0_10_median_5x5_Image.save('saltAndPepper_0_10_median_5x5.bmp')
    # Save 5x5 median filtered salt-and-pepper image with probability of 0.05 fo file.
    saltAndPepper_0_05_median_5x5_Image.save('saltAndPepper_0_05_median_5x5.bmp')

    # Save closingThenOpening gaussian noise image with amplitude of 10 fo file.
    gaussianNoise_10_openingThenClosing_Image.save('gaussianNoise_10_openingThenClosing.bmp')
    # Save closingThenOpening gaussian noise image with amplitude of 30 fo file.
    gaussianNoise_30_openingThenClosing_Image.save('gaussianNoise_30_openingThenClosing.bmp')
    # Save closingThenOpening salt-and-pepper image with probability of 0.10 fo file.
    saltAndPepper_0_10_openingThenClosing_Image.save('saltAndPepper_0_10_openingThenClosing.bmp')
    # Save closingThenOpening salt-and-pepper image with probability of 0.05 fo file.
    saltAndPepper_0_05_openingThenClosing_Image.save('saltAndPepper_0_05_openingThenClosing.bmp')

    # Save closingThenOpening gaussian noise image with amplitude of 10 fo file.
    gaussianNoise_10_closingThenOpening_Image.save('gaussianNoise_10_closingThenOpening.bmp')
    # Save closingThenOpening gaussian noise image with amplitude of 30 fo file.
    gaussianNoise_30_closingThenOpening_Image.save('gaussianNoise_30_closingThenOpening.bmp')
    # Save closingThenOpening salt-and-pepper image with probability of 0.10 fo file.
    saltAndPepper_0_10_closingThenOpening_Image.save('saltAndPepper_0_10_closingThenOpening.bmp')
    # Save closingThenOpening salt-and-pepper image with probability of 0.05 fo file.
    saltAndPepper_0_05_closingThenOpening_Image.save('saltAndPepper_0_05_closingThenOpening.bmp')

    # Calculate SNR for all noise image.
    gaussianNoise_10_SNR = getSNR(originalImage, gaussianNoise_10_Image)
    gaussianNoise_30_SNR = getSNR(originalImage, gaussianNoise_30_Image)
    saltAndPepper_0_10_SNR = getSNR(originalImage, saltAndPepper_0_10_Image)
    saltAndPepper_0_05_SNR = getSNR(originalImage, saltAndPepper_0_05_Image)

    gaussianNoise_10_box_3x3_SNR = getSNR(originalImage, gaussianNoise_10_box_3x3_Image)
    gaussianNoise_30_box_3x3_SNR = getSNR(originalImage, gaussianNoise_30_box_3x3_Image)
    saltAndPepper_0_10_box_3x3_SNR = getSNR(originalImage, saltAndPepper_0_10_box_3x3_Image)
    saltAndPepper_0_05_box_3x3_SNR = getSNR(originalImage, saltAndPepper_0_05_box_3x3_Image)
    gaussianNoise_10_box_5x5_SNR = getSNR(originalImage, gaussianNoise_10_box_5x5_Image)
    gaussianNoise_30_box_5x5_SNR = getSNR(originalImage, gaussianNoise_30_box_5x5_Image)
    saltAndPepper_0_10_box_5x5_SNR = getSNR(originalImage, saltAndPepper_0_10_box_5x5_Image)
    saltAndPepper_0_05_box_5x5_SNR = getSNR(originalImage, saltAndPepper_0_05_box_5x5_Image)

    gaussianNoise_10_median_3x3_SNR = getSNR(originalImage, gaussianNoise_10_median_3x3_Image)
    gaussianNoise_30_median_3x3_SNR = getSNR(originalImage, gaussianNoise_30_median_3x3_Image)
    saltAndPepper_0_10_median_3x3_SNR = getSNR(originalImage, saltAndPepper_0_10_median_3x3_Image)
    saltAndPepper_0_05_median_3x3_SNR = getSNR(originalImage, saltAndPepper_0_05_median_3x3_Image)
    gaussianNoise_10_median_5x5_SNR = getSNR(originalImage, gaussianNoise_10_median_5x5_Image)
    gaussianNoise_30_median_5x5_SNR = getSNR(originalImage, gaussianNoise_30_median_5x5_Image)
    saltAndPepper_0_10_median_5x5_SNR = getSNR(originalImage, saltAndPepper_0_10_median_5x5_Image)
    saltAndPepper_0_05_median_5x5_SNR = getSNR(originalImage, saltAndPepper_0_05_median_5x5_Image)

    gaussianNoise_10_openingThenClosing_SNR = getSNR(originalImage, gaussianNoise_10_openingThenClosing_Image)
    gaussianNoise_30_openingThenClosing_SNR = getSNR(originalImage, gaussianNoise_30_openingThenClosing_Image)
    saltAndPepper_0_10_openingThenClosing_SNR = getSNR(originalImage, saltAndPepper_0_10_openingThenClosing_Image)
    saltAndPepper_0_05_openingThenClosing_SNR = getSNR(originalImage, saltAndPepper_0_05_openingThenClosing_Image)

    gaussianNoise_10_closingThenOpening_SNR = getSNR(originalImage, gaussianNoise_10_closingThenOpening_Image)
    gaussianNoise_30_closingThenOpening_SNR = getSNR(originalImage, gaussianNoise_30_closingThenOpening_Image)
    saltAndPepper_0_10_closingThenOpening_SNR = getSNR(originalImage, saltAndPepper_0_10_closingThenOpening_Image)
    saltAndPepper_0_05_closingThenOpening_SNR = getSNR(originalImage, saltAndPepper_0_05_closingThenOpening_Image)

    # Write SNR to text file.
    file = open("SNR.txt", "w")
    file.write("gaussianNoise_10_SNR: " + str(gaussianNoise_10_SNR) + '\n')
    file.write("gaussianNoise_30_SNR: " + str(gaussianNoise_30_SNR) + '\n')
    file.write("saltAndPepper_0_10_SNR: " + str(saltAndPepper_0_10_SNR) + '\n')
    file.write("saltAndPepper_0_05_SNR: " + str(saltAndPepper_0_05_SNR) + '\n')

    file.write("gaussianNoise_10_box_3x3_SNR: " + str(gaussianNoise_10_box_3x3_SNR) + '\n')
    file.write("gaussianNoise_30_box_3x3_SNR: " + str(gaussianNoise_30_box_3x3_SNR) + '\n')
    file.write("saltAndPepper_0_10_box_3x3_SNR: " + str(saltAndPepper_0_10_box_3x3_SNR) + '\n')
    file.write("saltAndPepper_0_05_box_3x3_SNR: " + str(saltAndPepper_0_05_box_3x3_SNR) + '\n')
    file.write("gaussianNoise_10_box_5x5_SNR: " + str(gaussianNoise_10_box_5x5_SNR) + '\n')
    file.write("gaussianNoise_30_box_5x5_SNR: " + str(gaussianNoise_30_box_5x5_SNR) + '\n')
    file.write("saltAndPepper_0_10_box_5x5_SNR: " + str(saltAndPepper_0_10_box_5x5_SNR) + '\n')
    file.write("saltAndPepper_0_05_box_5x5_SNR: " + str(saltAndPepper_0_05_box_5x5_SNR) + '\n')

    file.write("gaussianNoise_10_median_3x3_SNR: " + str(gaussianNoise_10_median_3x3_SNR) + '\n')
    file.write("gaussianNoise_30_median_3x3_SNR: " + str(gaussianNoise_30_median_3x3_SNR) + '\n')
    file.write("saltAndPepper_0_10_median_3x3_SNR: " + str(saltAndPepper_0_10_median_3x3_SNR) + '\n')
    file.write("saltAndPepper_0_05_median_3x3_SNR: " + str(saltAndPepper_0_05_median_3x3_SNR) + '\n')
    file.write("gaussianNoise_10_median_5x5_SNR: " + str(gaussianNoise_10_median_5x5_SNR) + '\n')
    file.write("gaussianNoise_30_median_5x5_SNR: " + str(gaussianNoise_30_median_5x5_SNR) + '\n')
    file.write("saltAndPepper_0_10_median_5x5_SNR: " + str(saltAndPepper_0_10_median_5x5_SNR) + '\n')
    file.write("saltAndPepper_0_05_median_5x5_SNR: " + str(saltAndPepper_0_05_median_5x5_SNR) + '\n')
    
    file.write("gaussianNoise_10_openingThenClosing_SNR: " + str(gaussianNoise_10_openingThenClosing_SNR) + '\n')
    file.write("gaussianNoise_30_openingThenClosing_SNR: " + str(gaussianNoise_30_openingThenClosing_SNR) + '\n')
    file.write("saltAndPepper_0_10_openingThenClosing_SNR: " + str(saltAndPepper_0_10_openingThenClosing_SNR) + '\n')
    file.write("saltAndPepper_0_05_openingThenClosing_SNR: " + str(saltAndPepper_0_05_openingThenClosing_SNR) + '\n')

    file.write("gaussianNoise_10_closingThenOpening_SNR: " + str(gaussianNoise_10_closingThenOpening_SNR) + '\n')
    file.write("gaussianNoise_30_closingThenOpening_SNR: " + str(gaussianNoise_30_closingThenOpening_SNR) + '\n')
    file.write("saltAndPepper_0_10_closingThenOpening_SNR: " + str(saltAndPepper_0_10_closingThenOpening_SNR) + '\n')
    file.write("saltAndPepper_0_05_closingThenOpening_SNR: " + str(saltAndPepper_0_05_closingThenOpening_SNR) + '\n')