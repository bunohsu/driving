i = 2
while i > -1:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('密碼正確')
		break
	if i == 0:
		print('密碼錯誤!')
		break
	else:
		print('密碼錯誤! ', '還有', i, '次機會')
	i = i - 1
