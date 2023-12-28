import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Define font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
font_color = (255, 255, 255)  # White color

# Define text and positions for each planet
planet_texts = {
    "Sun": (50, 80),
    "Mercury": (50, 180),
    "Venus": (180, 160),
    "Earth": (280, 160),
    "Moon": (280, 120),
    "Mars": (380, 160),
    "Jupiter": (580, 50),
    "Saturn": (780, 130),
    "Uranus": (950, 150),
    "Neptune": (1080, 150)
}

# Add text for each planet
for planet, position in planet_texts.items():
    cv2.putText(img, planet, position, font, font_scale, font_color, font_thickness)

# Display the image
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_system_with_name.jpg", img)

# Close the OpenCV window
cv2.destroyAllWindows()
