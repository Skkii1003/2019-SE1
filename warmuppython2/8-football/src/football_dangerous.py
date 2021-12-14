"""write your code in method"""


def is_dangerous():
	position = input()
	same = True
	times = 0
	for i in range(1,len(position)):
		if position[i] == position[i-1]:
			times = 1
			same = True
			while same:
				if i+times >=len(position):
					same = False
					continue
				if position[i] == position[i+times]:
					times += 1
					if times == 6:
						print('YES')
						return
				else:
					times = 0
					same = False

	print('NO')
	return
