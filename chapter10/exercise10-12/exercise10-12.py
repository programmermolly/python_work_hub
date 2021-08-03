import json
file_name='favourite_number.json'
try:
	with open(file_name) as f:
		num=json.load(f)
except FileNotFoundError:
	favourite_number=input('请输入一个你喜欢的数： ')
	with open(file_name,'w') as f:
		json.dump(33,f)
else:
	print(num)