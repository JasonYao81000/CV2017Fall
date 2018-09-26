from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv

# Load image from file.
originalImage = Image.open('lena.bmp')

# Get width and height of image.
width, height = originalImage.size
# print ('width = %d, height = %d' %(width, height))

# Create histogram array with zeros.
histogram = np.zeros(256)

# Process image pixel by pixel.
for c in range(width):
    for r in range(height):
        # Get pixel from original image.
        pixelValue = originalImage.getpixel((c, r))
        # Record count in histogram array.
        histogram[pixelValue] += 1

# Save histogram to csv file.
csvFile = open('histogram.csv', 'w')
writer = csv.writer(csvFile)
writer.writerow(histogram)

# Plot histogram.
plt.bar(range(len(histogram)), histogram)
# Save histogram to image file.
plt.savefig('histogram.png')
# Show plot.
plt.show()