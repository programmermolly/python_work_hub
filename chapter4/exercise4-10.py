cube=[]
for i in range(1,11):
	cube.append(i**3)


for i in cube:
	print(i)

print('The first three items in the list are:'+str(cube[:3]))
print('The three items from the middle of the list are:'+str(cube[3:6]))
print('The last three items in the list are:'+str(cube[7:]))