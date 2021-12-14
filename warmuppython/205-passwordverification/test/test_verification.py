import unittest
import sys
from src import verification


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_verification_one(self):
        self.stream_in.write('user01')
        self.stream_in.write('12345')
        user = 'user01'
        pwd = 'abc$123'
        verification.password_verification(user, pwd)
        expect = 'I don\'t know you.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_verification_two(self):
        self.stream_in.write('user01')
        self.stream_in.write('abc$123')
        user = 'user01'
        pwd = 'abc$123'
        verification.password_verification(user, pwd)
        expect = 'Welcome!\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_verification_three(self):
        self.stream_in.write('user03')
        self.stream_in.write('abc$123')
        user = 'user01'
        pwd = 'abc$123'
        verification.password_verification(user, pwd)
        expect = 'I don\'t know you.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_verification_four(self):
        self.stream_in.write('user03')
        self.stream_in.write('1234')
        user = 'user01'
        pwd = 'abc$123'
        verification.password_verification(user, pwd)
        expect = 'I don\'t know you.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_verification_five(self):
        self.stream_in.write('user03')
        self.stream_in.write('12$user')
        user = 'user03'
        pwd = '12$user'
        verification.password_verification(user, pwd)
        expect = 'Welcome!\n'
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
        if len(self.buff) > 10000:
            sys.exit("Too many outputs, error! There may be an endless loop in your code!")

    def readline(self):
        if len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            return cur
