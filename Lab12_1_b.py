from random import *
def print_shortest_distance(d, city1, city2):
	distance = d[city1][city2]
	via = city1
	for i in range(len(d)):
		if i != city1 and i != city2:
			indirect_distance = d[city1][i] + d[i][city2]
			if distance > indirect_distance:
				distance = indirect_distance
				via = i
	if via == city1:
		print(f'Shortest distance between city {city1 + 1} and city {city2 + 1} is {distance}.')
	else:
		print(f'Shortest distance between city {city1 + 1} and city {city2 + 1} is {distance} via {via + 1}.')

def main():
	LENGTH = randint(5, 6)
	d = [[randint(1, 9) for i in range(LENGTH)] for j in range(LENGTH)]
	for i in range(len(d)):
		for j in range(len(d)):
			print (d[i][j], end = ' ')
		print()
	for i in range(LENGTH):
		d[i][i] = 0
	for i in range(LENGTH):
                for j in range(LENGTH):
                        if i != j:
                                print_shortest_distance(d, i, j)

main()
