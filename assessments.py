list_class_assessments = [
{'school_class': '4a', 'scores': [3,5,5,5,2]},
{'school_class': '4b', 'scores': [3,4,4,5,2]},
{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '4c', 'scores': [3,2,2,5,2]}
]
scores_class = []
score_all = 0
class_average_dict = {}
for classes in list_class_assessments:
    scores_class += classes['scores']
    class_average = sum(classes['scores']) / len(classes['scores'])
    class_average_dict[classes['school_class']] = class_average
school_average = sum(scores_class) / len(scores_class)
print('Средний бал по школе = ', school_average)
print(class_average_dict)


'''print(scores_class)
for score in scores_class:
    score_all += score

print('Средний бал по школе = ', school_average) 
for classes in list_class_assessments:
    scor = 0
    for sco in classes['scores']:
        scor += sco
    class_average = scor/len(classes['scores'])
    print('Название класса: ', classes['school_class'], 'Средний бал: ', class_average)
'''