with open("8.txt") as f:
    ciphers = f.read().splitlines()

for cipher in ciphers:
    chunks = []
    chunk_len = 16
    for i in range(0, len(cipher), chunk_len):
        chunks.append(cipher[i:i + chunk_len])
    chunks = sorted(chunks)

    matches = 0


    for ci in range(len(chunks)):
        if chunks[ci] in chunks[ci + 1:]:
            matches += 1

    if matches > 0:
        for chunk in chunks:
            print(chunk)

    