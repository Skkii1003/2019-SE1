import unittest
import sys
from src import paint_cal


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
        self.stream_in.write('10')
        self.stream_in.write('36')
        paint_cal.paint_calculation()
        expect = ('You will need to purchase 2 gallons of paint'+'\n')
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_two(self):
        self.stream_in.write('20')
        self.stream_in.write('15')
        paint_cal.paint_calculation()
        expect = ('You will need to purchase 1 gallons of paint' + '\n')
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_three(self):
        self.stream_in.write('15')
        self.stream_in.write('100')
        paint_cal.paint_calculation()
        expect = ('You will need to purchase 5 gallons of paint' + '\n')
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_four(self):
        self.stream_in.write('25')
        self.stream_in.write('78')
        paint_cal.paint_calculation()
        expect = ('You will need to purchase 6 gallons of paint' + '\n')
        result = ''
        for i in range(2, len(self.stream_out.buff)):
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