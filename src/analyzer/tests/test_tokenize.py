import unittest
from ..tokenize import tokenize


class TokenizeTest(unittest.TestCase):
    def testTextTokenizing(self):
        text = 'кошка кошка собака собака собака мышь'
        expect = ['кошка', 'кошка', 'собака', 'собака', 'собака', 'мышь']

        self.assertEqual(expect, tokenize(text))

    def testTextTokenizingWithNotLetters(self):
        text = 'кошка,;-+ - собака,мышь медведь кто-то где-нибудь'
        expect = ['кошка', 'собака', 'мышь', 'медведь', 'кто-то', 'где-нибудь']

        self.assertEqual(expect, tokenize(text))

if __name__ == '__main__':
    unittest.main()
