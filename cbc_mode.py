
from xor_encryption import bytewise_xor
from Cryptodome.Cipher import AES

def pad(text, block_len):
    remainder = len(text) % block_len
    pad_len = block_len - remainder
    
    padding = bytes([pad_len]*pad_len)
    return text + padding


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

if __name__ == "__main__":
    plaintext_block = b'yellow submarine'
    key = b'YELLOW SUBMARINE'
    salt = bytes([0]*16)    
    ciphertext = encrypt_one_block(plaintext_block, salt, key)
    print(ciphertext)
    print(len(ciphertext))