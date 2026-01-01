import numpy as np
import matplotlib.pyplot as plt
import cv2

def inputHandler():
    """
    This functions handles user inputs for image path and Gaussian blur size.
    It ensures that the image path is valid, that the image can be read, and that the blur size is a valid odd integer.
    Returns:
        img_raw (numpy.ndarray): The image read from the specified path. It is in RGB format.
        gaussian_blur_size (int): The size of the Gaussian blur kernel.
    """
    input_issue = True
    while input_issue:
        path = input("Enter the path of the image: ")
        try:
            img_raw = cv2.imread(path, cv2.IMREAD_COLOR_RGB)
            if img_raw is None:
                print("Image not found or unable to read.")
                continue
            input_issue = False
        except Exception as e:
            print(f"Error: {e}. Please try again.")

    input_issue = True
    while input_issue:
        try:
            gaussian_blur_size = int(input("Enter the Gaussian blur size (odd integer): "))
            if gaussian_blur_size % 2 == 0 or gaussian_blur_size <= 0:
                print("Please enter a valid odd integer greater than 0.")
                continue
            input_issue = False
        except ValueError:
            print("Invalid input. Please enter an odd integer.")

    return img_raw, gaussian_blur_size

def pencil_sketch_gray(img_raw, gaussian_blur_size):
    """
    Docstring for pencil_sketch_gray

    :param img_raw: The image read from the specified path. It is in RGB format.
    :param gaussian_blur_size: The size of the Gaussian blur kernel.

    :return: A tuple containing:
        img_gray (numpy.ndarray): The grayscale version of the input image.
        img_inv_blurred (numpy.ndarray): The inverted blurred image.
        final (numpy.ndarray): The final pencil sketch image in grayscale.
    """
    img_gray = cv2.cvtColor(img_raw, cv2.COLOR_RGB2GRAY).astype(np.float32) # Convert to grayscale

    #Genergating the blurred inverted image
    img_inv = 255 - img_gray
    img_inv_blurred = cv2.GaussianBlur(img_inv, (gaussian_blur_size, gaussian_blur_size), 0)
    img_inv_blurred_inv = 255 - img_inv_blurred + 1e-6
    
    #Generating the final pencil sketch image
    sketch_img = cv2.divide(img_gray, img_inv_blurred_inv.astype(np.float32), scale=256.0)
    final = np.clip(sketch_img, 0, 255).astype(np.uint8)
    return img_gray, img_inv_blurred.astype(np.uint8), final

def pencil_sketch_color(img_raw, gaussian_blur_size):
    """
    Docstring for pencil_sketch_color
    :param img_raw: The image read from the specified path. It is in RGB format.
    :param gaussian_blur_size: The size of the Gaussian blur kernel.
    :return: A tuple containing:
        img_gray (numpy.ndarray): The grayscale version of the input image.
        img_inv_blurred (numpy.ndarray): The inverted blurred image.
        img_HSV (numpy.ndarray): The final pencil sketch image in HSV color space.
    """

    # Generating the grayscale pencil sketch (Value channel is basically grayscale pencil sketch)
    img_gray, img_inv_blurred, img_v = pencil_sketch_gray(img_raw, gaussian_blur_size)


    # Generating the final color pencil sketch image in HSV color space
    img_HSV = cv2.cvtColor(img_raw, cv2.COLOR_RGB2HSV)
    img_HSV[:, :, 2] = img_v #value channel substitued 
    img_HSV[:, :, 1] = np.clip(img_HSV[:, :, 1] * 0.5, 0, 255).astype(np.uint8) #saturation reduced
    return img_gray, img_inv_blurred, img_HSV

if __name__ == "__main__":

    img_raw, gaussian_blur_size = inputHandler()
    _, _, gray_sketch = pencil_sketch_gray(img_raw, gaussian_blur_size)
    _, _, color_sketch = pencil_sketch_color(img_raw, gaussian_blur_size)
    color_sketch = cv2.cvtColor(color_sketch, cv2.COLOR_HSV2RGB)

    # Displaying the results
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(img_raw)
    axes[0].set_title('Original Image')
    axes[1].imshow(gray_sketch, cmap='gray')
    axes[1].set_title('Gray Sketch Image')
    axes[2].imshow(color_sketch)
    axes[2].set_title('Color Sketch Image')

    plt.tight_layout()
    plt.show()

    #Saving the files
    cv2.imwrite('gray_sketch.png', gray_sketch)
    cv2.imwrite('color_sketch.png', cv2.cvtColor(color_sketch, cv2.COLOR_RGB2BGR))
