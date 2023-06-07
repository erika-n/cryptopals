
from b64 import b64_to_bytes
from xor_encryption import break_repeating_key, decrypt_repeating_key

if __name__ == "__main__":


    with open("6.txt") as f:
        cipher_b64 = f.read().splitlines()
    
    cipher_b64 = "".join(cipher_b64)

    cipher_bytes = b64_to_bytes(cipher_b64)

    proposed_key = break_repeating_key(cipher_bytes)

    print(f"{proposed_key=}")

    proposed_plaintext = decrypt_repeating_key(cipher_bytes, proposed_key)

    print(proposed_plaintext)





   







