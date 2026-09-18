def rail_pattern(length: int, rails: int) -> list[int]:
    """
    Return the rail index used by each character position.

    Example for rails=3 and length=10:
    0, 1, 2, 1, 0, 1, 2, 1, 0, 1
    """
    pattern = []
    rail = 0
    direction = 1

    for _ in range(length):
        pattern.append(rail)

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    return pattern


def rail_fence_decrypt(ciphertext: str, rails: int) -> str:
    """
    Decrypt a Rail Fence cipher given the number of rails.
    """

    length = len(ciphertext)

    # Step 1: Determine which rail each plaintext position belongs to.
    pattern = rail_pattern(length, rails)

    # Step 2: Count how many characters belong to each rail.
    rail_counts = [pattern.count(r) for r in range(rails)]

    # Step 3: Split the ciphertext into the appropriate rail segments.
    rail_contents = []
    index = 0

    for count in rail_counts:
        rail_contents.append(list(ciphertext[index:index + count]))
        index += count

    # Step 4: Walk through the zig-zag pattern and pull characters
    # from the appropriate rail.
    rail_positions = [0] * rails
    plaintext = []

    for rail in pattern:
        plaintext.append(
            rail_contents[rail][rail_positions[rail]]
        )

        rail_positions[rail] += 1

    return "".join(plaintext)


def draw_rails(plaintext: str, rails: int) -> None:
    """
    Draw the plaintext in Rail Fence zig-zag form.
    """

    pattern = rail_pattern(len(plaintext), rails)

    grid = [
        [" " for _ in range(len(plaintext))]
        for _ in range(rails)
    ]

    for column, char in enumerate(plaintext):
        rail = pattern[column]
        grid[rail][column] = char

    for rail_number, row in enumerate(grid):
        print(f"Rail {rail_number + 1}: ", end="")

        for char in row:
            if char == " ":
                print(". ", end="")
            else:
                print(f"{char} ", end="")

        print()


def main():
    ciphertext = input("Enter ciphertext: ").strip()

    print("\nTrying rail counts from 2 through 6:\n")

    for rails in range(2, 7):
        plaintext = rail_fence_decrypt(ciphertext, rails)

        print("=" * 70)
        print(f"Rails: {rails}")
        print(f"Plaintext: {plaintext}\n")

        draw_rails(plaintext, rails)

        print()


if __name__ == "__main__":
    main()
