store={'Rice':450,'Beans':200,'Egg':40,'Fish':250,'Spag':250}
bill=()
total=()
print('Welcome!!!we sell:',"\n",[store])
while True:
	a=input('What would you like to buy?=')
	b=input('how many of each product do you want?=')
	if a in store:
		bill=store[a]*b
		print('bill=',bill)
	elif a not in store:
		print('Sorry we don\'t have that')
	else:
		total=bill+total
print('Total=',total)


