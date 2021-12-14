import unittest
from src import insomnia_cure
import sys


class Test(unittest.TestCase):
    """test """

    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test1(self):
        k = '1\n'
        l = '2\n'
        m = '3\n'
        n = '4\n'
        count = '12\n'
        input_strs = (k, l, m, n, count)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        insomnia_cure.solve()
        result = int(str(self.stream_out.readline()))
        self.assertEqual(result, 12)

    def test2(self):
        k = '2\n'
        l = '3\n'
        m = '4\n'
        n = '5\n'
        count = '24\n'
        input_strs = (k, l, m, n, count)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        insomnia_cure.solve()
        result = int(str(self.stream_out.readline()))
        self.assertEqual(result, 17)

    def test3(self):
        k = '1\n'
        l = '1\n'
        m = '1\n'
        n = '1\n'
        count = '10000\n'
        input_strs = (k, l, m, n, count)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        insomnia_cure.solve()
        result = int(str(self.stream_out.readline()))
        self.assertEqual(result, 10000)

    def test4(self):
        k = '10\n'
        l = '9\n'
        m = '8\n'
        n = '7\n'
        count = '6\n'
        input_strs = (k, l, m, n, count)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        insomnia_cure.solve()
        result = int(str(self.stream_out.readline()))
        self.assertEqual(result, 0)

    def test5(self):
        k = '9\n'
        l = '7\n'
        m = '8\n'
        n = '10\n'
        count = '42357\n'
        input_strs = (k, l, m, n, count)
        for input_str in input_strs:
            self.stream_in.write(input_str)
        insomnia_cure.solve()
        result = int(str(self.stream_out.readline()))
        self.assertEqual(result, 16540)

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
