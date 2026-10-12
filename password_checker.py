import math

import re 
import csv
from collections import Counter

# open the common passwords file 
with open('common_passwords.csv' , mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data_list = list(reader)

# character pool sizes
LOWER = 26
UPPER = 26
DIGITS = 10
SYMBOLS = 32
SPACE = 1


# load common passwords dataset
def load_common_passwords ():
    try:
        with open('common_passwords.csv' , mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data_list = list(reader)
            return data_list
    except  FileNotFoundError:
        return []

# Return which character classes appear in the password
def detect_character(password: str)-> dict:
    return {
        "lower": bool(re.search(r"[a-z]", password)),
        "upper": bool(re.search(r"[A-Z]", password)),
        "digit": bool(re.search(r"[0-9]", password)),
        "symbol": bool(re.search(r"[A-Za-Z0-9]", password)),
        "space": " " in password,
    }


# computer pool size function
def pool_size(charsets: dict) -> int:
    n = 0
    if charsets['lower']: n+=LOWER
    if charsets['upper']: n+=UPPER
    if charsets['digit']: n+=DIGITS
    if charsets['symbol']: n+=SYMBOLS
    if charsets['space']: n+= SPACE

    return n

