from PIL import Image

# Define threshold of binary image.
threshold = 128

# Load image from file.
originalImage = Image.open('lena.bmp')

# Get width and height of image.
width, height = originalImage.size
# print ('width = %d, height = %d' %(width, height))

# New image with the same size and 'binary' format.
binaryImage = Image.new('1', originalImage.size)

# Process image pixel by pixel.
for c in range(width):
    for r in range(height):
        # Get pixel from original image.
        value = originalImage.getpixel((c, r))
        if (value >= threshold):
            value = 1
        else:
            value = 0
        # Put pixel to binary image.
        binaryImage.putpixel((c, r), value)

# Save image.
binaryImage.save('binary.bmp')