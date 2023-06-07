from english_letter_freq import lf_score
from hamming_distance import hamming_distance

def bytewise_xor(bytes1, bytes2):
    b_xor = []
    for b1, b2 in zip(bytes1, bytes2):
        b_xor.append(b1 ^ b2)
    return bytes(b_xor)

def get_repeating_key_bytes(key, length):
    longkey = key*(1 + length//len(key))
    return longkey[:length].encode('ascii')


def encrypt_repeating_key(plaintext, key):
    text_bytes = plaintext.encode('ascii')

    repeating_key = get_repeating_key_bytes(key, len(plaintext))

    bytes_cipher = bytewise_xor(repeating_key, text_bytes)
    return bytes_cipher

def decrypt_repeating_key(cipher_bytes, key):
    text_bytes = bytewise_xor(cipher_bytes, get_repeating_key_bytes(key, len(cipher_bytes)))
    plaintext = text_bytes.decode('ascii')
    return plaintext


def break_single_letter_key(cipher_bytes):

    scores = []
    for ascii_code in range(128):
        proposed_key = chr(ascii_code)

        test_text = decrypt_repeating_key(cipher_bytes, proposed_key)
        scores.append((proposed_key, test_text[:10], lf_score(test_text)))
    scores = sorted(scores, key=lambda x:x[2])
    return scores[0][0]


def break_key_len(cipher, max_len = 40, top_n = 5):
    scores = []
    for key_len in range(1, max_len):
 
        total_dist = 0

        for j in range(0, len(cipher) - 2*key_len, key_len):
            total_dist += hamming_distance(cipher[j:j +key_len], cipher[j + key_len:j + 2*key_len])
        n_trials = len(cipher) //key_len
        score = total_dist/n_trials
        score /= key_len
        scores.append((key_len, score))
    scores = sorted(scores, key=lambda x:x[1])

    top_scores = [scores[i][0] for i in range(top_n)]
 
    return top_scores


def break_repeating_key(cipher):
    key_lens = break_key_len(cipher, max_len=50, top_n=4)
    key_lens = sorted(key_lens)
    scores = []
    for key_len in key_lens:
        proposed_key = ""
        for offset in range(key_len):
            current_cipher = cipher[offset::key_len]
            current_key = break_single_letter_key(current_cipher)
            proposed_key += current_key
        proposed_plaintext = decrypt_repeating_key(cipher, proposed_key)
        scores.append((proposed_key, proposed_plaintext[:20], lf_score(proposed_plaintext)))

    scores = sorted(scores, key=lambda x:x[2])

    return scores[0][0]

        

