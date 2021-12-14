import unittest
import sys
from src import number_to_month


class TestMonth(unittest.TestCase):
    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_month1(self):
        self.stream_in.write('1')
        number_to_month.number_2_month()
        result = self.stream_out.buff[1]
        self.assertEqual(result, "The name of the month is january.")

    def test_month3(self):
        self.stream_in.write('3')
        number_to_month.number_2_month()
        result = self.stream_out.buff[1]
        self.assertEqual(result, "The name of the month is March.")

    def test_month5(self):
        self.stream_in.write('5')
        number_to_month.number_2_month()
        result = self.stream_out.buff[1]
        self.assertEqual(result, "The name of the month is May.")

    def test_month7(self):
        self.stream_in.write('7')
        number_to_month.number_2_month()
        result = self.stream_out.buff[1]
        self.assertEqual(result, "The name of the month is July.")

    def test_month9(self):
        self.stream_in.write('9')
        number_to_month.number_2_month()
        result = self.stream_out.buff[1]
        self.assertEqual(result, "The name of the month is September.")

    def test_month11(self):
        self.stream_in.write('11')
        number_to_month.number_2_month()
        result = self.stream_out.buff[1]
        self.assertEqual(result, "The name of the month is November.")

    def tearDown(self):
        sys.stdout = self.out_stream
        sys.stdin = self.in_stream
        pass


class MyStream:
    def __init__(self):
        self.buff = []
        self.write_count = 0

    def write(self, output_stream):
        self.buff.append(output_stream)
        if len(self.buff) > 10000:
            sys.exit("Too many outputs, error! There may be an endless loop in your code!")

    def readline(self):
        if len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            return cur
