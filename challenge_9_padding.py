
def pad(block, pad_len, pad_with=0x04):
    n_pad = pad_len - len(block)
    padding = bytes([pad_with]*n_pad)
    return block + padding


block = b"YELLOW SUBMARINE"
print(pad(block, 20))
