import functools
from .tokenize import tokenize


def frequency(arr):
    result = {}

    if not len(arr):
        return result

    frequencyStep = 1 / len(arr)

    for word in arr:
        result[word] = result.get(word, 0) + frequencyStep

    return result


def frequencyLimited(arr, minK=0, maxK=1):
    freqList = frequency(arr)

    m = max(freqList.values())
    minFreq = minK * m
    maxFreq = maxK * m

    return {k: v for k, v in freqList.items() if minFreq <= v <= maxFreq}
