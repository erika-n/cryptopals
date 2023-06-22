import base64

def b64_to_bytes(b64_str):
    ascii_bytes = b64_str.encode("ascii")
    return base64.b64decode(ascii_bytes)

def b64_file_to_bytes(file):
    with open(file) as f:
        lines = f.read().splitlines()

    b64_str = "".join(lines)
    return b64_to_bytes(b64_str)

def bytes_to_b64(bytearr):
    return base64.b64encode(bytearr).decode("ascii")


if __name__ == "__main__":
    b = b64_to_bytes("BAAA")
    print(b)
