import json
filename='favourite_number.json'
favourite_number=input('请输入一个你喜欢的数： ')
with open(filename,'w') as f:
	json.dump(favourite_number,f)


