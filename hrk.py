a=int(raw_input())
x=1
y=1
count=0
if(a==0):
	print(a)
elif(a<0):
	print("enter the valid number")
else:
	while(count<a):
		print x,
		term=x+y
		x=y
		y=term
		count+=1
	
