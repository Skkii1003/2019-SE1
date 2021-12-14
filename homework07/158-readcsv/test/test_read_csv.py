#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys
from src import read_csv


class TestReadCSV(unittest.TestCase):
	def setUp(self):
		self.stream_out = MyStream()
		self.out_stream = sys.stdout
		sys.stdout = self.stream_out
		pass

	def test_read_csv(self):
		read_csv.read('./test/resource-1.csv')
		expect = 'Last    Fisrt    Salary' + '\n' + 'Ling    Mai    55900.00' + '\n' + 'Johnson    Jim    56500.00' + '\n' + 'Zarnecki    Sabrina    51500.00' + '\n'
		result = ''
		for i in range(0, len(self.stream_out.buff)):
			result = result + self.stream_out.buff[i]
		self.assertEqual(expect, result)

	def tearDown(self):
		sys.stdout = self.out_stream
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
