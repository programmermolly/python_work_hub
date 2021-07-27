cubes=[]

for i in range(1,11):
	cubes.append(i**3)

for cube in cubes:
	print(cube)

print('The first three items in the list are:',cubes[:3])

print('Three items from the middle of the list are:',cubes[4:6])
print('The last three items in the list are:',cubes[7:])