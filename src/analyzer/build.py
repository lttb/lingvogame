import random

from .tokenize import tokenize
from .bigrams import bigramsWithFrequency
from .frequency import frequencyLimited


def build(text, ** options):
    freqList = frequencyLimited(
        tokenize(text),
        options['min'],
        options['max']
    )

    randomWord = random.choice([* freqList.keys()])

    return (
        randomWord,
        bigramsWithFrequency(text, randomWord)
    )
