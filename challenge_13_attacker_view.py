from challenge_13_ecb_cut_paste import encrypted_profile_for, is_admin
from code_oracle import random_bytes, pad

if __name__ == "__main__":
    UNKNOWN_KEY = random_bytes(16)


    # want to create profile string with blocks:
    # [email=filler1][admin padded][filler2][&uid=blah&role=][user padded]

    # by setting email to:
    # filler1+admin_padded+filler2

    # what we want for attacked_profile is blocks:
    # [email=filler1][admin padded][filler2][&uid=blah&role=][admin padded]

    # filler1 has length 16 - len('email =') = 10
    # filler2 is tuned to make "user" be in its own block

    filler1 = b"0123456789"
    filler2 = "01234567890123user"
    padded_admin = pad(b"email=" + filler1 + b"admin", 16)
    padded_admin = padded_admin[6:]

    encrypted_profile = encrypted_profile_for(padded_admin.decode('utf-8') + filler2, UNKNOWN_KEY)

    print(is_admin(encrypted_profile, UNKNOWN_KEY))

    attacked_profile = encrypted_profile[:-16]

    attacked_profile += encrypted_profile[16:32]

    print(is_admin(attacked_profile, UNKNOWN_KEY))




