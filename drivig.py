country = input('where are you from?')
age = input('what is your age?')
age = int(age)
if country == 'taiwan':
	if age >= 18:
		print('you can get driving test!')
	else:
		print('no qualificaiton!')
elif country == 'the US':
	if age >= 16:
		print('you can get driving test!')
	else:
		print('no qualificaiton!')