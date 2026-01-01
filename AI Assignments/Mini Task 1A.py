import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == "__main__":
    img_raw = cv2.imread('data/scroll.jpg', cv2.IMREAD_GRAYSCALE)

    img_blurred = cv2.GaussianBlur(img_raw, (7, 7), 0)
    img_canny = cv2.Canny(img_blurred, 50, 150)
    img_thresh = cv2.threshold(img_canny, 127, 255, cv2.THRESH_BINARY)[1]

    fig, axes = plt.subplots(2, 2, figsize=(15, 5))
    axes = axes.ravel()

    axes[0].imshow(img_raw, cmap='gray')
    axes[0].set_title('Original Image')

    axes[1].imshow(img_blurred, cmap='gray')
    axes[1].set_title('Blurred Image')

    axes[2].imshow(img_canny, cmap='gray')
    axes[2].set_title('Canny Edges')

    axes[3].imshow(img_thresh, cmap='gray')
    axes[3].set_title('Thresholded Image')

    plt.tight_layout()
    plt.show()