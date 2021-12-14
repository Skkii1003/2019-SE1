import unittest
from src import filter_even_numbers

class TestFilterEvenNumbers(unittest.TestCase):
    def test_filter_even_numbers_one(self):
        numbers = [1,2,3,4,5,6]
        expect = [2,4,6]
        actual = filter_even_numbers.filter_even_numbers(numbers)
        self.assertEqual(expect,actual)

    def test_filter_even_numbers_two(self):
        numbers = []
        for i in  range(0,2000):
            numbers.append(i-1000)
        expect = []
        for i in range(-500,500):
            expect.append(i*2)
        actual = filter_even_numbers.filter_even_numbers(numbers)
        self.assertEqual(expect,actual)

    def test_filter_even_numbers_three(self):
        numbers = [2, 4, 6, 8, 10]
        expect = [2, 4, 6, 8, 10]
        actual = filter_even_numbers.filter_even_numbers(numbers)
        self.assertEqual(expect, actual)

    def test_filter_even_numbers_four(self):
        numbers = [1,3,5,7,9]
        expect = []
        actual = filter_even_numbers.filter_even_numbers(numbers)
        self.assertEqual(expect,actual)

    def test_filter_even_numbers_five(self):
        numbers = [10,8,6,4,2]
        expect = [10,8,6,4,2]
        actual = filter_even_numbers.filter_even_numbers(numbers)
        self.assertEqual(expect,actual)

if __name__ == '__main__':
    unittest.main()
