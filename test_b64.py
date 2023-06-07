from b64 import b64_to_bytes, bytes_to_b64


def test_b64_to_bytes():
    b = b64_to_bytes("BAA=")
    assert b[0] == 4, f"{b[0]=}"
    assert b[1] == 0, f"{b[1]=}"




def test_64_to_bytes_and_back():
    b64_1 = "CAA="
    bytearr = b64_to_bytes(b64_1)
    b64_2 = bytes_to_b64(bytearr)
    assert b64_1 == b64_2, f"{b64_2=}, should be {b64_1}"


