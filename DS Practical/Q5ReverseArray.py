n=int(input("Enter the number of elements:"))
arr=[]

for i in range(n):
    num=int(input("Enter the number:"))
    arr.append(num)

for i in range(n):
    print(arr[n-1-i]," ")