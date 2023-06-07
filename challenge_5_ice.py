import math
import sys

message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"



key = "ICE"

def ascii_to_num(ascii):
    num = 0
    mul = 1
    for character in ascii[::-1]:

        num += ord(character)*mul
        mul = mul << 8

    return num

def num_to_ascii(num):
    ascii = ""
    while num > 0:
 
        ascii += chr(num % 2**8)

        num = num >> 8

    return ascii[::-1]


def repeat_key(key, message_length):

    repeated_key = key * math.ceil( message_length / len(key))

    chop_off = len(repeated_key) % message_length
    if chop_off > 0:
        repeated_key = repeated_key[:-chop_off]

    return repeated_key


def encrypt_repeating_key(message, key):

    repeated_key = repeat_key(key, len(message))
    message_num = ascii_to_num(message)
    key_num = ascii_to_num(repeated_key)

    encrypted = message_num ^ key_num
    return encrypted

def byte_length(i):
    return (i.bit_length() + 7) // 8

def decrypt_repeating_key(cipher_bignum, key_ascii):
    print("byte length cipher", byte_length(cipher_bignum))
    repeated_key = repeat_key(key_ascii, byte_length(cipher_bignum))
    print("repeated key len: ", len(repeated_key))
    key_num = ascii_to_num(repeated_key)
    plain = key_num ^ cipher_bignum
    return num_to_ascii(plain)




def test_repeating_key(cipher_bignum, key_letter_ascii, key_len, key_offset ):
    cipher_text = num_to_ascii(cipher_bignum)
    test_list= list(cipher_text)[key_offset:len(cipher_text):key_len]
    test_text = "".join(test_list)
    test_bignum = ascii_to_num(test_text)
    plain_text = decrypt_repeating_key(test_bignum, key_letter_ascii)
    return plain_text

encrypted = encrypt_repeating_key(message, key)
print(hex(encrypted))

solution = 0x0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
assert(encrypted == solution)

#print(decrypt_repeating_key(encrypted, key))

test_repeating_key(encrypted, "C", 3, 1)


# repeat_key("ICE", len(message))