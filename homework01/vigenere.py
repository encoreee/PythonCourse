from itertools import cycle

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    alp = 'abcdefghijklmnopqrstuvwxyz'
    alpU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    f = lambda arg: alp[(alp.index(arg[0]) + alp.index(arg[1]) % 26) % 26]
    fu = lambda arg: alpU[(alpU.index(arg[0]) + alpU.index(arg[1]) % 26) % 26]

    if plaintext[0].isupper():
        ciphertext = ''.join(map(fu, zip(plaintext, cycle(keyword))))
    else:
        ciphertext = ''.join(map(f, zip(plaintext, cycle(keyword))))
    return ciphertext




def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    alp = 'abcdefghijklmnopqrstuvwxyz'
    alpU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    f = lambda arg: alp[alp.index(arg[0]) - alp.index(arg[1]) % 26]
    fu = lambda arg: alpU[alpU.index(arg[0]) - alpU.index(arg[1]) % 26]

    if ciphertext[0].isupper():
        plaintext = ''.join(map(fu, zip(ciphertext, cycle(keyword))))
    else:
        plaintext = ''.join(map(f, zip(ciphertext, cycle(keyword))))
    return plaintext



