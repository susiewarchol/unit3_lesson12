health = input('What is your health?')


if int(health) == 100:
	print('You are at full health.')
elif int(health) >= 20:
	print('You have taken some minor damage. Health at ' + str(health))
elif int(health) >= 1:
	print('You only have ' + str(health) + ' health. Critical warning!')
else:
	print('You have died :(')