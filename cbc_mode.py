
from xor_encryption import bytewise_xor
from Cryptodome.Cipher import AES

def pad(text, block_len):
    remainder = len(text) % block_len
    pad_len = block_len - remainder
    
    padding = bytes([pad_len]*pad_len)
    return text + padding

def unpad(padded_text):
    pad_len = padded_text[-1]
    return padded_text[:-pad_len]


def encrypt_one_block(plaintext_block, salt, key):

    assert len(plaintext_block) == 16
    assert len(salt) == 16
    assert len(key) == 16


    to_encrypt = bytewise_xor(plaintext_block, salt)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext_block = cipher.encrypt(to_encrypt)
    return ciphertext_block

def decrypt_one_block(ciphertext_block, salt, key):
    assert len(ciphertext_block) == 16
    assert len(salt) == 16
    assert len(key) == 16
    
    cipher = AES.new(key, AES.MODE_ECB)
    deciphered = cipher.decrypt(ciphertext_block)
    plaintext = bytewise_xor(deciphered, salt)
    return plaintext

def encrypt_cbc(plaintext, initialization_vector, key):
    assert len(initialization_vector) == 16
    assert len(key) == 16

    plaintext = pad(plaintext, 16)
    prev_block = initialization_vector
    ciphertext = bytes([])
    for i in range(0, len(plaintext), 16):
        crypt_block = encrypt_one_block(plaintext[i:i + 16], prev_block, key)
        ciphertext += crypt_block
        prev_block = crypt_block
    return ciphertext

def decrypt_cbc(ciphertext, initialization_vector, key):
    assert len(ciphertext) % 16 == 0
    assert len(initialization_vector) == 16
    assert len(key) == 16

    plaintext = bytes([])
    prev_block = initialization_vector

    for i in range(0, len(ciphertext), 16):
        decrypt_block = decrypt_one_block(ciphertext[i:i + 16], prev_block, key)
        plaintext += decrypt_block
        prev_block = ciphertext[i:i + 16]
    return unpad(plaintext)


if __name__ == "__main__":
    plaintext_block = b'yellow submarine'
    key = b'YELLOW SUBMARINE'
    salt = bytes([0]*16)    
    ciphertext = encrypt_one_block(plaintext_block, salt, key)
    print(ciphertext)
    print(len(ciphertext))