from code_oracle import encrypt_ECB_with_key, random_bytes, is_ECB
from b64 import b64_file_to_bytes
universal_key = random_bytes(16)
def decode_one_byte(target_text_bytes, block_size):
    short_text = "A"*(block_size - 1)
    short_text_bytes = short_text.encode('ascii')
    cipher_text_short = encrypt_ECB_with_key(short_text_bytes + target_text_bytes, universal_key)
    for i in range(256):
        cipher_text_test = encrypt_ECB_with_key(short_text_bytes + bytes([i]), universal_key)
        if cipher_text_test[:block_size] == cipher_text_short[:block_size]:
            return i
    return -1    

if __name__ == "__main__":


    target_text_bytes = b64_file_to_bytes('12.txt')

    text = "A"
    text_bytes = text.encode('ascii')
    prev_block_test = encrypt_ECB_with_key(text_bytes, universal_key)

    block_size = -1
    for i in range(2, 256):
        text = "A"*i
        text_bytes = text.encode('ascii')
        new_block_test = encrypt_ECB_with_key(text_bytes, universal_key)
        if new_block_test[0] == prev_block_test[0]:
            block_size = i - 1
            break
        prev_block_test = new_block_test
    print("block size:", block_size)

    print(is_ECB(encrypt_ECB_with_key(text_bytes + text_bytes, universal_key)))

    decoded = []
    for i in range(len(target_text_bytes)):
        decoded.append(decode_one_byte(target_text_bytes[i:], block_size))

    decoded = bytes(decoded)
    decoded = decoded.decode('ascii')
    print(decoded)
        





