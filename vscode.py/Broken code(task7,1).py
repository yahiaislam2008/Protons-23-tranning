def caesar_decrypt(message, shift):

    decrypted = ""

    for char in message:
        letter_num = ord(char)- 96
        
        shifted_letter_num = (letter_num  -shift)%27
        
        shifted_letter =chr(shifted_letter_num +96)

        decrypted +=shifted_letter

    return decrypted

secret = "surwrqv"
decreypted_secret = caesar_decrypt(secret,3)

print(decreypted_secret)