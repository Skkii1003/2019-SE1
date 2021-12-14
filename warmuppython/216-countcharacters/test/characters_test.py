import unittest
from src import characters
import sys


class TestCharacters(unittest.TestCase):
    """test count characters"""
    def setUp(self):
        self.stream_out = MyStream()
        self.out_stream = sys.stdout
        sys.stdout = self.stream_out
        pass

    def test_characters1(self):
        str='Homer'
        characters.count_characters(str)
        test=''
        test = test.join(self.stream_out.buff)
        self.assertEqual(test, "Homer has 5 characters.\n")

    def test_characters2(self):
        str='amy'
        characters.count_characters(str)
        test=''
        test = test.join(self.stream_out.buff)
        self.assertEqual(test, "amy has 3 characters.\n")

    def test_characters3(self):
        str='iPhone'
        characters.count_characters(str)
        test=''
        test = test.join(self.stream_out.buff)
        self.assertEqual(test, "iPhone has 6 characters.\n")

    def test_characters4(self):
        str='hello world'
        characters.count_characters(str)
        test=''
        test = test.join(self.stream_out.buff)
        self.assertEqual(test, "hello world has 11 characters.\n")

    def tearDown(self):
        sys.stdout = self.out_stream
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