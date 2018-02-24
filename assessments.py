list_class_assessments = [{'school_class': '4a', 'scores': [3,5,5,5,2]},{'school_class': '4b', 'scores': [3,4,4,5,2]},{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '4c', 'scores': [3,2,2,5,2]}]
scores_class = []
score_all = 0

for classes in list_class_assessments:
	scores_class += classes['scores']

print(scores_class)
for score in scores_class:
	score_all += score
school_average = score_all/len(scores_class)
print('Средний бал по школе = ', school_average) 
for classes in list_class_assessments:
	scor = 0
	for sco in classes['scores']:
		scor += sco
	class_average = scor/len(classes['scores'])
	print('Название класса: ', classes['school_class'], 'Средний бал: ', class_average)
