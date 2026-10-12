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






