#-*- coding: utf-8 -*-
from random import randint
x = randint (1, 10)

i =0
while i <= 11:
	print u" угадай! "
	answer = int(raw_input ("> "))
	if answer == x:
		print u" молодец"
	else:
		print u" плохо "