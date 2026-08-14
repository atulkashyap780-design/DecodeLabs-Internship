def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


print("=== Basic Encryption & Decryption ===")

message = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift key (1-25): "))

encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("\nOriginal text :", message)
print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)