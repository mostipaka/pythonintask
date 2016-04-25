# Задача 5. Вариант 15.
# Программа, которая выводит один из 12 городом Золотого кольца России

# Mostipaka A. E.
# 11.04.2016
import random
print('Один из городов Золотого кольца России')
gorod1=(' Переславль-Залесский')
gorod2=('Ростов Великий')
gorod3=(' Углич')
gorod4=('Ярославль')
gorod5=(' Кострома')
gorod6=('  Плёс')
gorod7=(' Суздаль')
gorod8=('Владимир')
gorod9=(' Юрьев-Польский')
gorod10=(' Александров ')
gorod11=('Сергиев Посад')
gorod12=(' Тутаев ')

city=random.randint(1,12)
if city==1:
  print (gorod1)
if city==2:
	print(gorod2)
if city==3:
  print (gorod3)
if city==4:
	print(gorod4)
if city==5:
  print (gorod5)
if city==6:
	print(gorod6)
if city==7:
  print (gorod7)
if city==8:
	print(gorod8)
if city==9:
  print (gorod9)
if city==10:
	print(gorod10)
if city==11:
	print(gorod11)
elif city==12:
	print(gorod12)

input('Нажмите Enter для выхода')