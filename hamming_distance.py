


def hamming_distance(bytes1, bytes2):

    assert isinstance(bytes1, bytes)
    assert isinstance(bytes2, bytes)
    assert len(bytes1) == len(bytes2)
    ans = 0

    for b1, b2 in zip(bytes1, bytes2):
        xored = int(b1) ^ int(b2)
        blist = list(bin(xored))
        blist = blist[2:]
        ans += sum(map(int, blist))
    return ans
