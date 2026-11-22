n=int(input("Enter The No:"))
for i in range(n):
    p=1
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()