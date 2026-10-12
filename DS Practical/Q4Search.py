n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter the numbers:"))
    arr.append(num)

search=int(input("enter the number you want to search:"))
flag=0
for i in range(n):
    if arr[i]==search:
        flag=1
        break
    
if flag==1:
    print(search," is found at",i," position")
else:
    print(search," not found")