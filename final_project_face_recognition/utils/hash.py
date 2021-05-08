from typing import AnyStr
from hashlib import sha256
import os


def get_salt() -> bytes:
    # You may consider to add in .env to secure your salt code or travis
    SALT = "3f87b3a5b7e48ba408964366a7194789249d4ed33b962a9e5d76c5d6122237bc"

    # convert hexadecimal salt to bytes equivalent and return those bytes
    return bytes.fromhex(SALT)


## May consider to add salt in .env file
    # SALT = os.environ["SALT_HERE_ENV"]
    #
    # # convert hexadecimal salt to bytes equivalent and return those bytes
    # return bytes.fromhex(SALT)


def hash_str(some_val: AnyStr, salt: AnyStr = ""):
    """Converts strings to hash digest

    :param some_val: thing to hash
    :param salt: Add randomness to the hashing
    :return: hash digest of input
    """
    # create a SHA-256 hash object
    h = sha256()

    # lambda function used to ensure input vars to the hash object are bytes
    encode = lambda x: x.encode() if isinstance(x, str) else x

    # feed hash object with salt bytes
    h.update(encode(salt))

    # feed hash object with bytes representation of the input string
    h.update(encode(some_val))

    # return digest of the data fed into the hash object
    return h.digest()


def get_user_id(username: str) -> str:
    """Converts username string to hash digest

    :param username: string to hash
    :return: first 8 chars in hex format of hash digest of input
    """
    # retrieve salt from environment variables
    salt = get_salt()
    # compute and return hash digest of input
    return hash_str(username.lower(), salt=salt).hex()[:8]
