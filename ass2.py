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

# Step 6: Extract the red channel and sum all the red pixel values
# OpenCV loads images in BGR format, so the red channel is the last one
red_channel = modified_img[:, :, 2]  # 2 is the index for the red channel
red_sum = np.sum(red_channel)

# Step 7: Print the sum of the red pixel values
print("The sum of all red pixel values in the modified image is:", red_sum)


# CHAPTER 2

import re

# Step 1: Define the string
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'

# Step 2: Separate numbers and letters using regular expressions
number_string = ''.join(re.findall(r'\d', s))
letter_string = ''.join(re.findall(r'[a-zA-Z]', s))

print("Number string:", number_string)
print("Letter string:", letter_string)

# Step 3: Convert even numbers to ASCII decimal values
even_numbers = [int(ch) for ch in number_string if int(ch) % 2 == 0]
ascii_even_numbers = [ord(str(ch)) for ch in even_numbers]

print("Even numbers in number string:", even_numbers)
print("ASCII values of even numbers:", ascii_even_numbers)

# Step 4: Convert upper-case letters to ASCII decimal values
upper_case_letters = [ch for ch in letter_string if ch.isupper()]
ascii_upper_case_letters = [ord(ch) for ch in upper_case_letters]

print("Upper-case letters in letter string:", upper_case_letters)
print("ASCII values of upper-case letters:", ascii_upper_case_letters)

# Define the ciphered quote
ciphered_quote = "V2 FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVHGHXRF V NZ BHG BS PHAGFBY hAONG GVZrf unEQ gb unNaoyr OHg Vs LOH PHAG UNAQYR ZR NG ZL 30EFG GURA LDH FHER NF URYYQBAG QRFREIR ZR NS ZL ORFG ZNEVYLA ZBAEBR"

# Caesar cipher decryption function
def decrypt_caesar(cipher_text, shift):
    decrypted_text = []
    for char in cipher_text:
        if 'A' <= char <= 'Z':
            decrypted_text.append(chr((ord(char) - shift - 65) % 26 + 65))
        elif 'a' <= char <= 'z':
            decrypted_text.append(chr((ord(char) - shift - 97) % 26 + 97))
        else:
            decrypted_text.append(char)  # Keep non-alphabet characters as is
    return ''.join(decrypted_text)

# Define the shift key (you can adjust the value if you know the key)
shift_key = 13  # Example shift value for Caesar cipher

# Decrypt and print the deciphered quote
deciphered_quote = decrypt_caesar(ciphered_quote, shift_key)
print("Deciphered Quote:", deciphered_quote)

