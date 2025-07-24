# TODO: Implement utility functions here
# Consider functions for:
# - Generating short codes
# - Validating URLs
# - Any other helper functions you need
import hashlib
from urllib.parse import  urlparse

BaseChar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
len_base = len(BaseChar)

#encoding to base 62 format
def base_char_encode(id):
    if id == 0:
        return BaseChar[0]
    encode= ""
    while id > 0:
        id, rem = divmod(id, len_base)
        encode = BaseChar[rem]+ encode

    return encode

def short_url(long_url, length = 6):
    try:
        #hashing the long url given by user and converting it to integer form
        hashed_url =int( hashlib.sha256(long_url.encode()).hexdigest(),16)
        #encoding to BaseChar
        base_62_str = base_char_encode(hashed_url)

        return base_62_str[:length]
    except :
        raise ValueError("url shortening failed")


def validate_url(long_url:str)->bool:
    try:
        result = urlparse(long_url)
        if result.scheme and result.netloc:
            return True
    except:
        return False









