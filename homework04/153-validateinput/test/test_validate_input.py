import unittest
import sys
from src import validate_input


class Testvalidateimput(unittest.TestCase):
    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_validate_input_one(self):
        # validate_input.validate()
        self.stream_in.write('J')
        self.stream_in.write('\n')
        self.stream_in.write('ABCDE')
        self.stream_in.write('A12-1234')
        validate_input.validate()
        expect = ('\"J\" is not a valid first name. It is too short.' + '\n'
                  + 'The last name must be filled in.' + '\n'
                  + 'The ZIP code must be numeric.' + '\n'
                  + 'A12-1234 is not a valid ID.' + '\n')
        result = ''
        for i in range(4, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_validate_input_two(self):
        self.stream_in.write('\n')
        self.stream_in.write('A')
        self.stream_in.write('ABCDE')
        self.stream_in.write('AX-1234')
        validate_input.validate()
        expect = ('The first name must be filled in.' + '\n'
                  + '\"A\" is not a valid last name. It is too short.' + '\n'
                  + 'The ZIP code must be numeric.' + '\n'
                  )
        result = ''
        for i in range(4, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_validate_input_three(self):
        # validate_input.validate()
        self.stream_in.write('ASSS')
        self.stream_in.write('ASD')
        self.stream_in.write('z1')
        self.stream_in.write('QQ?1234')
        validate_input.validate()
        expect = ('The ZIP code must be numeric.' + '\n'
                  + 'QQ?1234 is not a valid ID.' + '\n'
                  )
        result = ''
        for i in range(4, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_validate_input_four(self):
        self.stream_in.write('qwq')
        self.stream_in.write('a')
        self.stream_in.write('11234')
        self.stream_in.write('QQ-3232')
        validate_input.validate()
        expect = ('\"a\" is not a valid last name. It is too short.' + '\n'
                  )
        result = ''
        for i in range(4, len(self.stream_out.buff)):
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

if __name__ == '__main__':
    unittest.main
