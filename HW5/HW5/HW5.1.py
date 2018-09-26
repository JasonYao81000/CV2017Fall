if __name__ == '__main__':
    from PIL import Image
    import numpy as np
    import JasonDIP

    # Define kernel for dilation.
    kernel = np.array([\
        [0, 1, 1, 1, 0], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [0, 1, 1, 1, 0]])
    # Define center of kernel for dilation.
    centerKernel = (2, 2)
    # Load image from file.
    originalImage = Image.open('lena.bmp')
    # Get dilation image.
    dilationImage = JasonDIP.dilation(originalImage, kernel, centerKernel)
    # Save image fo file.
    dilationImage.save('dilation.bmp')