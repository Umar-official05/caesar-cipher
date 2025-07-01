def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher")
    choice = input("Encrypt or Decrypt? (E/D): ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice.")
        return

    message = input("Enter message: ")
    try:
        shift = int(input("Enter shift value: "))
    except ValueError:
        print("Shift must be a number.")
        return

    if choice == 'E':
        print("Encrypted:", encrypt(message, shift))
    else:
        print("Decrypted:", decrypt(message, shift))

if __name__ == "__main__":
    main()
