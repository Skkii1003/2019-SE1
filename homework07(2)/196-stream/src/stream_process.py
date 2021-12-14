#! /usr/bin/env python
# -*- coding: utf-8 -*-


def process(param):

	# delete those with one character

	validword = []
	for word in param:
		if len(word) > 1:
			validword.append(word)

	# transform the first character

	finalword = []

	for word in validword:
		newword = ''
		if word[0] >= 'a' and word[0] <= 'z':
			newword += chr(ord(word[0]) - 32)
		else:
			newword += word[0]
		for i in word[1:]:
			if i >= 'A' and i <= 'Z':
				newword += chr(ord(i) + 32)
			else:
				newword += i
		finalword.append(newword)

	# output

	result = ','.join(finalword)
	return result

