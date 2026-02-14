#find if a no. is a armstrong no. or not 
a=int(input("Enter the no. : "))
l=[]
l1=[]
b=a
while b>0:
    c=b%10
    l.append(c)
    b=b//10
print(l)
for i in l:
    d=i**3
    l1.append(d)
e=0
for j in l1:
    e+=j
if e==a:
    print (a,"is a armstrong no. ")
else :
    print(a,"is not a armstrong no.")