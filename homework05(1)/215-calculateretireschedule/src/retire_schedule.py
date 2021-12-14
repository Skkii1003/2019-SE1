#! /usr/bin/env python
# -*- coding: utf-8 -*-


def calculate():
	currentage = int (input('What is your current age?'))
	retireage = int (input('At what age would you like to retire?'))

	remainyears = retireage - currentage
	retireyears = 2020 + remainyears

	if remainyears <= 0:
		remainyears = 0
	print('You have',remainyears,'years left until you can retire.')
	print('It\'s 2020, so you can retire in {}.'.format(retireyears))
	pass
