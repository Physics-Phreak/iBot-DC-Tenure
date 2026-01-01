import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == "__main__":
    img = cv2.imread('data/scroll.jpg', cv2.IMREAD_GRAYSCALE)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].imshow(img, cmap='gray')
    axes[0].set_title('Original Image')

    axes[1].plot(hist)
    axes[1].set_title('Histogram')
    axes[1].set_xlabel('Intensity Value')
    axes[1].set_ylabel('Frequency')

    print("Median: ", np.median(img))
    print("Mean: ", np.mean(img))
    print("Standard Deviation: ", np.std(img))

    plt.tight_layout()
    plt.show()

