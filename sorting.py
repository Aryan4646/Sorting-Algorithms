
# Bubble sort
def bubble_sort(l):
    for x in range(len(l)-1):
        if l[x] > l[x+1]:
            p = l[x]
            l[x] = l[x+1]
            l[x+1] = p
        elif l[x] < l[x+1]:
            x += 1
            p = l[x]
            l[x] = l[x+1]
            l[x+1] = p




n = int(input("Enter the number of elements you would like to add in list: "))
l = []
for i in range(n):
    p = int(input(f"Enter the element at {i} index in the list: "))
    l.append(p)
print(f"Original list is : {l}")
print(f"Sorted list is: {bubble_sort(l)}")
