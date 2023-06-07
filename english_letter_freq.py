

def lf_score(text):
    letter_freqs = {
        "e":0.12702,
        "t":0.09056,
        "a":0.08167,
        "o":0.07507,
        "i":0.06966,
        "n":0.06749,
        "s":0.06327,
        "h":0.06094,
        "r":0.05987,
        "d":0.04253,
        "l":0.04025,
        "c":0.02782,
        "u":0.02758,
        "m":0.02406,
        "w":0.0236,
        "f":0.02228,
        "g":0.02015,
        "y":0.01974,
        "p":0.01929,
        "b":0.01492,
        "v":0.00978,
        "k":0.00772,
        "j":0.00153,
        "x":0.0015,
        "q":0.00095,
        "z":0.00074,
        " ":0.12,
        "'":0.012,
        ",":0.012,
        "\n":0.012
    }
    text = text.lower()
    my_letter_freqs = {}
    score = 0
    for letter in text:
        if letter in letter_freqs:
            my_letter_freqs[letter] = my_letter_freqs.get(letter, 0) + 1
        else:
            score += 10



    for letter in letter_freqs.keys():

        expected_n = letter_freqs[letter]*len(text)
        
        if letter in my_letter_freqs:
            score +=  (expected_n - my_letter_freqs[letter])**2/expected_n
        else:
            score += 1.0
 
    return score


if __name__ == "__main__":
    print(lf_score("hello there this is a test of some text"))
    print(lf_score("evkjnef8u98uy3423 5mcn[][3nnk,m|]"))
