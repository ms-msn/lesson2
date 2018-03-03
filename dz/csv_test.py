import csv

with open('answer.csv', 'r', encoding='utf-8') as f:
    fields = ['question', 'answer']
    reader = csv.DictReader(f, fields, delimiter=';')
    for row in reader:
        print(row)