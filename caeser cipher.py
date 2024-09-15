def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    Args:
        text (str): The text to be encrypted or decrypted.
        shift (int): The shift value for the Caesar Cipher.
        mode (str): 'encrypt' or 'decrypt' to specify the operation.

    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            if mode == 'encrypt':
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            elif mode == 'decrypt':
                result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char

    return result


def main():
    # Input text
    text = input("Enter the text to be encrypted/decrypted: ")
    
    # Input shift value with validation
    while True:
        try:
            shift = int(input("Enter the shift value (integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the shift value.")
    
    # Input mode with validation
    while True:
        mode = input("Do you want to (e)ncrypt or (d)ecrypt? ").strip().lower()
        if mode in ('e', 'encrypt', 'd', 'decrypt'):
            break
        else:
            print("Invalid mode. Please enter 'e' for encryption or 'd' for decryption.")
    
    # Process mode
    if mode in ('e', 'encrypt'):
        encrypted_text = caesar_cipher(text, shift, 'encrypt')
        print("Encrypted text:", encrypted_text)
    elif mode in ('d', 'decrypt'):
        decrypted_text = caesar_cipher(text, shift, 'decrypt')
        print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()