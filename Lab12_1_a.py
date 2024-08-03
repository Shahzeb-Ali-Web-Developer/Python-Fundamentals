from random import *
def print_distance(d, city1, city2):
	print (f'Direct Distance: {d[city1][city2]}')
	print('Inirect Distances')
	for i in range(len(d)):
		if i != city1 and i != city2:
			print (f'Via City {i+1}: {d[city1][i] + d[i][city2]}')

def main():
	LENGTH = randint(5, 9)
	d = [[randint(1, 9) for i in range(LENGTH)] for j in range(LENGTH)]
	for i in range(len(d)):
		for j in range(len(d)):
			print (d[i][j], end = ' ')
		print()
	print ('Distance between 2 and 4')
	for i in range(LENGTH):
		d[i][i] = 0
	print_distance(d, 1, 3)

main()