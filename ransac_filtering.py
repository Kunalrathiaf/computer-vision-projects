import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the images in grayscale
img1 = cv2.imread('image_1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('image_2.jpg', cv2.IMREAD_GRAYSCALE)

# Optional: check if images loaded correctly
if img1 is None or img2 is None:
    print("Error loading images. Check filenames and paths.")
    exit()

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Use Brute-Force matcher to find the two best matches for each descriptor
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Apply Lowe's ratio test
good_matches = []
pts1 = []
pts2 = []

for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)
        pts1.append(kp1[m.queryIdx].pt)
        pts2.append(kp2[m.trainIdx].pt)

# Convert to NumPy arrays
pts1 = np.float32(pts1)
pts2 = np.float32(pts2)

# Use RANSAC to compute a homography and filter out outliers
H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC)
matches_mask = mask.ravel().tolist()

# Draw only inlier matches
result = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None,
                         matchesMask=matches_mask, flags=2)

# Show the result
plt.figure(figsize=(12, 6))
plt.title("RANSAC Filtered Feature Matches")
plt.imshow(result)
plt.axis('off')
plt.show()
