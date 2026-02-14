# WAP to take input for your name and display each rotation until original name appear 
name=input("Enter your name : ")
rotate=name 
count=1
while True:
    print(rotate)
    rotate=rotate[-1]+rotate[:-1]
    if rotate==name:
        print(rotate)
        print("No. of rotation :",count)
        break
    else:
        count+=1
        

