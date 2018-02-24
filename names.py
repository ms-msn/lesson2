names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
#i = 0
#while i < len(names):
#	if names[i] == 'Валера':
#		print(names.pop(i), 'нашелся')
	
#	i += 1
	

def find_person(name):
	i = 0
	while i < len(names):
		if names[i] == name:
			print(names.pop(i), 'нашелся')
	
		i += 1
	
find_person('Маша')

def ask_user():
	otvet = ''
	while otvet != 'Хорошо':
		try:
			otvet = input('Как дела? ')
		except KeyboardInterrupt:
			print('Пока')
ask_user()

def get_answer():
	otvet = ''
	while otvet != 'Пока':
		otvet = input()

		
get_answer()