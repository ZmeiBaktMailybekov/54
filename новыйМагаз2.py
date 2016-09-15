#-*- coding: utf-8 -*-
print u"обро пожаловать в наш магазин!"
print u"чего желаете?"

tov1 = raw_input ("> ") #гамбургер
qu1 = raw_input ("Skolko?>")
print u"Цена 50 сом. Ещё?"
tov2 = raw_input ("> ") #кетчуп
qu2 = raw_input ("Skolko?>")
print u"Цена 80 сом. Ещё?"
tov3 = raw_input ("> ") #сок
qu3 = raw_input ("Skolko?>")
print u"Цена 25 сом."

price1 = 50
price2 = 80
price3 = 25

summ1 = price1 * int(qu1)
summ2 = price2 * int(qu2)
summ3 = price3 * int(qu3)

summa = summ1 + summ2 + summ3
print summa