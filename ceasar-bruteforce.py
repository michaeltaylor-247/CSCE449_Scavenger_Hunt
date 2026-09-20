# caesar_bruteforce.py

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    plaintext = ""

    for char in ciphertext:
        if char == " ":
            plaintext += char
            continue

        plaintext += chr(
            (ord(char) - ord("a") - shift) % 26 + ord("a")
        )

    return plaintext


def main():
    ciphertext = input("Enter ciphertext: ").strip()

    print("\nTrying every possible Caesar shift:\n")

    for shift in range(26):
        plaintext = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift:2}: {plaintext}")


if __name__ == "__main__":
    main()
