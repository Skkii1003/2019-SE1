import unittest
from src import Alice_Bob_and_Chocolate
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
        input2 = '2 9 8 2 7\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Alice_Bob_and_Chocolate.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '2 3\n')

    def test2(self):
        input1 = '1\n'
        input2 = '1\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Alice_Bob_and_Chocolate.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '1 0\n')

    def test3(self):
        input1 = '2\n'
        input2 = '1 1\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Alice_Bob_and_Chocolate.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '1 1\n')

    def test4(self):
        input1 = '5\n'
        input2 = '1 9 8 2 7\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Alice_Bob_and_Chocolate.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '2 3\n')

    def test5(self):
        input1 = '13\n'
        input2 = '9 9 9 9 9 9 9 9 9 9 9 9 9\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Alice_Bob_and_Chocolate.solve()
        result = str(self.stream_out.readline())
        self.assertEqual(result, '7 6\n')

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
