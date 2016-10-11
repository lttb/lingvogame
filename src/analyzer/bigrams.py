import re
from operator import itemgetter
from .frequency import frequency


def bigrams(text, word):
    return re.findall(
        r'(?=(\b\w+\s%(w)s\b|\b%(w)s\s\w+\b))' % {'w': word},
        text
    )


def bigramsWithFrequency(text, word, count=3):
    freqList = frequency(bigrams(text, word))

    return [* map(
        lambda pair: pair[0],
        sorted(freqList.items(), key=itemgetter(1))[-count:]
    )]
