def sel_sort():
    n = len(l)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n+1):
            if l[j] < l[min_idx]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
    return l
n = int(input("Enter the number of elements you would like to add in list: "))
l = []
for i in range(n):
    p = int(input(f"Enter the element at {i} index in the list: "))
    l.append(p)
print(f"Original List is : {l}")
print(f"Sorted List is: {sel_sort(l)}")