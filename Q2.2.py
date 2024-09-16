def separate_and_convert(s):
    # Separate into numbers and letters
    numbers = ''.join([char for char in s if char.isdigit()])
    letters = ''.join([char for char in s if char.isalpha()])

    # Convert even numbers in the number string to ASCII Decimal Values
    even_numbers_ascii = [ord(num) for num in numbers if int(num) % 2 == 0]

    # Convert uppercase letters in the letter string to ASCII Decimal Values
    uppercase_letters_ascii = [ord(char) for char in letters if char.isupper()]

    return even_numbers_ascii, uppercase_letters_ascii

# Example input
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'
even_numbers_ascii, uppercase_letters_ascii = separate_and_convert(s)

print("Even Numbers ASCII:", even_numbers_ascii)
print("Uppercase Letters ASCII:", uppercase_letters_ascii)
