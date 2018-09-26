from PIL import Image

# Load image from file.
originalImage = Image.open('lena.bmp')

# Get width and height of image.
width, height = originalImage.size
# print ('width = %d, height = %d' %(width, height))

# New image with the same size and 'grayscale' format.
upSideDownImage = Image.new('L', originalImage.size)
rightSideLeftImage = Image.new('L', originalImage.size)
diagonallyMirroredImage = Image.new('L', originalImage.size)

# Process image pixel by pixel.
for c in range(width):
    for r in range(height):
        # Get pixel for up-side-down image.
        value = originalImage.getpixel((c, height - 1 - r))
        # Put pixel to up-side-down image.
        upSideDownImage.putpixel((c, r), value)
        # Get pixel for right-side-left image.
        value = originalImage.getpixel((width - 1 - c, r))
        # Put pixel to right-side-left image.
        rightSideLeftImage.putpixel((c, r), value)
        # Get pixel for diagonally mirrored image.
        value = originalImage.getpixel((r, c))
        # Put pixel to right-side-left image.
        diagonallyMirroredImage.putpixel((c, r), value)

# Save image.
upSideDownImage.save('up-side-down.bmp')
rightSideLeftImage.save('right-side-left.bmp')
diagonallyMirroredImage.save('diagonally-mirrored.bmp')