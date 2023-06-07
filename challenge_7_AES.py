from b64 import b64_to_bytes
from Cryptodome.Cipher import AES

if __name__ == "__main__":


    with open("7.txt") as f:
        cipher_b64 = f.read().splitlines()
    
    cipher_b64 = "".join(cipher_b64)

    ciphertext = b64_to_bytes(cipher_b64)
    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext.decode('ascii'))