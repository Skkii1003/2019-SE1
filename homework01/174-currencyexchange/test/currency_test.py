import unittest
from src import currency
import sys


class TestCurrency(unittest.TestCase):
    """test currency exchange"""

    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_currency1(self):
        euro = '97'
        rate = '31'
        self.stream_in.write(euro)
        self.stream_in.write(rate)
        currency.currency_exchange()
        result = float(str(self.stream_out.buff[2]).split(" ")[9])
        self.assertEqual(result, 30.07)

    def test_currency2(self):
        euro = '105'
        rate = '423'
        self.stream_in.write(euro)
        self.stream_in.write(rate)
        currency.currency_exchange()
        result = float(str(self.stream_out.buff[2]).split(" ")[9])
        self.assertEqual(result, 444.15)

    def test_currency3(self):
        euro = '81'
        rate = '137.51'
        self.stream_in.write(euro)
        self.stream_in.write(rate)
        currency.currency_exchange()
        result = float(str(self.stream_out.buff[2]).split(" ")[9])
        self.assertEqual(result, 111.38)

    def test_currency4(self):
        euro = '13'
        rate = '7'
        self.stream_in.write(euro)
        self.stream_in.write(rate)
        currency.currency_exchange()
        result = float(str(self.stream_out.buff[2]).split(" ")[9])
        self.assertEqual(result, 0.91)

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
