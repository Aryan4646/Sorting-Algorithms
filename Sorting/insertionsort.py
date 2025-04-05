def ins_sort(l):
    n = len(l)
    for i in range(1,n):
        j = i
        for j in range(j, 0, -1):
            if l[j] >= l[j-1]:
                break
            else:
                l[j], l[j-1] = l[j-1], l[j]
    return l
n = int(input("Enter the number of elements you would like to add in list: "))
l = []
for i in range(n):
    p = int(input(f"Enter the element at {i} index in the list: "))
    l.append(p)
print(f"Original List is : {l}")
print(f"Sorted List is: {ins_sort(l)}")