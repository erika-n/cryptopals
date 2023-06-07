from xor_encryption import *

def test_bytewise_xor():
    bytes1 = bytes([255, 0])
    bytes2 = bytes([0, 255])
    b_xor = bytewise_xor(bytes1, bytes2)
    assert b_xor == bytes([255, 255]), f"{b_xor=}, should be {bytes[255, 255]}"


def test_repeating_key():
    key = "ABC"
    length = 8
    ans = b"ABCABCAB"
    assert get_repeating_key_bytes(key, length) == ans, f"{ans=}"


def test_encrypt_decrypt():
    plaintext = "Hello out there earthlings"
    key = "MARS"
    cipher_bytes = encrypt_repeating_key(plaintext, key)
    outtext = decrypt_repeating_key(cipher_bytes, key)
    assert outtext == plaintext, f"{outtext=}, should be {plaintext}"

def test_break_single_letter():
    plaintext = "The world is a giant squid"
    key = "q"
    cipher_bytes = encrypt_repeating_key(plaintext, key)
    proposed_key = break_single_letter_key(cipher_bytes)

    assert key == proposed_key, f"{proposed_key=}, should be {key}"

def test_break_key_len():
    with open("sometext.txt") as f:
        plaintext = f.read()

    key = "this is a pretty long pass phrase(*(*N))"
    cipher_bytes = encrypt_repeating_key(plaintext, key)
    key_lens = break_key_len(cipher_bytes, max_len=50, top_n=3)
    print(key_lens)
    assert len(key) in key_lens, f"{key_lens=}, should contain {len(key)}"


def test_break_repeating_key():
    with open("sometext.txt") as f:
        plaintext = f.read()

    key = "28hvw78c997&"
    cipher = encrypt_repeating_key(plaintext, key)
    proposed_key = break_repeating_key(cipher)
    print(f"{len(proposed_key)=}")
    assert key == proposed_key, f"{proposed_key=}, should be {key}"