favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")



people_should_be_invested=['Mary','Lily', 'jen','John','Sarah']
for person_should_be_invested in people_should_be_invested:
	if person_should_be_invested in favorite_languages.keys():
		print('Thank you for your participation in the survey!')
	else:
		print('Please participate in the survey!')
