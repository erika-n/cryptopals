
with open("letter_frequency.csv") as f:
    freqs = f.readlines()

english_freqs = {line.split(",")[0]:float(line.strip().split(",")[1]) for line in freqs[1:]}

cipher = 0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736


def to_ascii(hex_num):
    ascii = ""
    while hex_num > 0:
 
        ascii += chr(hex_num % 2**8)

        hex_num = hex_num >> 8
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

for i in range(26*2 + 6):
    letter = ord("A") + i
    letters = [letter] * 34

    key = list_to_num(letters, 8)

    text = to_ascii(cipher^key)
    score = letter_freq_score(text)
    output.append((chr(letter), text, score))

output = sorted(output, key=lambda x: x[2], reverse=True)
for o in output[:5]:
    print(o)





