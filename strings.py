def strings(string1,string2):
	if string1 == string2:
		return print(1)
	else:
		if len(string1) > len(string2):
			return print(2)
		if string2 == 'learn':
			return print(3)

strings('aa','aa')

strings('aaa', 'aa')

strings('aaa','learn')