i = 0
while i <= 11:

	from random import randint
	x = randint (1, 10)
	y = randint (1, 10)

	if x > y:
		print x - y
	elif x < y:
		print x + y
	elif x == y:
		print x * y
	i += 1