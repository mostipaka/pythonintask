#Задача 5. Вариант 15.
#Программа пишет игру, в которой компьютер загадывает один из двенадцати городов Золотого кольца России, а игрок должен его угадать.

#Mostipaka A. E.
#11.04.16
import random
gorod=('Переславль-Залесский', 'Ростов Великий', 'Углич', 'Ярославль', 'Кострома', ' Плёс', 'Суздаль', ' Владимир', 'Юрьев-Польский', 'Александров', 'Сергиев Посад', 'Тутаев')
city=random.randint(0,13)
Ball=12
rand=gorod[city]
print('Я загадал один из городов Золотого кольца России')
otvet=0
while (otvet)!=(rand):
	otvet=input('Введите один из двенадцати городов Золотого кольца России:')
	if (otvet)!=(rand):
		print('Вы не угадали,попробуйте снова.')
		Ball-=1
	elif (otvet)==(rand):
		print('Вы угадали.')
		print('Ваши баллы:'+str(Ball))
		break
input('Нажмите Enter для выхода.')

    Status API Training Shop Blog About 

    © 2016 GitHub, Inc. Terms Privacy Security Contact Help 

