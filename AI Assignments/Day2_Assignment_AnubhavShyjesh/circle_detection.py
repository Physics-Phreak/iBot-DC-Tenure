import cv2
import numpy as np
import matplotlib . pyplot as plt

def inputHandler():
    """
    This functions handles user inputs for image path.
    It ensures that the image path is valid, that the image can be read.
    Returns:
        img_raw (numpy.ndarray): The image read from the specified path. It is in RGB format.
        path (str): The path of the input image.
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
        min_dist = input("Enter minimum distance between circles: ")
        if not min_dist.isdigit() or int(min_dist) <= 0:
            print("Invalid minimum distance. Please enter a positive integer.")
        else:
            input_issue = False

    input_issue = True
    while input_issue:
        min_radius = input("Enter minimum radius of circles: ")
        if not min_radius.isdigit() or int(min_radius) <= 0:
            print("Invalid minimum radius. Please enter a positive integer.")
        else:
            input_issue = False
    
    input_issue = True
    while input_issue:
        max_radius = input("Enter maximum radius of circles: ")
        if not max_radius.isdigit() or int(max_radius) <= 0:
            print("Invalid maximum radius. Please enter a positive integer.")
        else:
            input_issue = False

    input_issue = True
    while input_issue:
        param2 = input("Enter param2 for Hough Circles detections: ")
        if not param2.isdigit() or int(param2) <= 0:
            print("Invalid param2. Please enter a positive integer.")
        else:
            input_issue = False
    
    return img_raw, path, int(min_dist), int(min_radius), int(max_radius), int(param2)


def preprocess_image (img_raw, blur_kernel_size = 5):
    """
    Preprocesses the raw image.
    Args:
        img_raw (numpy.ndarray): The raw image in RGB format.
        blur_kernel_size (int): The size of the Gaussian blur kernel (must be an odd integer).
    Returns:
        img_processed (numpy.ndarray): The processed image in grayscale format.
    """
    img_gray = cv2.cvtColor(img_raw, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (blur_kernel_size, blur_kernel_size), 0)
    return img_blur

def detect_circles (gray_image , dp =1 , minDist =50 , param1 =50 ,
                    param2 =30 , minRadius =10 , maxRadius =100):
    circle_info = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, dp, minDist,
                                   param1=param1, param2=param2,
                                   minRadius=minRadius, maxRadius=maxRadius)
    if circle_info is None:
        return circle_info
    
    circle_info = np.uint16(np.around(circle_info))
    return circle_info

def visualize_circles (image_color, circle_info, save_path = None):
    img_annotated = image_color.copy()
    for (x, y, r) in circle_info[0]:
        cv2.circle(img_annotated, (x, y), r, (0, 255, 0), 2)
        cv2.circle(img_annotated, (x, y), 2, (255, 0, 0), 3)

    cv2.imwrite(save_path, img_annotated)

    return img_annotated

def calculate_statistics (circle_info):
    if circle_info is None:
        return "No circles detected."
    
    num_circles = len(circle_info[0])
    
    total_radius = sum(circle_info[0][:,2])
    
    max_radius = max(circle_info[0][:,2])
    min_radius = min(circle_info[0][:,2])
    avg_radius = total_radius / num_circles if num_circles > 0 else 0
    
    print(f"Number of circles detected: {num_circles}")
    print(f"Average radius: {avg_radius:.2f}")
    print(f"Maximum radius: {max_radius}")
    print(f"Minimum radius: {min_radius}")

    print("Circle Coordinates and Radii:")
    for (x, y, r) in circle_info[0]:
        print(f"Center: ({x}, {y}), Radius: {r}")

    return {
        "number_of_circles": num_circles,
        "average_radius": avg_radius,
        "max_radius": max_radius,
        "min_radius": min_radius
    }

if __name__ == "__main__":
    img_raw, input_path, min_dist, min_radius, max_radius, param2 = inputHandler()
    img_processed = preprocess_image(img_raw, blur_kernel_size=5)

    output_path = input_path.replace(".", "_annotated.")

    circle_info = detect_circles(img_processed, minDist=min_dist, minRadius=min_radius, maxRadius=max_radius, param2=param2)
    if circle_info is not None:
        img_annotated = visualize_circles(img_raw, circle_info, save_path=output_path)
    else:
        img_annotated = img_raw.copy()

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    axes[0].imshow(img_raw)
    axes[0].set_title('Original Image')
    axes[1].imshow(img_annotated)
    axes[1].set_title('Annotated Image')

    plt.tight_layout()
    plt.show()

    stats = calculate_statistics(circle_info)
    stats_output_path = input_path.replace(".", "_stats.txt")

    with open(stats_output_path, "w") as f:
        if circle_info is None:
            f.write("No circles detected.\n")
        else:
            f.write("Parameters Used:\n")
            f.write(f"minDist: {min_dist}\n")
            f.write(f"minRadius: {min_radius}\n")
            f.write(f"maxRadius: {max_radius}\n")
            f.write(f"param2: {param2}\n")
            f.write("\nStatistics:\n")
            f.write(f"Number of circles detected: {stats['number_of_circles']}\n")
            f.write(f"Average radius: {stats['average_radius']:.2f}\n")
            f.write(f"Maximum radius: {stats['max_radius']}\n")
            f.write(f"Minimum radius: {stats['min_radius']}\n")
            f.write("Circle Coordinates and Radii:\n")
            for (x, y, r) in circle_info[0]:
                f.write(f"Center: ({x}, {y}), Radius: {r}\n")