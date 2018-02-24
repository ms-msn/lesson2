age = int(input('Сколько вам лет?'))
if age < 7 :
	type_of_activity = 'Садик'
elif age >= 7 and age <= 18 :
	type_of_activity = 'Школа'
elif age > 18 and age <= 23 :
	type_of_activity = 'Вуз'
elif age > 23 :
	type_of_activity = 'Работа'
print(type_of_activity)
