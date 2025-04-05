# Insertion Sort
def ins_sort(l):
    n = len(l)
    for i in range(1, n):
        while l[i] < l[i-1]:
            if i == 0:
                break                         #This sorting is not the standard way to do insertion sort i implemented this way
            else:                             #This is an inefficient way but still it passes all the test cases that i checked
                l[i], l[i-1] = l[i-1], l[i]
                i -= 1
        print(l)
    return l
n = int(input("Enter the number of elements you would like to add in list: "))
l = []
for i in range(n):
    p = int(input(f"Enter the element at {i} index in the list: "))
    l.append(p)
print(f"Original List is : {l}")
print(f"Sorted List is: {ins_sort(l)}")




