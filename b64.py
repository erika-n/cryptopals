import base64

def b64_to_bytes(b64_str):
    ascii_bytes = b64_str.encode("ascii")
    return base64.b64decode(ascii_bytes)


def bytes_to_b64(bytearr):
    return base64.b64encode(bytearr).decode("ascii")


if __name__ == "__main__":
    b = b64_to_bytes("BAAA")
    print(b)
