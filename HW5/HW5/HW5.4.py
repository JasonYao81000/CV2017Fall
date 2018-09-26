if __name__ == '__main__':
    from PIL import Image
    import numpy as np
    import JasonDIP

    # Define kernel for closing.
    kernel = np.array([\
        [0, 1, 1, 1, 0], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [0, 1, 1, 1, 0]])
    # Define center of kernel for closing.
    centerKernel = (2, 2)
    # Load image from file.
    originalImage = Image.open('lena.bmp')
    # Get closing image.
    closingImage = JasonDIP.closing(originalImage, kernel, centerKernel)
    # Save image fo file.
    closingImage.save('closing.bmp')