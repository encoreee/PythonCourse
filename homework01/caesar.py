import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    n = '.[]{}()=-.,;:"1234567890~!`@#$%^&*<>?|=+_- '
    for c in plaintext:
        if c.isupper():
            if c in n:
                ciphertext += c
            else:
                ciphertext += alphabetU[(alphabetU.index(c) + shift) % len(alphabetU)]
        else:
            if c in n:
                ciphertext += c
            else:
                ciphertext += alphabet[(alphabet.index(c) + shift) % len(alphabet)]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    n = '.[]{}()=-.,;:"1234567890~!`@#$%^&*<>?|=+_- '
    for c in ciphertext:
        if c.isupper():
            if c in n:
                plaintext += c
            else:
                plaintext += alphabetU[(alphabetU.index(c) - shift) % len(alphabetU)]
        else:
            if c in n:
                plaintext += c
            else:
                plaintext += alphabet[(alphabet.index(c) - shift) % len(alphabet)]

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
