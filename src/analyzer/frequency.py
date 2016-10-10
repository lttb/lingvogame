import functools
from .tokenize import tokenize


def build_list(arr):
    frequencyStep = 1 / len(arr)

    return functools.reduce(lambda acc, word: {
        ** acc,
        ** {word: acc.get(word, 0) + frequencyStep}
    }, arr, {})


def build_list_limited(arr, min_k=0, max_k=1):
    freq_list = build_list(arr)

    m = max(freq_list.values())
    min_freq = min_k * m
    max_freq = max_k * m

    return {k: v for k, v in freq_list.items() if min_freq <= v <= max_freq}
