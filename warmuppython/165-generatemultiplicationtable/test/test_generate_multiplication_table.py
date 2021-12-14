import unittest
import sys
from src import generate_multiplication_table


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_heart_rate_cal_one(self):
        self.stream_in.write('1')
        generate_multiplication_table.generate()
        expect = (
            '0 X 0 = 0' + '\n'
            + '0 X 1 = 0' + '\n'
            + '1 X 0 = 0' + '\n'
            + '1 X 1 = 1' + '\n'
        )
        result = ''
        for i in range(1, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_heart_rate_cal_two(self):
        self.stream_in.write('2')
        generate_multiplication_table.generate()
        expect = (
            '0 X 0 = 0' + '\n'
            + '0 X 1 = 0' + '\n'
            + '0 X 2 = 0' + '\n'
            + '1 X 0 = 0' + '\n'
            + '1 X 1 = 1' + '\n'
            + '1 X 2 = 2' + '\n'
            + '2 X 0 = 0' + '\n'
            + '2 X 1 = 2' + '\n'
            + '2 X 2 = 4' + '\n'
        )
        result = ''
        for i in range(1, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_heart_rate_cal_three(self):
        self.stream_in.write('3')
        generate_multiplication_table.generate()
        expect = (
            '0 X 0 = 0' + '\n'
            + '0 X 1 = 0' + '\n'
            + '0 X 2 = 0' + '\n'
            + '0 X 3 = 0' + '\n'
            + '1 X 0 = 0' + '\n'
            + '1 X 1 = 1' + '\n'
            + '1 X 2 = 2' + '\n'
            + '1 X 3 = 3' + '\n'
            + '2 X 0 = 0' + '\n'
            + '2 X 1 = 2' + '\n'
            + '2 X 2 = 4' + '\n'
            + '2 X 3 = 6' + '\n'
            + '3 X 0 = 0' + '\n'
            + '3 X 1 = 3' + '\n'
            + '3 X 2 = 6' + '\n'
            + '3 X 3 = 9' + '\n'
        )
        result = ''
        for i in range(1, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_heart_rate_cal_four(self):
        self.stream_in.write('4')
        generate_multiplication_table.generate()
        expect = (
            '0 X 0 = 0' + '\n'
            + '0 X 1 = 0' + '\n'
            + '0 X 2 = 0' + '\n'
            + '0 X 3 = 0' + '\n'
            + '0 X 4 = 0' + '\n'
            + '1 X 0 = 0' + '\n'
            + '1 X 1 = 1' + '\n'
            + '1 X 2 = 2' + '\n'
            + '1 X 3 = 3' + '\n'
            + '1 X 4 = 4' + '\n'
            + '2 X 0 = 0' + '\n'
            + '2 X 1 = 2' + '\n'
            + '2 X 2 = 4' + '\n'
            + '2 X 3 = 6' + '\n'
            + '2 X 4 = 8' + '\n'
            + '3 X 0 = 0' + '\n'
            + '3 X 1 = 3' + '\n'
            + '3 X 2 = 6' + '\n'
            + '3 X 3 = 9' + '\n'
            + '3 X 4 = 12' + '\n'
            + '4 X 0 = 0' + '\n'
            + '4 X 1 = 4' + '\n'
            + '4 X 2 = 8' + '\n'
            + '4 X 3 = 12' + '\n'
            + '4 X 4 = 16' + '\n'
        )
        result = ''
        for i in range(1, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_heart_rate_cal_five(self):
        self.stream_in.write('5')
        generate_multiplication_table.generate()
        expect = (
            '0 X 0 = 0' + '\n'
            + '0 X 1 = 0' + '\n'
            + '0 X 2 = 0' + '\n'
            + '0 X 3 = 0' + '\n'
            + '0 X 4 = 0' + '\n'
            + '0 X 5 = 0' + '\n'
            + '1 X 0 = 0' + '\n'
            + '1 X 1 = 1' + '\n'
            + '1 X 2 = 2' + '\n'
            + '1 X 3 = 3' + '\n'
            + '1 X 4 = 4' + '\n'
            + '1 X 5 = 5' + '\n'
            + '2 X 0 = 0' + '\n'
            + '2 X 1 = 2' + '\n'
            + '2 X 2 = 4' + '\n'
            + '2 X 3 = 6' + '\n'
            + '2 X 4 = 8' + '\n'
            + '2 X 5 = 10' + '\n'
            + '3 X 0 = 0' + '\n'
            + '3 X 1 = 3' + '\n'
            + '3 X 2 = 6' + '\n'
            + '3 X 3 = 9' + '\n'
            + '3 X 4 = 12' + '\n'
            + '3 X 5 = 15' + '\n'
            + '4 X 0 = 0' + '\n'
            + '4 X 1 = 4' + '\n'
            + '4 X 2 = 8' + '\n'
            + '4 X 3 = 12' + '\n'
            + '4 X 4 = 16' + '\n'
            + '4 X 5 = 20' + '\n'
            + '5 X 0 = 0' + '\n'
            + '5 X 1 = 5' + '\n'
            + '5 X 2 = 10' + '\n'
            + '5 X 3 = 15' + '\n'
            + '5 X 4 = 20' + '\n'
            + '5 X 5 = 25' + '\n'
        )
        result = ''
        for i in range(1, len(self.stream_out.buff)):
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

    def readline(self):
        if len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            return cur
