def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted text: {encrypted_text}")

        elif choice == "2":
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted text: {decrypted_text}")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 for encryption, 2 for decryption, or 3 to exit.")
