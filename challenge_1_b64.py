

# Convert hexadecimal string to base 64 string
def hex_to_b64(hexstr):
    hextable = "0123456789abcdef"

    pad = len(hexstr) % 3
    if pad == 1:
        hexstr = "00" + hexstr
    elif pad == 2:
        hexstr = "0" + hexstr


    b64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    b64str = ""

    for i in range(0, len(hexstr), 3):
        n = 0
        mul = 1
        for j in range(2, -1, -1):
            single_hex = hextable.index(hexstr[i + j])
            n += single_hex*mul
            mul = mul << 4
        # now that we have 3 hex characters together, that is 2 base64 characters
        char2 = b64_table[n % 64]
        n = n // 64
        char1 = b64_table[n % 64] 
        b64str += char1 + char2
    return b64str


def test_hex_to_b64():
    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    ans = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    val = hex_to_b64(hex)
    assert val == ans, f"{val=}"

