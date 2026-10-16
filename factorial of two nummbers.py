a=int(input("give:"))
b=int(input("give"))
c=a
for i in range(1,a+1):
    if b%i==0:
        if a%i==0:
            if i!=1:
                print(i)
            elif i==1:
                print(i)
            else:
                print("not coomon factors")
                break
    
    
        