import re
import requests

PATTERN = (r'\b(?:(?:[0-9A-F]{2}[:]){5}(?:[0-9A-F]){2})\b|'
           r'\b(?:(?:[0-9A-F]{2}[-]){5}(?:[0-9A-F]){2})\b')
LINK = 'https://en.wikipedia.org/wiki/MAC_address'


def mac_return_valid(mac):
    return re.findall(PATTERN, mac, flags=re.I)

def mac_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return max_return_valid(file.read())
    return None
