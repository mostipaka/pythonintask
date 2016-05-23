#Задача 8. Вариант 15.
#Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

import random
WORDS =('Переславль-Залесский', 'Ростов Великий', 'Углич', 'Ярославль', 'Кострома', ' Плёс', 'Суздаль', ' Владимир', 'Юрьев-Польский', 'Александров', 'Сергиев Посад', 'Тутаев')
word = random.choice(WORDS)
correct = word
jumble =""
hint=""
ball=100
while word:
	position=random.randrange(len(word))
	jumble+=word[position]
	word = word[:position] + word[(position + 1):]
print(
"""
				Добро пожаловать в игру "Анаграмма":
			Надо переставить буквы так,чтобы получилось осмысленное слово.
		(Для выхода нажмите Enter,не вводя своей версии.)
"""
)
print("Boт анаграмма:", jumble)
guess=" "
while guess != correct and guess != "":
	guess=input("Попробуйте отгадать исходное слово: ")
	if guess=="Подсказка":
		hint=(correct[:position+1])
		print (hint)
		ball-=10
		position+=1
	elif guess==correct:
		print("Вы отгадали!\n")
		print("Ваши баллы",ball)
	elif guess==correct:
		print("Не верно,попробуйте еще раз.")
print("Спасибо за игру!")
input("Нажмите Enter для выхода")
