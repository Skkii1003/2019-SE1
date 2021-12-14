import unittest
import sys
from src import interest_cal


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_one(self):
        self.stream_in.write('1500')
        self.stream_in.write('4.3')
        self.stream_in.write('4')
        interest_cal.calculation()
        expect = ('investment:1758.00'+'\n')
        result = ''
        for i in range(3, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_two(self):
        self.stream_in.write('100')
        self.stream_in.write('15')
        self.stream_in.write('30')
        interest_cal.calculation()
        expect = ('investment:550.00' + '\n')
        result = ''
        for i in range(3, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_three(self):
        self.stream_in.write('100')
        self.stream_in.write('4.3')
        self.stream_in.write('1')
        interest_cal.calculation()
        expect = ('investment:104.30' + '\n')
        result = ''
        for i in range(3, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_four(self):
        self.stream_in.write('300')
        self.stream_in.write('4.78')
        self.stream_in.write('3')
        interest_cal.calculation()
        expect = ('investment:343.02' + '\n')
        result = ''
        for i in range(3, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

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
        if len(self.buff) > 1000:
            sys.exit("Too many outputs, error! There may be an endless loop in your code!")

    def readline(self):
        if len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            return cur