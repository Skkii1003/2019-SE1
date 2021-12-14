import unittest
import sys
from src import sum_of_nums


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_sum_of_nums_one(self):
        self.stream_in.write('1')
        self.stream_in.write('2')
        self.stream_in.write('3')
        self.stream_in.write('4')
        self.stream_in.write('5')
        expect = 'The total is 15\n'
        sum_of_nums.sum_of_nums_calculation()
        result = ''
        for i in range(5, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_sum_of_nums_two(self):
        self.stream_in.write('-1')
        self.stream_in.write('-2')
        self.stream_in.write('-3')
        self.stream_in.write('-4')
        self.stream_in.write('-5')
        expect = 'The total is -15\n'
        sum_of_nums.sum_of_nums_calculation()
        result = ''
        for i in range(5, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_sum_of_nums_three(self):
        self.stream_in.write('10')
        self.stream_in.write('20')
        self.stream_in.write('30')
        self.stream_in.write('40')
        self.stream_in.write('50')
        expect = 'The total is 150\n';
        sum_of_nums.sum_of_nums_calculation()
        result = ''
        for i in range(5, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_sum_of_nums_four(self):
        self.stream_in.write('2')
        self.stream_in.write('4')
        self.stream_in.write('6')
        self.stream_in.write('8')
        self.stream_in.write('16')
        expect = 'The total is 36\n';
        sum_of_nums.sum_of_nums_calculation()
        result = ''
        for i in range(5, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_sum_of_nums_five(self):
        self.stream_in.write('512')
        self.stream_in.write('1024')
        self.stream_in.write('2048')
        self.stream_in.write('4096')
        self.stream_in.write('8192')
        expect = 'The total is 15872\n'
        sum_of_nums.sum_of_nums_calculation()
        result = ''
        for i in range(5, len(self.stream_out.buff)):
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
        if len(self.buff) > 10000:
            sys.exit("Too many outputs, error! There may be an endless loop in your code!")

    def readline(self):
        if len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            return cur
        return ''
