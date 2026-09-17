# caesar_bruteforce.py

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")

            decrypted = chr(
                (ord(char) - base - shift) % 26 + base
            )

            plaintext += decrypted
        else:
            plaintext += char

    return plaintext


def main():
    ciphertext = input("Enter ciphertext: ").strip()

    print("\nTrying every possible Caesar shift:\n")

    for shift in range(26):
        plaintext = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift:2}: {plaintext}")


if __name__ == "__main__":
    main()
