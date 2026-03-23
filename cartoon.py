import cv2

def cartoonize_image(input_path, output_path):
    # Load the input image
    img = cv2.imread(input_path)

    # Check if the image was loaded successfully
    if img is None:
        print(f"Error: Could not load {input_path}")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reduce noise while preserving edges
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    # Smooth colors while preserving boundaries
    color = cv2.bilateralFilter(img, 9, 250, 250)

    # Combine the color image with the edge mask
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Save output image
    cv2.imwrite(output_path, cartoon)
    print(f"Saved: {output_path}")

# Process the good example image
cartoonize_image("good_image.jpeg", "good_output.jpg")

# Process the bad example image
cartoonize_image("bad_image.jpeg", "bad_output.jpg")