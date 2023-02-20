import cv2

# Define the video capture device (0 is usually the default webcam)
cap = cv2.VideoCapture(0)

# Define the color of the new background
background_img = ("image.png")

while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()
    
    # Create a mask based on the color of the original background
    lower_color = (0, 0, 0) # (B, G, R)
    upper_color = (50, 50, 50) # (B, G, R)
    mask = cv2.inRange(frame, lower_color, upper_color)

    # Invert the mask so that the background is white and the foreground is black
    mask = cv2.bitwise_not(mask)

    # Create a new image with the desired background color
    new_background = frame.copy()
    new_background = background_img

    # Use the mask to combine the original image and the new background
    final_image = cv2.bitwise_or(frame, frame, mask=mask)
    final_image = cv2.bitwise_or(final_image, new_background, mask=mask)

    # Show the final image
    cv2.imshow('Final Image', final_image)

    # Check for a key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close the window
cap.release()
cv2.destroyAllWindows()
