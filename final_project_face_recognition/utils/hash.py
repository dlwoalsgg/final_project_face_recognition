from typing import Union
import hashlib
from canvasapi import Canvas
from environs import Env
import base64



def get_csci_salt() -> bytes:
    env = Env()
    env.read_env()
    # a string of hexadecimal values
    saltHexStr = bytes.fromhex(env('CSCI_SALT'))
    """Returns the appropriate salt for CSCI E-29

    :return: bytes representation of the CSCI salt
    """
    return saltHexStr
    # Hint: use os.environment and bytes.fromhex
    # raise NotImplementedError()

def get_csci_pepper() -> bytes:
    """Returns the appropriate pepper for CSCI E-29

    This is similar to the salt, but defined as the UUID of the Canvas course,
    available from the Canvas API.

    This value should never be recorded or printed.

    :return: bytes representation of the pepper
    """
    # env instance to retrive canvas object
    env = Env()
    env.read_env()
    # Load canvas objects
    canvas = Canvas(env('CANVAS_URL'), env('CANVAS_TOKEN'))

    course = canvas.get_course(env('CANVAS_COURSE_ID'))
    # receive uuid from coourse object
    uuidStr = course.uuid
    # decode a uuid string to bytes
    uuidHex = base64.b64decode(uuidStr)
    return uuidHex
    #     # Hint: Use base64.b64decode to decode a UUID string to bytes
    # raise NotImplementedError()


def hash_str(some_val: Union[str, bytes], salt: Union[str, bytes] = "") -> bytes:
    """
    Converts strings to hash digest

    See: https://en.wikipedia.org/wiki/Salt_(cryptography)

    :param some_val: thing to hash, can be str or bytes
    :param salt: Add randomness to the hashing, can be str or bytes
    :return: sha256 hash digest of some_val with salt, type bytes
    """
    some_valHex = some_val
    saltHex = salt
    # verify whether some_val is str or hex
    if isinstance(some_val, str):
        some_valHex = some_val.encode()
    # verify whether salt is str or hex
    if isinstance(salt, str):
        saltHex = salt.encode()
    # concat saltHex and some val hex to return
    concatHex = hashlib.sha256(saltHex + some_valHex).digest()
    return concatHex


# return type last 8 digit str
def get_user_id(username: str) -> str:
    salt = get_csci_salt() + get_csci_pepper()
    return hash_str(username.lower(), salt=salt).hex()[:8]
