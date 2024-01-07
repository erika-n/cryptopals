import random
from Cryptodome.Cipher import AES
from code_oracle import random_bytes, encrypt_ECB_with_key, decrypt_ECB_with_key



def kv_parse(kv_str):
    kvs = kv_str.split('&')
    parsed = {}
    for kv in kvs:
        k, v  = kv.split('=')
        parsed[k] = v
    return parsed


def profile_for(email):

    profile_info = {
        'email': email,
        'uid': str(random.randint(101, 999)),
        'role': 'user'
    }

    if '&' in email or '=' in email:
        raise Exception

    profile_str = ""
    for i, (key, val) in enumerate(profile_info.items()):
        profile_str += key + '=' + val + '&'

    profile_str = profile_str[:-1]

    return profile_str

def encrypted_profile_for(email, key):
    profile_str = profile_for(email)

    ciphertext = encrypt_ECB_with_key(profile_str.encode('utf-8'), key)
    return ciphertext

def decrypt_profile_info(profile_info, key):
    plaintext = decrypt_ECB_with_key(profile_info, key)
    return plaintext.decode('utf-8')

def is_admin(encrypted_profile, key):
    profile_str = decrypt_profile_info(encrypted_profile, key)

    profile = kv_parse(profile_str)

    if profile['role'] == 'admin':
        return True
    return False


if __name__ == "__main__":

    key = random_bytes(16)

    parsed = kv_parse('foo=bar&baz=qux&zap=zazzle')
    print(parsed)

    my_profile = profile_for("test@gmail.com")
    print(my_profile)

    my_profile_encrypted = encrypted_profile_for("test@gmail.com", key)
    print(my_profile_encrypted)

    my_profile_decrypted = decrypt_profile_info(my_profile_encrypted, key)
    print(my_profile_decrypted)

    print(is_admin(my_profile_encrypted, key))