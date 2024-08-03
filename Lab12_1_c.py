from random import *

def main():
	LENGTH = randint(5, 6)
	#The distance is taken in 3 digits to avoid duplication
	d = [[randint(100, 999) for i in range(LENGTH)] for j in range(LENGTH)]
	for i in range(len(d)):
		for j in range(len(d)):
			print (d[i][j], end = ' ')
		print()
	for i in range(LENGTH):
		d[i][i] = 0
	shortest_distance = 1000000000
	shortest_distance_from = shortest_distance_to = 0
	for i in range(LENGTH):
		for j in range(LENGTH):
			if i != j:
				if shortest_distance > d[i][j]:
					shortest_distance = d[i][j]
					shortest_distance_from = i
					shortest_distance_to = j
	print (f'City {shortest_distance_from + 1} and City {shortest_distance_to + 1} has shortest direct distance {shortest_distance}')

main()
