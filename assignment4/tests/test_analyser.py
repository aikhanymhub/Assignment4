import unittest
from analytics.analyser import SleepAnalyser 

class TestAnalyser(unittest.TestCase):

    def setUp(self):
        self.sample = [
            {'name': 'A', 'major': 'Computer Science', 'GPA': '4.0'},
            {'name': 'B', 'major': 'Economics', 'GPA': '3.5'}
        ]
        self.analyser = SleepAnalyser(self.sample)

    def test_major_logic(self):
        result = self.analyser.analyse()
        self.assertEqual(result['Computer Science'], 1)
        self.assertEqual(result['Economics'], 1)

    def test_not_empty(self):
        result = self.analyser.analyse()
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()