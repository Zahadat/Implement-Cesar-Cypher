def caesar_cipher_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
    if choice == 'E':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'D':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
