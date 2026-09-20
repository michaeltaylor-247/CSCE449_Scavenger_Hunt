import random
import re
import math

QUADGRAMS = {
    "that": 10000, "ther": 9000, "with": 8500, "tion": 8000, "here": 7500,
    "ould": 7000, "ight": 6500, "have": 6000, "hich": 5500, "this": 5000,
    "thin": 4500, "they": 4000, "atio": 3500, "ever": 3000, "from": 2500,
    "ough": 2400, "pres": 2300, "ment": 2200, "comp": 2100, "cons": 2000,
    "ever": 1900, "very": 1850, "eryw": 1800, "rywh": 1750, "ywhe": 1700,
    "wher": 1650, "eere": 1550, "unde": 1500, "nder": 1450, "dern": 1400,
    "erne": 1350, "neat": 1300, "eath": 1250, "know": 1200, "nowl": 1150,
    "owle": 1100, "wled": 1050, "ledg": 1000, "edge": 950, "look": 900,
    "floo": 850, "loor": 800, "need": 750, "eede": 700, "eded": 650,
    "deep": 600, "thei": 550, "heir": 500, "runs": 450, "under": 1400,
    "rnea": 1300, "eath": 1200, "aiss": 500, "isne": 600, "snee": 600,
    "eede": 600, "eded": 600, "their": 700, "eirk": 400, "irkn": 400,
    "rknow": 500, "nowl": 600, "owle": 600, "wled": 600, "ledge": 600,
    "edger": 400, "dgeru": 400, "gerun": 400, "eruns": 500, "runsd": 400,
    "unsde": 400, "nsdee": 400, "sdeep": 500, "ookev": 400, "okeve": 400,
    "kever": 500, "erywh": 600, "rywhe": 600, "ywher": 600, "where": 700,
    "hereb": 400, "erebu": 400, "rebut": 500, "butth": 600, "utthe": 600,
    "thefl": 600, "heflo": 500, "efloo": 500, "floor": 700, "loor": 600,
    "ooru": 400, "orund": 400, "runde": 500, "derne": 600, "erneat": 600
}

class SubstitutionBruteForce:
    def __init__(self, ciphertext: str):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.raw_ciphertext = ciphertext.lower()
        self.clean_ciphertext = re.sub(r'[^a-z]', '', self.raw_ciphertext)
        self.floor = math.log10(0.01 / sum(QUADGRAMS.values()))
        self.quadgrams = self._load_quadgrams()

    def _load_quadgrams(self):
        total = sum(QUADGRAMS.values())
        return {k: math.log10(v / total) for k, v in QUADGRAMS.items()}

    def score(self, text: str) -> float:
        score = 0.0
        for i in range(len(text) - 3):
            quadgram = text[i:i + 4]
            if quadgram in self.quadgrams:
                score += self.quadgrams[quadgram]
            else:
                score += self.floor
        return score

    def decrypt(self, text: str, key: str) -> str:
        translation_table = str.maketrans(key, self.alphabet)
        return text.translate(translation_table)

    def solve(self, restarts: int = 5, max_iterations: int = 3000):
        best_score = float('-inf')
        best_key = None

        print("Starting brute-force substitution cipher solver...")

        for _ in range(restarts):
            parent_key = list(self.alphabet)
            random.shuffle(parent_key)
            parent_key = ''.join(parent_key)

            decrypted_text = self.decrypt(self.clean_ciphertext, parent_key)
            parent_score = self.score(decrypted_text)

            for _ in range(max_iterations):
                child_key = list(parent_key)
                a, b = random.sample(range(len(child_key)), 2)
                child_key[a], child_key[b] = child_key[b], child_key[a]
                child_key = ''.join(child_key)

                decrypted_text = self.decrypt(self.clean_ciphertext, child_key)
                child_score = self.score(decrypted_text)

                if child_score > parent_score:
                    parent_key = child_key
                    parent_score = child_score

            if parent_score > best_score:
                best_score = parent_score
                best_key = parent_key

        final_decrypted_text = self.decrypt(self.raw_ciphertext, best_key)
        return final_decrypted_text, best_key

if __name__ == "__main__":
    print("Simple Substitution Cipher Brute Force Solver")
    user_input = input("Enter the ciphertext: ")

    if not user_input:
        print("No ciphertext provided. Exiting.")
    else:
        solver = SubstitutionBruteForce(user_input)
        decrypted_text, key = solver.solve(restarts=5, max_iterations=3000)
        print("\n" + "="*40)
        print("result:")
        print("="*40)
        print(f"decrypted text:\n{decrypted_text}\n")
        print(f"alphabet: {solver.alphabet}")
        print(f"cipher  : {key}")

# k ok xf szzaza otzxg bsdhvzaqz gmsf azze x vddb zyzguhtzgz nmo otz ivddg msazgszkot