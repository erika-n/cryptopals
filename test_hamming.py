from hamming_distance import hamming_distance
# Test the hamming distance function, should return 37

def test_hamming():
    h1 = b"this is a test"
    h2 = b"wokka wokka!!!"
    hd = hamming_distance(h1, h2)
    assert hd == 37 , f"{hd=}"