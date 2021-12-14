import unittest
import sys
from src import arrival_of_general


class Test(unittest.TestCase):

    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test1(self):
        input_num = '4\n'
        input_strs = ('21\n', '11\n', '75\n', '32\n')
        output_str = '3\n'
        self.stream_in.write(input_num)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        arrival_of_general.calculate()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test2(self):
        input_num = '2\n'
        input_strs = ('21\n', '11\n')
        output_str = '0\n'
        self.stream_in.write(input_num)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        arrival_of_general.calculate()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test3(self):
        input_num = '10\n'
        input_strs = ('11\n', '88\n', '33\n', '90\n', '1\n', '3\n', '44\n', '34\n', '22\n', '22\n')
        output_str = '8\n'
        self.stream_in.write(input_num)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        arrival_of_general.calculate()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test4(self):
        input_num = '16\n'
        input_strs = ('23\n', '44\n', '1\n', '22\n', '34\n', '56\n', '444\n', '65\n', '21\n', '43\n', '78\n', '89\n', '5\n', '12\n', '9\n', '11\n')
        output_str = '18\n'
        self.stream_in.write(input_num)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        arrival_of_general.calculate()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test5(self):
        input_num = '8\n'
        input_strs = ('6\n', '4\n', '65\n', '21\n', '43\n', '78\n', '89\n', '444\n')
        output_str = '12\n'
        self.stream_in.write(input_num)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        arrival_of_general.calculate()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

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
