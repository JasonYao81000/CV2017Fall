if __name__ == '__main__':
    from PIL import Image
    import numpy as np
    import JasonDIP

    # Define kernels for hit-and-miss.
    kernel_J = np.array([
        [1, 1], 
        [0, 1]])
    centerKernel_J = (1, 0)
    kernel_K = np.array([
        [1, 1], 
        [0, 1]])
    centerKernel_K = (0, 1)
    # Load image from file.
    originalImage = Image.open('binary.bmp')
    # Get hit-and-miss image.
    hitAndMissImage = JasonDIP.hitmiss(originalImage, 
        kernel_J, centerKernel_J, 
        kernel_K, centerKernel_K)
    # Save image fo file.
    hitAndMissImage.save('hit-and-miss.bmp')

