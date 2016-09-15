i = 1
while i <= 100:
	
	if i % 3 == 0:
		print str(i) + "fizz"
	elif i % 5 == 0:
		print str(i) + "buzz"
	elif i % 3 == i % 5:
		print str(i) + "fizzbuzz"
	else:
		print str(i) + "ups"
	i = i + 1
