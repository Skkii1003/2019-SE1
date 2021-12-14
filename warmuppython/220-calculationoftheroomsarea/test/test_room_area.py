import unittest
import sys
from src import room_area_cal


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
        self.stream_in.write('20')
        self.stream_in.write('15')
        room_area_cal.room_area_calculation()
        expect = ('300 square feet' + '\n' +
                  '27.871 square meters'+'\n')
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_two(self):
        self.stream_in.write('30')
        self.stream_in.write('20')
        room_area_cal.room_area_calculation()
        expect = ('600 square feet' + '\n' +
                  '55.742 square meters' + '\n')
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_three(self):
        self.stream_in.write('11')
        self.stream_in.write('3')
        room_area_cal.room_area_calculation()
        expect = ('33 square feet' + '\n' +
                  '3.066 square meters' + '\n')
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_four(self):
        self.stream_in.write('75')
        self.stream_in.write('65')
        room_area_cal.room_area_calculation()
        expect = ('4875 square feet' + '\n' +
                  '452.902 square meters' + '\n')
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