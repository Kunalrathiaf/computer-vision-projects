# Computer Vision Projects with OpenCV

This repository contains implementations of three key computer vision algorithms using OpenCV in Python:

1. **SIFT (Scale-Invariant Feature Transform)** – to detect and match keypoints between two images.
2. **RANSAC (Random Sample Consensus)** – to remove outlier keypoint matches and fit a transformation model.
3. **Harris Corner Detector** – to detect and visualize corner points in grayscale images.

---

## Technologies Used

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

---

## Folder Structure


---

## Project Descriptions

### 1. SIFT Keypoint Detection and Matching
Detects keypoints using the SIFT algorithm and matches them using a brute-force matcher with a ratio test. The result shows correspondences between two images.

> File: `sift_matching.py`

### 2. RANSAC for Outlier Removal
Applies RANSAC to filter out incorrect matches from SIFT and estimates a homography (perspective transformation) between two images.

> File: `ransac_filtering.py`

### 3. Harris Corner Detection
Detects corner points in a grayscale image using the Harris algorithm and visualizes them in red.

> File: `harris_corners.py`

---

## Sample Results

> Add screenshots of output visualizations here.  
> Use `plt.savefig()` or take screenshots and upload them.

---

## How to Run

1. Clone this repository:
```bash
git clone https://github.com/yourusername/computer-vision-projects.git
cd computer-vision-projects
