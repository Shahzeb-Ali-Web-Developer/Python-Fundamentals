from random import *
def main():
	LENGTH = 10
	x = [0] * LENGTH
	y = [0] * LENGTH
	for i in range(LENGTH):
		x[i] = randint(10, 99)
		print(x[i], end=' ')
	print()
	for i in range(LENGTH):
		y[i] = x[i]		#y is exact copy of x
	for i in range(LENGTH):
		for j in range(LENGTH - 1):
			if y[j] > y[j + 1]:
				y[j], y[j+1] = y[j+1], y[j]
		for j in range(LENGTH):
			print(y[j], end=' ')
		print()
	print("-------------------")
	for i in range(LENGTH):
		print (f'{x[i]} is at position', end=' ')
		for j in range(LENGTH):
			if x[i] == y[j]:
				print(j)
				break				#to avoid duplicate entries

main()