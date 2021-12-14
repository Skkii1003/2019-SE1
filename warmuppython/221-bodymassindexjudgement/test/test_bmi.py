import unittest
import sys
from src import bmi_judge


class Test(unittest.TestCase):
    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_temperature_one(self):
        self.stream_in.write('68')
        self.stream_in.write('146')
        bmi_judge.bmi()
        expect = 'Your BMI is 22.2.\nYou are within the ideal weight range.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_temperature_two(self):
        self.stream_in.write('68')
        self.stream_in.write('177')
        bmi_judge.bmi()
        expect = 'Your BMI is 27.0.\nYou are overweight.You should see your doctor.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_temperature_three(self):
        self.stream_in.write('67')
        self.stream_in.write('115')
        bmi_judge.bmi()
        expect = 'Your BMI is 18.1.\nYou are underweight.You should see your doctor.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_temperature_four(self):
        self.stream_in.write('61')
        self.stream_in.write('106')
        bmi_judge.bmi()
        expect = 'Your BMI is 20.1.\nYou are within the ideal weight range.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_temperature_five(self):
        self.stream_in.write('65')
        self.stream_in.write('99')
        bmi_judge.bmi()
        expect = 'Your BMI is 16.5.\nYou are underweight.You should see your doctor.\n'
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
