

with open("letter_frequency.csv") as f:
    freqs = f.readlines()

english_freqs = {line.split(",")[0]:float(line.strip().split(",")[1]) for line in freqs[1:]}


with open("challenge_4_encrypted.txt") as f:
    ciphers = f.read().splitlines() 

def to_ascii(num):
    ascii = ""
    while num > 0:
 
        ascii += chr(num % 2**8)

        num = num >> 8
    return ascii[::-1]

def list_to_num(lst, bits):
    num = 0
    mul = 1
    for item in lst[::-1]:

        num += item*mul
        mul = mul << bits

    return num

def letter_freq_score(text):


    score = 0
    text = text.lower()
    my_freqs = {}
    for character in text:
        my_freqs[character] = my_freqs.get(character, 0) + 1

    for key in my_freqs.keys():
        my_freqs[key] /= len(text)

    for key in my_freqs.keys():
        if key in english_freqs:
            score += my_freqs[key]*english_freqs[key]

    return score

output = []
for cipher in ciphers:
    n_chars = len(cipher)//2
    n_cipher = int(cipher, 16)
 
    for i in range(256):
        letter = i
        letters = [letter] * n_chars

        key = list_to_num(letters, 8)

        text = to_ascii(n_cipher^key)
        score = letter_freq_score(text)
        output.append((cipher, chr(letter), text, score))

output = sorted(output, key=lambda x: x[3], reverse=True)
for o in output[:5]:
    print(o)

# Answer: 
# ('7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f', '5', 'Now that the party is jumping\n', 0.066741)




