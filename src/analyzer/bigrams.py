import re
from operator import itemgetter
from .frequency import build_list


def build(text, word):
    return re.findall(r'(?=(\b\w+\s%(w)s|%(w)s\s\w+))' % {'w': word}, text)


def frequencyList(text, word, count=3):
    bigrams = build(text, word)

    freq_list = build_list(bigrams)

    return [*map(
        lambda pair: pair[0],
        sorted(freq_list.items(), key=itemgetter(1))[-count:]
    )]
