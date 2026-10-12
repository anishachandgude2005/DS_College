n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    num=int(input("Enter the number:"))
    arr.append(num)

even=0
odd=0

for i in range(n):
    if arr[i]%2==0:
        even=even+1
    else:
        odd=odd+1

print("Even=",even)
print("Odd=",odd)
