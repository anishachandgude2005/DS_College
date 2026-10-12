n=int(input("Enter number of elements:"))
arr=[]
for i in range(n) :
    num=int(input("Enter the Number:"))
    arr.append(num)

max=arr[0]
min=arr[0]
smin=arr[0]
smax=arr[0]

for i in range(1,n) :
    if arr[i]>max:
        smax=max
        max=arr[i]
    elif arr[i]>smax and arr[i]!=max:
        smax=arr[i]

for i in range(1,n):
    if arr[i]<min:
        smin=min
        min=arr[i]
    elif arr[i]<smin and arr[i]!=min:
        smin=arr[i]

print("Max=",max)
print("Second Max=",smax)
print("Min=",min)
print("Second Min=",smin)