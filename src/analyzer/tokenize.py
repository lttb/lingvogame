import re


def tokenize(text):
    return [word.lower() for word in re.split(r'(?!\b-\b)\W', text) if word]
