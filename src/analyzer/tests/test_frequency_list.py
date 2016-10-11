import unittest
from ..frequency import frequency, frequencyLimited


class FrequencyListTest(unittest.TestCase):
    def testListBuilding(self):
        arr = ['кошка'] * 2 + ['собака'] * 3 + ['мышь']
        expect = {'кошка': 1/3, 'собака': 1/2, 'мышь': 1/6}

        self.assertEqual(expect, frequency(arr))

    def testListBuildingWithLimits(self):
        arr = ['кошка'] * 9 + ['мышь']
        expect = {'мышь': 0.1}

        self.assertEqual(expect, frequencyLimited(arr, 0.02, 0.15))

if __name__ == '__main__':
    unittest.main()
