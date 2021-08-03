import json
file_name='favourite_number.json'
with open(file_name) as f:
	num=json.load(f)
print(num)
