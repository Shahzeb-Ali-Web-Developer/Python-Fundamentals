from random import *
def main():
	LENGTH = 30
	score = pass_count = 0
	rollno = [0] * LENGTH
	marks = [0] * LENGTH
	for i in range(LENGTH):
		rollno[i] = i + 1				#i starts from 0, roll no starts from 1
		marks[i] = randint(1, 100)
		print (marks[i], end = ' ')
	print ()
	SEN = -1
	for i in range(5):
		marks[randint(0, 29)] = SEN
	print("Roll No		Marks")
	for i in range(LENGTH):
		if marks[i] != SEN:
			print (f'  {rollno[i]} \t\t {marks[i]}')
			pass_count += 1
	pass_rollno = [0] * pass_count
	pass_marks = [0] * pass_count
	j = 0
	for i in range(LENGTH):
		if marks[i] != SEN:
			pass_rollno[j] = rollno[i]
			pass_marks[j] = marks[i]
			j += 1
	print(end = '[')
	for i in range(pass_count):
		print(f'{pass_rollno[i]:2d}', end = ' ')
		if (i + 1) < pass_count:
			print (end = ', ')
	print("]\n[", end='')
	for i in range(pass_count):
		print(f'{pass_marks[i]:2d}', end = ' ')
		if (i + 1) < pass_count:
			print (",", end = ' ')
	print("]")

main()