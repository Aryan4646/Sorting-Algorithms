def merge_Sort(l):


n = int(input("Enter the number of element you would like to add in the list: "))
l= []
for i in range(n):
    p = int(input(f"Enter the element at {i} index of the list: "))
    l.append(p)
print(f"The original list is:\n{l}")
print(f"The sorted list is:\n {merge_Sort(l)}")