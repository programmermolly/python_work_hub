rivers={'Yangtze River':'China','Yellow River':'China','Neil':'Egypt'}

for river,country in rivers.items():
	print(f'The {river} runs through {country}')

# 打印河流名字
for river in rivers.keys():
	print(f'这条河流叫：{river}')

# 打印国家名字
for country in rivers.values():
	print(f'这条河流经{country}')