import unittest
from src import max_number
import sys


class TestMaxNumber(unittest.TestCase):

    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_max1(self):
        a = '1'
        b = '1'
        c = '9'
        self.stream_in.write(a)
        self.stream_in.write(b)
        self.stream_in.write(c)
        max_number.get_max_number()
        result = self.stream_out.buff[3]
        self.assertEqual("Have the same number:"+str(a), result)

    def test_max2(self):
        a = '2'
        b = '10'
        c = '2'
        self.stream_in.write(a)
        self.stream_in.write(b)
        self.stream_in.write(c)
        max_number.get_max_number()
        result = self.stream_out.buff[3]
        self.assertEqual("Have the same number:"+str(a), result)

    def test_max3(self):
        a = '13'
        b = '5'
        c = '5'
        self.stream_in.write(a)
        self.stream_in.write(b)
        self.stream_in.write(c)
        max_number.get_max_number()
        result = self.stream_out.buff[3]
        self.assertEqual("Have the same number:"+str(b), result)

    def test_max4(self):
        a = '1'
        b = '99'
        c = '321423'
        self.stream_in.write(a)
        self.stream_in.write(b)
        self.stream_in.write(c)
        max_number.get_max_number()
        result = self.stream_out.buff[3]
        self.assertEqual("The largest number is "+str(c), result)

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
        if len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            return cur
