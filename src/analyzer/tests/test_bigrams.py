import unittest
from ..bigrams import bigrams, bigramsWithFrequency


class BigramsTest(unittest.TestCase):
    def testBigramsFinding(self):
        text = 'первый снег выпал. снег хрустел под ногами.'
        expect = [
            'первый снег',
            'снег выпал',
            'снег хрустел'
        ]

        self.assertEqual(expect, bigrams(text, 'снег'))

    def testBigramsFindingMultiline(self):
        text = """
            первый снег выпал.
            снег хрустел под ногами.
            первый снег всегда в радость
        """
        expect = [
            'первый снег',
            'снег выпал',
            'снег хрустел',
            'первый снег',
            'снег всегда'
        ]

        self.assertEqual(expect, bigrams(text, 'снег'))

    def testBigramsFrequencyList(self):
        text = """
            первый снег выпал.
            снег хрустел под ногами.
            первый снег всегда в радость.
            первый снег такой первый снег.
            снег выпал, снег выпал!
            снег хрустел
        """
        expect = [
            'снег хрустел',
            'снег выпал',
            'первый снег'
        ]

        self.assertEqual(expect, bigramsWithFrequency(text, 'снег'))

if __name__ == '__main__':
    unittest.main()
