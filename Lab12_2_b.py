from random import *

def main():
	LENGTH = randint(5, 6)
	d = [[randint(1, 9) for i in range(LENGTH)] for j in range(LENGTH)]
	NOLINK = -1				#NOLINK is defined to reprent that there is no direct link between two cities
	for i in range(len(d)):
		for j in range(len(d)):
			value = randint (0, 9)
			if value == 5:				#in case of 5, consider no link, so chances are 1 out of 10
				d[i][j] = NOLINK
			print (d[i][j], end = ' ')
		print()
	for i in range(LENGTH):
		d[i][i] = 0
	for i in range(LENGTH):
		for j in range(LENGTH):
			if i != j and d[i][j] == NOLINK:
				for k in range(LENGTH):
					if i != k and j != k and d[i][k] != NOLINK and d[k][j] != NOLINK:
						print(f'City {i} has indirect link with {j} via {k}')
						break				#terminate k loop if one indirect link found
main()
