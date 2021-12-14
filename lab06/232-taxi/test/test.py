import unittest
from src import Taxi
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
        input1 = '5\n'
        input2 = '1 1 1 1 4\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Taxi.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '2\n')

    def test2(self):
        input1 = '1\n'
        input2 = '1\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Taxi.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '1\n')

    def test3(self):
        input1 = '5\n'
        input2 = '4 4 4 4 4\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Taxi.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '5\n')

    def test4(self):
        input1 = '4\n'
        input2 = '1 1 1 1\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Taxi.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '1\n')

    def test5(self):
        input1 = '10\n'
        input2 = '3 1 2 2 2 2 2 2 1 2\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Taxi.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '5\n')

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
