
# Bubble sort
# def bubble_sort(l):
#     n = len(l)
#     for i in range(n-1):
#        for j in range(n-1-i):
#            if l[j] > l[j+1]:
#                l[j], l[j+1] = l[j+1],l[j]
#     return l
# n = int(input("Enter the number of elements you would like to add in list: "))
# l = []
# for i in range(n):
#     p = int(input(f"Enter the element at {i} index in the list: "))
#     l.append(p)
# print(f"Original list is : {l}")
# print(f"Sorted list is: {bubble_sort(l)}")

# Selection Sort
def minm(l,i):
    
def sel_sort(l):
    n = len(l)
    for i in range(n-1):
        ele,ind = minm(l,i)

n = int(input("Enter the number of elements you would like to add in list: "))
l = []
for i in range(n):
    p = int(input(f"Enter the element at {i} index in the list: "))
    l.append(p)
print(f"Original List is : {l}")
print(f"Sorted List is: {sel_sort(l)}")


# cd /c/Users/DELL/PycharmProjects/Solo_Leveling  # Navigate to your project directory
# touch sorting.py  # Create a new Python file
# git add sorting.py  # Stage the new file
# git commit -m "Added sorting.py"  # Commit with a message
# git push origin main  # Push to GitHub (use 'master' if your branch is master)
