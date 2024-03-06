
lim=int(input("Enter the limit of the list "))
l=[]
unique_list = []
for i in range(lim):
    x=input("Enter the element: ")
    l.append(x)
    for char in x:
        if char not in unique_list:
            unique_list.append(char)
print("original list",l)
print("Unique list",unique_list)




