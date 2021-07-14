import string

#to include any member in the Nominated candidiates for presidency
name=()
citizens=[]
filtr=[]
president=[]
#alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
	f=input("Enter a Name in Uppercase=")
	citizens.append(f)
	if f=="":
		break

print(f"Nominated Candidiates={citizens}")

#to check if they are qualified enough to be president
for name in citizens:
	filtr=[]
	print((name))
	#print(list(name))
	for i in name:
		if i in filtr:
			continue
		else:
			filtr.append(i)
	print("Distinct letters in names=",filtr)
	print("Number of Distinct letters=",len(filtr))
	president.append(len(filtr))
print(f"The President is {citizens[president.index(max(president))]}") 

		



