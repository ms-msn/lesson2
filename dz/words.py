with open('referat.txt', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace("\n", " ")
text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
text = text.lower()
words = text.split()
print('Количество слов', len(words))