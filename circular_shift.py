def circular_shift(arr,k):
    n=len(arr)
    k=k%n
    return arr[-k:]+arr[:-k]


lim=int(input("Enter the limit of the list "))
l=[]
for i in range(lim):
    x=int(input("Enter the element: "))
    l.append(x)
print(l)
s=int(input("Enter the number of rotations: "))
s=circular_shift(l,s)
print(s)



