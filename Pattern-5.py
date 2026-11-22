n=int(input("Enter The No:-"))
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()