#-*- coding: utf-8 -*-
print u"Добро пожаловать в наш магазин!"
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

summa = int(summ1 + summ2 + summ3)

print summa
if summa >= 500:
	print u"НО!"
	print u"вам полагается скида в 40%"
elif summa < 500:
	print u"Пожалуйста оплатите!"

oplata = int(summa - summa*0.4)
print "Itogo" + str(oplata) + "som."
print u"Давай деньги!!!"

dengi = int(raw_input ("> "))
sda4a = dengi - oplata
if  dengi > str(oplata):
	print u"Ваша сдача" + str(sda4a) + u"сом."
elif dengi < str(oplata):
	print u"недостаточно денег! дополните!"
else:
	print u"Спасибо за покупку!"
	print u"НЕ ЗАДЕРЖИВАЙТЕ ОЧЕРЕДЬ!"