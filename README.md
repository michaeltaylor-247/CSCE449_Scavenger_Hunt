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

Because the same substitution mapping is used for the entire message, repeated plaintext characters remain repeated in the ciphertext. This means patterns, letter frequencies, and repeated character sequences can help when attempting to break the cipher. Because there are only 26 possible shift values, it is quite easy to brute-force a Ceasar Cipher. 


### Phase 2: Monoalphabetic Substitution Cipher (@OCSB)

This clue is encrypted via a monoalphabetic substitution cipher. A monoalphabetic substitution cipher is a type of *substitution* cipher where each plaintext character is consistently mapped to exactly one ciphertext character.

Unlike a Caesar cipher, the mapping does not follow a fixed shift. Instead, the alphabet may be mapped in any arbitrary order, as long as each plaintext character maps to a unique ciphertext character.

**Example Monoalphabetic Substitution Cipher**:
The following showcases one possible random substitution mapping.

| Plaintext | Ciphertext |
| --------- | ---------- |
| a         | q          |
| b         | w          |
| c         | e          |
| d         | r          |
| e         | t          |
| f         | y          |
| g         | u          |
| h         | i          |
| i         | o          |
| j         | p          |
| k         | a          |
| l         | s          |
| m         | d          |
| n         | f          |
| o         | g          |
| p         | h          |
| q         | j          |
| r         | k          |
| s         | l          |
| t         | z          |
| u         | x          |
| v         | c          |
| w         | v          |
| x         | b          |
| y         | n          |
| z         | m          |

For example:

```text
plaintext:  hello
ciphertext: itssg
```

Because the same substitution mapping is used for the entire message, repeated plaintext characters remain repeated in the ciphertext. This means patterns, letter frequencies, and repeated character sequences can help when attempting to break the cipher. However brute-forcing is more difficult as there are $26!$ possible mappings.

### Phase 3: Rail Fence Cipher (@ECRB)

This clue is encrypted via a Rail Fence cipher. A Rail Fence cipher is a type of *transposition* cipher. Unlike substitution ciphers, the actual characters are not changed. Instead, their positions are rearranged.

The plaintext is written across a fixed number of "rails" in a repeating zig-zag pattern. The ciphertext is then produced by reading each rail from left to right, starting from the top rail and moving downward.

**Example Rail Fence Cipher**:
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

