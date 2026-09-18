import re
from collections import Counter

class InteractiveFrequencySolver:
    def __init__(self, ciphertext: str):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.raw_ciphertext = ciphertext.lower()
        self.clean_ciphertext = re.sub(r'[^a-z]', '', self.raw_ciphertext)
        self.english_freq = 'etaoinshrdlcumwfgypbvkjxqz'

    def generate_initial_key(self) -> list[str]:
        letter_counts = Counter(self.clean_ciphertext)
        present_sorted = [item[0] for item in letter_counts.most_common()]
        missing = [c for c in self.alphabet if c not in present_sorted]
        full_cipher_sorted = present_sorted + missing

        # Map each cipher letter to English frequency rank
        cipher_to_english = {}
        for cipher_char, eng_char in zip(full_cipher_sorted, self.english_freq):
            cipher_to_english[cipher_char] = eng_char

        # Return key array aligned with 'a-z'
        return [cipher_to_english[char] for char in self.alphabet]

    def decrypt(self, key_list: list[str]) -> str:
        key_str = "".join(key_list)
        translation_table = str.maketrans(self.alphabet, key_str)
        return self.raw_ciphertext.translate(translation_table)

    def start_interactive_session(self):
        current_key = self.generate_initial_key()

        while True:
            decrypted = self.decrypt(current_key)
            print("\n" + "="*50)
            print("CURRENT DECRYPTION:")
            print("="*50)
            print(f"{decrypted}\n")
            print(f"Alphabet: {self.alphabet}")
            print(f"Key     : {''.join(current_key)}")
            print("="*50)

            user_choice = input("Swap two decrypted letters (e.g., 'e a') or 'q' to quit: ").strip().lower()
            if user_choice == 'q':
                break

            parts = user_choice.split()
            if len(parts) == 2 and len(parts[0]) == 1 and len(parts[1]) == 1:
                char1, char2 = parts[0], parts[1]
                if char1 in current_key and char2 in current_key:
                    idx1, idx2 = current_key.index(char1), current_key.index(char2)
                    current_key[idx1], current_key[idx2] = current_key[idx2], current_key[idx1]
                else:
                    print("One or both characters not found in key.")
            else:
                print("Invalid input. Type two space-separated letters, like 'i a'")

if __name__ == "__main__":
    print("=== Interactive Frequency Analysis Decrypter ===")
    user_input = input("Enter the ciphertext:\n> ").strip()

    if user_input:
        solver = InteractiveFrequencySolver(user_input)
        solver.start_interactive_session()

# k ok xf szzaza otzxg bsdhvzaqz gmsf azze x vddb zyzguhtzgz nmo otz ivddg msazgszkot 