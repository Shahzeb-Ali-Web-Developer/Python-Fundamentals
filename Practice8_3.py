
	c2 = randint(65, 90) #Capital alphabets have ascii 65 to 90
	count = 0
	print (f'First Character: {chr(c1)}\nSecond Character: {chr(c2)}')
	if (c1 & 1) == (c2 & 1):		count = count + 1;
	if (c1 & 2) == (c2 & 2):		count = count + 1;
	if (c1 & 4) == (c2 & 4):		count = count + 1;
	if (c1 & 8) == (c2 & 8):		count = count + 1;
	if (c1 & 16) == (c2 & 16):		count = count + 1;
	if (c1 & 32) == (c2 & 32):		count = count + 1;
	if (c1 & 64) == (c2 & 64):		count = count + 1;
	if (c1 & 128) == (c2 & 128):	count = count + 1;
	if count == 8:
		print (f'{chr(c1)} and {chr(c2)} are same')
	else:
		print (f'{chr(c1)} and {chr(c2)} are different')

main()