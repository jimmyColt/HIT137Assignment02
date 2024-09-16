import cv2
import numpy as np
import time

# Step 1: Load the image from the given path using OpenCV
img_path = r'C:\Users\JAMES\Documents\JAPA\CDU\HIT137\Assignment 2\chapter1.jpg'
image = cv2.imread(img_path)

# Step 2: Generate a number based on the current time
current_time = int(time.time())
generated_number = (current_time % 100) + 50

# If the number is even, add 10 to it
if generated_number % 2 == 0:
    generated_number += 10

# Step 3: Add the generated number to each pixel's RGB values
# Since OpenCV loads images in BGR format, we add the generated number to all three channels (B, G, R)
modified_img = cv2.add(image, (generated_number, generated_number, generated_number, 0))

# Step 4: Save the modified image
output_path = r'C:\Users\JAMES\Documents\JAPA\CDU\HIT137\Assignment 2\chapter1out.png'
cv2.imwrite(output_path, modified_img)

print("Modified image saved at:", output_path)
