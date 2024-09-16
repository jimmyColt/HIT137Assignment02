from PIL import Image
import time

# Generate the number
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print("Generated Number:", generated_number)

# Open the provided image
image = Image.open("Chapter1.png")
pixels = image.load()

# Modify the image by adding the generated number to each (r,g,b) value
width, height = image.size
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        pixels[x, y] = (r + generated_number, g + generated_number, b + generated_number)

# Save the new image as "chapter1out.png"
image.save("chapter1out.png")

# Sum all the red pixel values in the new image
sum_of_red_pixels = 0
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        sum_of_red_pixels += r

print("Sum of Red Pixels:", sum_of_red_pixels)
