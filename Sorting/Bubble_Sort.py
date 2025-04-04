def bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
n = int(input("Enter the number of elements you would like to add in list: "))
l = []
for i in range(n):
    p = int(input(f"Enter the element at {i} index in the list: "))
    l.append(p)
print(f"Original List is : {l}")
print(f"Sorted List is: {bubble_sort(l)}")