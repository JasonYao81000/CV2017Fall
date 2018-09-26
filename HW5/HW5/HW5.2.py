if __name__ == '__main__':
    from PIL import Image
    import numpy as np
    import JasonDIP

    # Define kernel for erosion.
    kernel = np.array([\
        [0, 1, 1, 1, 0], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [0, 1, 1, 1, 0]])
    # Define center of kernel for erosion.
    centerKernel = (2, 2)
    # Load image from file.
    originalImage = Image.open('lena.bmp')
    # Get erosion image.
    erosionImage = JasonDIP.erosion(originalImage, kernel, centerKernel)
    # Save image fo file.
    erosionImage.save('erosion.bmp')