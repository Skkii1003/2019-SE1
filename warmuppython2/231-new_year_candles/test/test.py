import unittest
from src import new_year_candles
import sys


class Test(unittest.TestCase):
    """test """

    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test1(self):
        input_ = '3 4\n'
        input_strs = (input_)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        new_year_candles.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '3\n')

    def test2(self):
        input_ = '7 4\n'
        input_strs = (input_)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        new_year_candles.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '9\n')

    def test3(self):
        input_ = '32 17\n'
        input_strs = (input_)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        new_year_candles.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '33\n')

    def test4(self):
        input_ = '5 5\n'
        input_strs = (input_)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        new_year_candles.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '6\n')

    def test5(self):
        input_ = '400 12\n'
        input_strs = (input_)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        new_year_candles.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '436\n')

    def test6(self):
        input_ = '500 11\n'
        input_strs = (input_)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        new_year_candles.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '549\n')

    def tearDown(self):
        sys.stdout = self.out_stream
        sys.stdin = self.in_stream
        pass


class MyStream:

    def __init__(self):
        self.buff = []

    def write(self, output_stream):
        self.buff.append(output_stream)

    def readline(self):
        result = ''
        while len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            result = result + cur
            if result.endswith('\n'):
                return result
        return result
