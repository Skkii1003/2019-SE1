import unittest
from src import Xenia_and_Ringroad
import sys


class Test(unittest.TestCase):
    """test addOperation"""

    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test1(self):
        input1 = '4 3\n'
        input2 = '3 2 3\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Xenia_and_Ringroad.solve()
        result = int(str(self.stream_out.readline()))
        self.assertEqual(result, 6)

    def test2(self):
        input1 = '4 3\n'
        input2 = '2 3 3\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Xenia_and_Ringroad.solve()
        result = int(str(self.stream_out.readline()))
        self.assertEqual(result, 2)

    def test3(self):
        input1 = '2 2\n'
        input2 = '1 1\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Xenia_and_Ringroad.solve()
        result = int(str(self.stream_out.readline()))
        self.assertEqual(result, 0)

    def test4(self):
        input1 = '4 3\n'
        input2 = '3 2 3\n'
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Xenia_and_Ringroad.solve()
        result = int(str(self.stream_out.readline()))
        self.assertEqual(result, 6)

    def test5(self):
        input1 = '78 58\n'
        input2 = '23 14 73 45 47 14 27 59 65 39 15 23 5 1 50 37 3 51 46 69 75 65 45 68 48 59 77 39 53 21 72 33 46 32 ' \
                 '34 5 69 55 56 53 47 31 32 5 42 23 76 15 2 77 65 24 16 68 61 28 55 10\n '
        input_strs = (input1, input2)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        Xenia_and_Ringroad.solve()
        result = int(str(self.stream_out.readline()))
        self.assertEqual(result, 2505)

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
