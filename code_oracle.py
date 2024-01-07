import random
from Cryptodome.Cipher import AES
from cbc_mode import encrypt_cbc


def pad(byte_arr, block_len):
    assert type(byte_arr) is bytes
    remainder = len(byte_arr) % block_len
    pad_len = block_len - remainder
    
    padding = bytes([pad_len]*pad_len)
    return byte_arr + padding

def unpad(padded_text):
    pad_len = padded_text[-1]
    return padded_text[:-pad_len]

def random_bytes(bytes_size):
    arr = []
    for i in range(bytes_size):
        arr.append(random.randint(0, 255))
    arr = bytes(arr)
    return arr

def extend_text(text_bytes):
    assert type(text_bytes) is bytes
    before_text_len = random.randint(5, 10)
    after_text_len = random.randint(5, 10)
    before_text = random_bytes(before_text_len)
    after_text = random_bytes(after_text_len)
    return before_text + text_bytes + after_text

def encrypt_ECB_with_key(text_bytes, key):
    padded = pad(text_bytes, 16)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded)
    return ciphertext

def decrypt_ECB_with_key(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.decrypt(ciphertext)
    ciphertext = unpad(ciphertext)
    return ciphertext

def encrypt_ECB_randomized(text_bytes):
    assert type(text_bytes) is bytes
    key = random_bytes(16)
    extended_text = extend_text(text_bytes)
    padded = pad(extended_text, 16)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded)
    return ciphertext

def encrypt_CBC_randomized(text_bytes):
    assert type(text_bytes) == bytes
    key = random_bytes(16)
    extended_text = extend_text(text_bytes)

    iv = random_bytes(16)

    ciphertext = encrypt_cbc(extended_text, iv, key)

    return ciphertext

def encryption_oracle(text_bytes):
    if random.random() > 0.5:
        return encrypt_ECB_randomized(text_bytes), "ECB"
    else:
        return encrypt_CBC_randomized(text_bytes), "CBC"
    

def is_ECB(ciphertext):
    chunks = []
    chunk_len = 16
    for i in range(0, len(ciphertext), chunk_len):
        chunks.append(ciphertext[i:i + chunk_len])
    chunks = sorted(chunks)

    matches = 0


    for ci in range(len(chunks)):
        if chunks[ci] in chunks[ci + 1:]:
            matches += 1

    if matches > 0:
        return "ECB"
    else: 
        return "CBC"

if __name__ == "__main__":

    with open("sometext.txt") as f:
        text = f.read()

    text_bytes = text.encode('utf-8')

    ciphertext, ans = encryption_oracle(text_bytes)
    print("We guessed", is_ECB(ciphertext))
    print("Answer: ", ans)