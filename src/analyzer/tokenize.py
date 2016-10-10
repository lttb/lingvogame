import re


def tokenize(text):
    return [word for word in re.split(r'\W', text) if word]
