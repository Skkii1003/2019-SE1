import unittest
import sys
from src import heart_rate_cal


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
        self.stream_in.write('65')
        self.stream_in.write('22')
        heart_rate_cal.heart_rate_calculation()
        expect = ('Intensity|  Rate' + '\n'
        + '---------|------' + '\n'
        + '55%      |138bpm' + '\n'
        + '60%      |144bpm' + '\n'
        + '65%      |151bpm' + '\n'
        + '70%      |158bpm' + '\n'
        + '75%      |164bpm' + '\n'
        + '80%      |171bpm' + '\n'
        + '85%      |178bpm' + '\n'
        + '90%      |184bpm' + '\n'
        + '95%      |191bpm' + '\n')
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_heart_rate_cal_two(self):
        self.stream_in.write('80')
        self.stream_in.write('30')
        heart_rate_cal.heart_rate_calculation()
        expect = ('Intensity|  Rate' + '\n'
        + '---------|------' + '\n'
        + '55%      |140bpm' + '\n'
        + '60%      |146bpm' + '\n'
        + '65%      |151bpm' + '\n'
        + '70%      |157bpm' + '\n'
        + '75%      |162bpm' + '\n'
        + '80%      |168bpm' + '\n'
        + '85%      |173bpm' + '\n'
        + '90%      |179bpm' + '\n'
        + '95%      |184bpm' + '\n')
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    ''' this test case is special, two results may occur dure to different ways to transfer to integer '''
    def test_heart_rate_cal_three(self):
        self.stream_in.write('80')
        self.stream_in.write('50')
        heart_rate_cal.heart_rate_calculation()
        expect = ('Intensity|  Rate' + '\n'
        + '---------|------' + '\n'
        + '55%      |129bpm' + '\n'
        + '60%      |134bpm' + '\n'
        + '65%      |138bpm' + '\n'
        + '70%      |143bpm' + '\n'
        + '75%      |147bpm' + '\n'
        + '80%      |152bpm' + '\n'
        + '85%      |156bpm' + '\n'
        + '90%      |161bpm' + '\n'
        + '95%      |165bpm' + '\n')
        expect2 = ('Intensity|  Rate' + '\n'
          + '---------|------' + '\n'
          + '55%      |129bpm' + '\n'
          + '60%      |134bpm' + '\n'
          + '65%      |138bpm' + '\n'
          + '70%      |142bpm' + '\n'
          + '75%      |147bpm' + '\n'
          + '80%      |152bpm' + '\n'
          + '85%      |156bpm' + '\n'
          + '90%      |161bpm' + '\n'
          + '95%      |165bpm' + '\n')
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        judge = (result == expect) or (result == expect2)
        self.assertTrue(judge)

    def test_heart_rate_cal_four(self):
        self.stream_in.write('65')
        self.stream_in.write('50')
        heart_rate_cal.heart_rate_calculation()
        expect = ('Intensity|  Rate' + '\n'
        + '---------|------' + '\n'
        + '55%      |122bpm' + '\n'
        + '60%      |128bpm' + '\n'
        + '65%      |133bpm' + '\n'
        + '70%      |138bpm' + '\n'
        + '75%      |143bpm' + '\n'
        + '80%      |149bpm' + '\n'
        + '85%      |154bpm' + '\n'
        + '90%      |159bpm' + '\n'
        + '95%      |164bpm' + '\n')
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
