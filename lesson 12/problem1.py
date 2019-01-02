import time
import random

print('-'*65)
print('Magic Eight Ball')
print()

question = input('What is your question? ')
print('Shaking')
time.sleep(1)
print('thinking...')
time.sleep(1)
print('...thinking')
time.sleep(1)

choice = random.randint(1,6)

if choice == 1:
	print('100%')
elif choice == 2:
	print('Likely')
elif choice == 3:
	print('Maybe')
elif choice == 4:
	print('Unlikely')
elif choice == 5:
	print('100% No')
else:
	print('Try Again')
	
	
	
	
	
