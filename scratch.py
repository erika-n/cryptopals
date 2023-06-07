with open("sometext.txt") as f:
    text = f.read()
text = text.upper()
letter_freqs = {}
for letter in text:
    letter_freqs[letter] = letter_freqs.get(letter, 0) + 1

letter_freqs = sorted(letter_freqs.items(), key=lambda x:x[1], reverse=True)

print(letter_freqs)

