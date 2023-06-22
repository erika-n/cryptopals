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

def test_unpad():
    plaintext = b'here we go a wassailing'
    padded_plaintext = pad(plaintext, 16)
    unpadded_plaintext = unpad(padded_plaintext)
    assert plaintext == unpadded_plaintext

def test_encrypt_cbc():
    plaintext = b'YELLOW SUBMARINEyellow submar'
    initialization_vector = bytes([ord('0')]*16)
    key = b'YELLOW SUBMARINE'
    ciphertext = encrypt_cbc(plaintext, initialization_vector, key)
    assert len(ciphertext) == 32

def test_encrypt_decrypt_cbc():
    plaintext = b'a fine day in the woods'
    initialization_vector = bytes([ord('0')]*16)
    key = b'purple taxi cabs'
    ciphertext = encrypt_cbc(plaintext, initialization_vector, key)
    proposed_plaintext = decrypt_cbc(ciphertext, initialization_vector, key)
    print(proposed_plaintext)
    print(len(proposed_plaintext))
    assert plaintext == proposed_plaintext