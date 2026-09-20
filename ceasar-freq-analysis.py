from collections import Counter

# Approximate frequency of English letters
ENGLISH_FREQUENCIES = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074,
}


# Deciphering by shifting the opposite way
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


def chi_squared_score(text: str) -> float:
    """
    Compare the letter frequencies in text against expected
    English letter frequencies.

    Lower score means the text is more English-like.
    """

    letters = text.replace(" ", "")
    counts = Counter(letters)
    total = len(letters)

    score = 0.0

    for letter, expected_percentage in ENGLISH_FREQUENCIES.items():
        observed = counts.get(letter, 0)
        expected = total * (expected_percentage / 100)

        score += ((observed - expected) ** 2) / expected

    return score


def main():
    ciphertext = input("Enter ciphertext: ").strip()

    candidates = []

    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        score = chi_squared_score(decrypted)

        candidates.append((score, shift, decrypted))

    # Lower chi-squared score means a better statistical match
    # to normal English letter frequencies.
    candidates.sort()

    print("\nFrequency-analysis candidates (lowest score first):")
    print("Inspect all candidates and identify the readable plaintext.\n")

    for score, shift, decrypted in candidates:
        print(f"Shift: {shift:2}")
        print(f"Score: {score:.2f}")
        print(f"Text:  {decrypted}")
        print()


if __name__ == "__main__":
    main()
