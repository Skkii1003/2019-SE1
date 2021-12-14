import unittest
from src import isAnagram_cal


class TestIsAnagram(unittest.TestCase):

    def setUp(self):
        pass

    def test_one(self):
        self.assertEqual(True, isAnagram_cal.is_anagram('note', 'tone'))

    def test_two(self):
        self.assertEqual(True, isAnagram_cal.is_anagram('', ''))

    def test_three(self):
        self.assertEqual(True, isAnagram_cal.is_anagram('n', 'n'))

    def test_four(self):
        self.assertEqual(False, isAnagram_cal.is_anagram('abcdefg', 'gfedcbaa'))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
