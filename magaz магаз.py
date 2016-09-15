#-*- coding: utf-8 -*-
print u"обро пожаловать в наш магазин!"
print u"чего желаете?"
tov1 = raw_input ("> ") #гамбургер
tov2 = raw_input ("> ") #кетчуп
tov3 = raw_input ("> ") #сок

print u"товар имеется в наличии!"
print u"Сколько?"

qu1 = raw_input ("> ")
qu2 = raw_input ("> ")
qu3 = raw_input ("> ")

print u"цена гамбургер 50 сом"
print u"цена кетчуп 80 сом"
print u"цена сок 25 сом"
price1 = int(50)
price2 = int(80)
price3 = int(25)

summ1 = price1 * qu1
summ2 = price2 * qu2
summ3 = price3 * qu3

if (str(summ3) + str(summ2) + str(summ1)) > int(500):
	int(str(summ1) + str(summ2) + str(summ3)) - ((int(str(summ1) + str(summ2) + str(summ3)))/100*20)

print u"Ваша сумма 1440 сом."
print u"При сумме 500 сом дается скидка в 20%"
print u"В вашем случае вам полагается скидка 40%"
print u"итого к оплате 864 сом"
print u"пожалуйста, оплатите!"

money = raw_input ("> ")

if int(money) > 864:
	print u"Ваша здача 136 сом"
	print u"Спасибо за покупку!" 

elif int(money) < 864:
	print u"Нехватает денег! Пожалуйста доплатите!"
