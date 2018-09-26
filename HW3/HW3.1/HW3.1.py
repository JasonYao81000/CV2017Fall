from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv

# Load image from file.
originalImage = Image.open('lena.bmp')

# Get width and height of image.
width, height = originalImage.size
# print ('width = %d, height = %d' %(width, height))

# New image with the same size and 'grayscale' format.
darkImage = Image.new('L', originalImage.size)

# Process image pixel by pixel.
for c in range(width):
    for r in range(height):
        # Get pixel from original image.
        pixelValue = originalImage.getpixel((c, r))
        # Assign 1/3 pixel value to dark image.
        darkImage.putpixel((c, r), pixelValue // 3)

# Save image to file.
darkImage.save('dark.bmp')

# Create histogram array with zeros.
darkHistogram = np.zeros(256)

# Process image pixel by pixel.
for c in range(width):
    for r in range(height):
        # Get pixel from dark image.
        pixelValue = darkImage.getpixel((c, r))
        # Record count in histogram array.
        darkHistogram[pixelValue] += 1

# Save histogram to csv file.
csvFile = open('dark histogram.csv', 'w')
writer = csv.writer(csvFile)
writer.writerow(darkHistogram)

# Clear plot.
plt.gcf().clear()
# Plot histogram.
plt.bar(range(len(darkHistogram)), darkHistogram)
# Save histogram to image file.
plt.savefig('dark histogram.png')
# # Show plot.
# plt.show()

# Histogram Equalization
# Look up table for transformation.
transformationTable = np.zeros(256)

# Deal with each value (0 ~ 255).
for i in range(len(transformationTable)):
    transformationTable[i] = 255 * np.sum(darkHistogram[0:i + 1]) / width / height

# New image with the same size and 'grayscale' format.
histEquImage = Image.new('L', originalImage.size)

# Process image pixel by pixel.
for c in range(width):
    for r in range(height):
        # Get pixel from dark image.
        pixelValue = darkImage.getpixel((c, r))
        # Put pixel to histogram equalization image.
        histEquImage.putpixel((c, r), int(transformationTable[pixelValue]))
    
# Save image to file.
histEquImage.save('histogram equalization.bmp')

# Create histogram array with zeros.
histEquHistogram = np.zeros(256)

# Process image pixel by pixel.
for c in range(width):
    for r in range(height):
        # Get pixel from dark image.
        pixelValue = histEquImage.getpixel((c, r))
        # Record count in histogram array.
        histEquHistogram[pixelValue] += 1

# Save histogram to csv file.
csvFile = open('histEqu histogram.csv', 'w')
writer = csv.writer(csvFile)
writer.writerow(histEquHistogram)

# Clear plot.
plt.gcf().clear()
# Plot histogram.
plt.bar(range(len(histEquHistogram)), histEquHistogram)
# Save histogram to image file.
plt.savefig('histEqu histogram.png')
# # Show plot.
# plt.show()