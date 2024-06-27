import random
from string import ascii_letters, digits, ascii_lowercase


def create_random_secret(passphrase_length):
    alphanum = ascii_letters + digits
    secret = ''.join([random.choice(alphanum) for i in range(passphrase_length)])
    print(secret)
    return secret
