from b64 import b64_to_bytes
from cbc_mode import decrypt_cbc

if __name__ == "__main__":


    with open("10.txt") as f:
        cipher_b64 = f.read().splitlines()
    cipher_b64 = "".join(cipher_b64)

    ciphertext = b64_to_bytes(cipher_b64)

    key = b'YELLOW SUBMARINE'
    initialization_vector = bytes([0]*16)

    plaintext = decrypt_cbc(ciphertext, initialization_vector, key)

    print(plaintext)
    