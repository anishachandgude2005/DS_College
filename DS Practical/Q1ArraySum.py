n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n) :
    num=int(input("Enter the number:"))
    arr.append(num)
total=0
for i in range(n):
    total=total+arr[i]
print("Sum=",total)