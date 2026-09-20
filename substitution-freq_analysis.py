import re
import math
import random
from collections import Counter

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# English letters ordered from most common to least common.
ENGLISH_FREQUENCY_ORDER = "etaoinshrdlcumwfgypbvkjxqz"

# Common English sequences. Longer matches receive more weight because they
# are much less likely to occur accidentally than individual letters.
COMMON_BIGRAMS = set(
    "th he in er an re on at en nd ti es or te of ed is it al ar st to nt ng "
    "se ha as ou io le ve co me de hi ri ro ic ne ea ra ce li ch ll be ma si om ur"
    .split()
)
COMMON_TRIGRAMS = set(
    "the and ing her ere ent tha nth was eth for dth hat she ion tio ver est ers "
    "ati his all ith hes ter con rea not you wit but thi have one our out who how "
    "man pro com are ill can nee dee run und der loo now led eve whe ear eat ath"
    .split()
)
COMMON_QUADGRAMS = set(
    "tion nthe ther that ofth fthe ethe with ment ions this here ould ight have "
    "hich whic ctio atio ever from ough were hing them thin they know need deep "
    "look unde floor where edge"
    .split()
)


def generate_frequency_key(ciphertext: str) -> str:
    """Create a cipher-to-plaintext key using letter-frequency ranks."""
    clean_ciphertext = re.sub(r"[^a-z]", "", ciphertext.lower())
    counts = Counter(clean_ciphertext)

    # Rank letters that occur, then append absent letters so the key contains
    # one mapping for every letter in the alphabet.
    cipher_frequency_order = [letter for letter, _ in counts.most_common()]
    cipher_frequency_order.extend(
        letter for letter in ALPHABET if letter not in counts
    )

    cipher_to_plaintext = dict(
        zip(cipher_frequency_order, ENGLISH_FREQUENCY_ORDER)
    )

    # Position 0 is the plaintext guess for cipher "a", position 1 for "b",
    # and so on.
    return "".join(cipher_to_plaintext[letter] for letter in ALPHABET)


def substitution_decrypt(ciphertext: str, key: str) -> str:
    """Decrypt while preserving the input's spaces and punctuation."""
    translation_table = str.maketrans(ALPHABET, key)
    return ciphertext.lower().translate(translation_table)


def english_score(text: str) -> float:
    """Score text using common, general-purpose English letter sequences."""
    clean_text = re.sub(r"[^a-z]", "", text)
    score = 0.0

    for index in range(len(clean_text) - 1):
        if clean_text[index:index + 2] in COMMON_BIGRAMS:
            score += 1.0

    for index in range(len(clean_text) - 2):
        if clean_text[index:index + 3] in COMMON_TRIGRAMS:
            score += 3.0

    for index in range(len(clean_text) - 3):
        if clean_text[index:index + 4] in COMMON_QUADGRAMS:
            score += 6.0

    return score


def improve_key(ciphertext: str, initial_key: str,
                restarts: int = 20, iterations: int = 10000) -> str:
    """Improve a frequency key with automatic swaps and simulated annealing."""
    random_source = random.Random(ciphertext)
    best_key = initial_key
    best_score = english_score(substitution_decrypt(ciphertext, best_key))

    for restart in range(restarts):
        current_key = list(initial_key)

        # Later restarts begin near, but not exactly at, the frequency guess.
        for _ in range(restart):
            first, second = random_source.sample(range(26), 2)
            current_key[first], current_key[second] = (
                current_key[second], current_key[first]
            )

        current_score = english_score(
            substitution_decrypt(ciphertext, "".join(current_key))
        )
        temperature = 5.0

        for _ in range(iterations):
            first, second = random_source.sample(range(26), 2)
            current_key[first], current_key[second] = (
                current_key[second], current_key[first]
            )
            candidate_score = english_score(
                substitution_decrypt(ciphertext, "".join(current_key))
            )
            difference = candidate_score - current_score

            if difference >= 0 or random_source.random() < math.exp(
                difference / temperature
            ):
                current_score = candidate_score
                if current_score > best_score:
                    best_score = current_score
                    best_key = "".join(current_key)
            else:
                current_key[first], current_key[second] = (
                    current_key[second], current_key[first]
                )

            temperature = max(0.1, temperature * 0.9995)

    return best_key


def main():
    ciphertext = input("Enter ciphertext: ").strip()

    if not ciphertext:
        print("No ciphertext provided.")
        return

    initial_key = generate_frequency_key(ciphertext)
    key = improve_key(ciphertext, initial_key)
    decrypted = substitution_decrypt(ciphertext, key)

    print("\nMost likely decryption:\n")
    print(f"Alphabet: {ALPHABET}")
    print(f"Key:      {key}")
    print(f"Text:     {decrypted}")


if __name__ == "__main__":
    main()

# k ok xf szzaza otzxg bsdhvzaqz gmsf azze x vddb zyzguhtzgz nmo otz ivddg msazgszkot
