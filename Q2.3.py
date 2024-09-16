def decrypt_cryptogram(cryptogram, shift_key):
    decrypted_message = []
    for char in cryptogram:
        if char.isalpha():
            # Shift the character by the given key
            shift = shift_key if char.isupper() else shift_key
            new_char = chr((ord(char) - shift - 65) % 26 + 65) if char.isupper() else chr((ord(char) - shift - 97) % 26 + 97)
            decrypted_message.append(new_char)
        else:
            # Keep non-alphabetical characters as they are
            decrypted_message.append(char)
    return ''.join(decrypted_message)

# Example cryptogram and shift key
cryptogram = "V2 FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVHGHXRF V NZ BHG BS PHAGFBY hAONG GVZrf unEQ gb unNaoyr..."
shift_key = 13  # You will need to find the correct key for your cryptogram

decrypted_message = decrypt_cryptogram(cryptogram, shift_key)
print("Decrypted Message:", decrypted_message)
