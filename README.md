# CSCE449_Scavenger_Hunt
Assignment 1 for CSCE449 - Applied Cryptography


---
# Instructions

### Phase 1: Ceasar Cipher (@Albatross Hall)
This clue is encrypted via a ceasar cypher. A ceasar cypher is a type of *substitution* cypher -- each character has been remapped to another -- where each character maps to a new one via some fixed shift value. 

**Example Ceasar Cypher**:
The following showcases a potential ceasar cypher mapping table. This specific example uses a shift of +3. 

| Plaintext | Numeric Value | Shift | Ciphertext |
| --------- | ------------: | ----: | ---------- |
| a         |             0 |    +3 | d          |
| b         |             1 |    +3 | e          |
| c         |             2 |    +3 | f          |
| d         |             3 |    +3 | g          |
| e         |             4 |    +3 | h          |
| f         |             5 |    +3 | i          |
| g         |             6 |    +3 | j          |
| h         |             7 |    +3 | k          |
| i         |             8 |    +3 | l          |
| j         |             9 |    +3 | m          |
| k         |            10 |    +3 | n          |
| l         |            11 |    +3 | o          |
| m         |            12 |    +3 | p          |
| n         |            13 |    +3 | q          |
| o         |            14 |    +3 | r          |
| p         |            15 |    +3 | s          |
| q         |            16 |    +3 | t          |
| r         |            17 |    +3 | u          |
| s         |            18 |    +3 | v          |
| t         |            19 |    +3 | w          |
| u         |            20 |    +3 | x          |
| v         |            21 |    +3 | y          |
| w         |            22 |    +3 | z          |
| x         |            23 |    +3 | a          |
| y         |            24 |    +3 | b          |
| z         |            25 |    +3 | c          |


### Phase 2: Atbash Cypher (@OCSB)

This clue is encrypted via an Atbash cypher. An Atbash cypher is another type of *substitution* cypher, but unlike a Caesar cypher, it does not use a shift value. Instead, each character is mapped to its corresponding character from the opposite end of the alphabet.

In other words, `a` maps to `z`, `b` maps to `y`, `c` maps to `x`, and so on.

**Example Atbash Cypher**:
The following showcases the complete Atbash mapping table.

| Plaintext | Ciphertext |
| --------- | ---------- |
| a         | z          |
| b         | y          |
| c         | x          |
| d         | w          |
| e         | v          |
| f         | u          |
| g         | t          |
| h         | s          |
| i         | r          |
| j         | q          |
| k         | p          |
| l         | o          |
| m         | n          |
| n         | m          |
| o         | l          |
| p         | k          |
| q         | j          |
| r         | i          |
| s         | h          |
| t         | g          |
| u         | f          |
| v         | e          |
| w         | d          |
| x         | c          |
| y         | b          |
| z         | a          |

For example:

```text
plaintext:  hello
ciphertext: svool
```

One useful property of the Atbash cypher is that encryption and decryption use the exact same mapping. Applying Atbash a second time restores the original plaintext.

### Phase 3: Rail Fence Cypher (@ECRB)

This clue is encrypted via a Rail Fence cypher. A Rail Fence cypher is a type of *transposition* cypher. Unlike substitution cyphers, the actual characters are not changed. Instead, their positions are rearranged.

The plaintext is written across a fixed number of "rails" in a repeating zig-zag pattern. The ciphertext is then produced by reading each rail from left to right, starting from the top rail and moving downward.

**Example Rail Fence Cypher**:
The following example uses the plaintext `helloworld` and 3 rails.

```text
Rail 1: h . . . o . . . l .
Rail 2: . e . l . w . r . d
Rail 3: . . l . . . o . . .
```

Reading each row from top to bottom gives:

```text
Rail 1: hol
Rail 2: elwrd
Rail 3: lo
```

The resulting ciphertext is:

```text
ciphertext: holelwrdlo
```

To decrypt the message, the receiver must know the number of rails. They can then reconstruct the zig-zag pattern, determine how many characters belong in each rail, place the ciphertext characters back into those positions, and finally follow the zig-zag path to recover the original plaintext.

