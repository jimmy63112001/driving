country = input('where are you from?')
age = input('what is your age?')
age = int(age)
if country == 'taiwan':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不能考駕照')