#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys
import datetime
from src import retire_schedule


class TestRetireSchedule(unittest.TestCase):
	def setUp(self):
		self.stream_out = MyStream()
		self.stream_in = MyStream()
		self.out_stream = sys.stdout
		self.in_stream = sys.stdin
		sys.stdout = self.stream_out
		sys.stdin = self.stream_in
		pass

	def test_retire_schedule_one(self):
		year = datetime.datetime.now().year
		self.stream_in.write('25')
		self.stream_in.write('65')
		retire_schedule.calculate()
		expect = 'You have 40 years left until you can retire.' + '\n' + 'It\'s ' + str(year) + ', so you can retire in ' + str(year + 40) + '.' + '\n'
		result = ''
		for i in range(2, len(self.stream_out.buff)):
			result = result + self.stream_out.buff[i]
		self.assertEqual(expect, result)

	def test_retire_schedule_two(self):
		year = datetime.datetime.now().year
		self.stream_in.write('30')
		self.stream_in.write('60')
		retire_schedule.calculate()
		expect = 'You have 30 years left until you can retire.' + '\n' + 'It\'s ' + str(year) + ', so you can retire in ' + str(year + 30) + '.' + '\n'
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


if __name__ == '__main__':
	print(unittest.main)
