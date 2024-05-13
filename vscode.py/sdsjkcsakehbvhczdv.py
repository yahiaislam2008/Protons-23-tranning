def caesar_decrypt(secret):

    decrypted = " "

    for char in range(0,len(secret)):
        letter_num = ord(secret[char]) -97
        shifted_letter_num = (letter_num) %27

        shifted_letter = chr(shifted_letter_num+97)

        decrypted += shifted_letter

    return decrypted

secret = "surwrqv"
decreypted_secret = caesar_decrypt(secret)

def encrypt_secret(w,s):
    
    encrypt=""
    for char in w:
        #if char.islower():
            encrypt+=chr((ord(char)+s-96)%27 +96)

    return encrypt
def decrypt_secret(w,s):
    
    decreypted=" "
    for char in w:
            decreypted +=chr((ord(char)-s-96 )%27 +96)

    return decreypted
secret1="surwrqv"
#encryptsecret=encrypt_secret(secret1,2)
#print(encryptsecret)
decrypt=decrypt_secret(secret1,2)
print(decrypt)
