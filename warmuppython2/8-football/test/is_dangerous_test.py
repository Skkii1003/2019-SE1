import unittest
import sys
from src import football_dangerous


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
        input_str = '00100110111111101\n'
        output_str = 'YES\n'
        self.stream_in.write(input_str)
        football_dangerous.is_dangerous()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test2(self):
        input_str = '11110111011101\n'
        output_str = 'NO\n'
        self.stream_in.write(input_str)
        football_dangerous.is_dangerous()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test3(self):
        input_str = '1010101010101010101010\n'
        output_str = 'NO\n'
        self.stream_in.write(input_str)
        football_dangerous.is_dangerous()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test4(self):
        input_str = '000000010101111111\n'
        output_str = 'YES\n'
        self.stream_in.write(input_str)
        football_dangerous.is_dangerous()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test5(self):
        input_str = '010101\n'
        output_str = 'NO\n'
        self.stream_in.write(input_str)
        football_dangerous.is_dangerous()
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
