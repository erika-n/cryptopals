from cbc_mode import *

def test_encrypt_one_block():
    plaintext_block = b'yellow submarine'
    key = b'YELLOW SUBMARINE'
    salt = bytes([0]*16)    
    ciphertext = encrypt_one_block(plaintext_block, salt, key)
    assert len(ciphertext) == 16

    
def test_encrypt_decrypt_one_block():
    plaintext_block = b'yellow submarine'
    key = b'YELLOW SUBMARINE'
    salt = bytes([0]*16)    
    ciphertext_block = encrypt_one_block(plaintext_block, salt, key)
    plaintext_decrypted = decrypt_one_block(ciphertext_block, salt, key)
    assert plaintext_decrypted == plaintext_block


def test_pad():
    plaintext = b'yellow submari'
    padded_plaintext = pad(plaintext, 16)
    assert padded_plaintext == b'yellow submari\02\02' 
    plaintext = b'YELLOW SUBMARINEyellow submar'
    padded_plaintext = pad(plaintext, 16)
    assert padded_plaintext == b'YELLOW SUBMARINEyellow submar\03\03\03'