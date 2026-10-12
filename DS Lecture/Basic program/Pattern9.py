n=int(input("Enter no of rows:"))
mid=(n+1)/2
for i in range(n):
    for j in range(n):
        if(j==mid-1 or i==mid-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()