import unittest
import sys
from src import beautiful_year


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
        input_str = '1987\n'
        output_str = '2013\n'
        self.stream_in.write(input_str)
        beautiful_year.get_year()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test2(self):
        input_str = '2200\n'
        output_str = '2301\n'
        self.stream_in.write(input_str)
        beautiful_year.get_year()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test3(self):
        input_str = '2019\n'
        output_str = '2031\n'
        self.stream_in.write(input_str)
        beautiful_year.get_year()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test4(self):
        input_str = '9000\n'
        output_str = '9012\n'
        self.stream_in.write(input_str)
        beautiful_year.get_year()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test5(self):
        input_str = '1000\n'
        output_str = '1023\n'
        self.stream_in.write(input_str)
        beautiful_year.get_year()
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
