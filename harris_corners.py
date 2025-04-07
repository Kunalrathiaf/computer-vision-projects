import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in color and convert to grayscale
img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Apply Harris corner detection
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Dilate the result to mark corners
dst = cv2.dilate(dst, None)

# Threshold to mark the corners on the original image
img[dst > 0.01 * dst.max()] = [0, 0, 255]  # Red color

# Show result using matplotlib
plt.figure(figsize=(6, 6))
plt.title("Harris Corner Detection")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
