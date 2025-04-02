# Write a function to check if a number is even or odd.
# def num(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# n = int(input("Enter the number: "))
#
# if num(n) == True:
#     print(f"{n} is even.")
# else:
#     print(f"{n} is odd.")

#  Write a function that takes two numbers and returns the larger one.
# def max_of_two(n1,n2):
#     if n1 < n2:
#         return True
#     else:
#         return False
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
#
# if max_of_two(n1, n2) == True:
#     print(f"Larger number b/w {n1} & {n2} : {n2}")
# else:
#     print(f"Larger number b/w {n1} & {n2} : {n1}")

# Write a function to calculate the sum of the first N natural numbers.
# def sum(n):
#     s = (n*(n+1))/2
#     return s
# n = int(input("Enter the number upto which you want the sum : "))
#
# print(f"The sum of first {n} is {sum(n)}")

#  Reverse a Number

# n = int(input("Enter the number you want to reverse : "))
#
# s = str(n)
#
# print(f"{n} reverse is : {s[::-1]}")

#  Mathematical Approach
# def s(n):
#     n2 = 0
#     while n > 0:
#         p = n % 10
#         n //= 10
#         n2 = n2*10 + p
#     return n2
#
# n = int(input("Enter the number you want to reverse : "))
# print(f"{n} reverse is : {s(n)}")

# Count Digits in a Number
# n = int(input("Enter the number: "))
# s = str(n)
#
# print(f"{n} has {len(s)} digits.")

# Mathematical approach
# def count(n):
#     c = 0
#     while n > 0:
#             n //= 10
#             c += 1
#     return c
# n = int(input("Enter the number: "))
#
# print(f"{n} has {count(n)} digits.")

# checking if a number is Palindrome using this function.
# def s(n):
#     n2 = 0
#     while n > 0:
#         p = n % 10
#         n //= 10
#         n2 = n2*10 + p
#     return n2
#
# n = int(input("Enter the number you want to check palindrome : "))
# n2 = s(n)
# if n == n2:
#     print(f"Yes {n} is palindrome i.e.: {n2}")
# else:
#     print(f"oho number {n} and {n2} are not palindrome")

# sum of the digits of a given number.
# def s(n):
#     sum = 0
#     while n > 0:
#         p = n % 10
#         n //= 10
#         sum += p
#     return sum
#
# n = int(input("Enter the number whose sum of digit you want : "))
#
# print(f"The sum of {n} digits : {s(n)}")

# product of digits of a number
# def s(n):
#     pro = 1
#     while n > 0:
#         p = n % 10
#         n //= 10
#         pro *= p
#     return pro
#
# n = int(input("Enter the number whose product of digit you want : "))
#
# print(f"The product of {n} digits : {s(n)}")

# Count the number of even and odd digits in a number.
# def count_even_odd(n):
#     even = 0
#     odd = 0
#     while n > 0:
#         p = n % 10
#         n //= 10
#         if p % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return even, odd
#
# n = int(input("Enter the number whose number of odd and even digits you want to find: "))
#
# even_count, odd_count = count_even_odd(n)
# print(f"Number of even and odd digits in {n} are {even_count} and {odd_count}, respectively.")

# Wap a function to calculate factorial of a numbr using recursion
# def fac(n,m):
#     if n == 1:
#         return m
#     else:
#         return fac(n-1, m*n)
#
# n = int(input("Enter the number whose factorial you would like to calculate: "))
# m = 1
# print(f"Factorial of {n} is {fac(n,m)}")

# Print numbers from n to 1 using recursion

# def rec(n):
#     if n == 1:
#         print(n)
#     else:
#         print(n)
#         rec(n-1)
#
# n = int(input("Enter the number: "))
#
# print(f"Number is {n} and the numbers are as follows:")
# rec(n)

# Print numbers from 1 to n  using recursion
# def rec(n,i):
#     if n >= 1:
#         print(i)
#         i += 1
#         rec(n-1, i)
#     else:
#         pass
# n = int(input("Enter the number: "))
# i = 1
# print(f"Number is {n} and the numbers are as follows:")
# rec(n, i)

#  Another approach without i  Print numbers from 1 to n  using recursion

# def rec(n):
#     if n >= 1:
#         rec(n-1)
#         print(n)
#
#     else:
#         pass
# n = int(input("Enter the number: "))
# print(f"Number is {n} and the numbers are as follows:")
# rec(n)

# Write a recursive function that takes an integer n and returns the sum of all numbers from 1 to n.
# def rec(s,n):
#     if n >= 1:
#         return rec(s+n, n-1)
#     else:
#         return s
# n = int(input("Enter the number : "))
# s = 0
# print(f"The sum of first {n} numbers is: {rec(s,n)}")

# try solving it without passing s as an argument and just using n
# def rec(n):
#     if n >= 0:
#         rec(n-1)
#         n += n
#         return n
#     else:
#         pass
# n = int(input("Enter the number : "))
# print(f"The sum of first {n} numbers is: {rec(n)}")

# Write a function to find the maximum of three numbers.
# def max(a,b,c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
#
# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
#
# print(f"The largest number between {a},{b} & {c} is : {max(a,b,c)}")

# Write a function to calculate the factorial of a number (without recursion).
# def fac(n):
#     z = 1
#     while n >= 1:
#         z *= n
#         n -= 1
#     else:
#         return z
#
# n = int(input("Enter the number: "))
#
# print(f"The factorial of number {n} is {fac(n)}")

# Write a function that checks if a number is prime.
# def prime(n):
#     count = 1
#     i = 2
#     while i <= n:
#         if n % i == 0:
#             count += 1
#             i += 1
#         else:
#             i += 1
#     if count == 2:
#         return "Yes", n
#     else:
#         return "No", n
#
# n = int(input("Enter the number: "))
# y, p = prime(n)
# if y == "Yes":
#     print(f"{y} number {p} is prime ")
# else:
#     print(f"{y} number {p} is not prime ")

# Write a function that returns the sum of all digits in a number.
# def s(n):
#     total = 0
#     while n > 0:
#         p = n % 10
#         n //= 10
#         total += p
#     return total
# n = int(input("Enter the number:"))
#
# print(f"The sum of all digits in number {n} is {s(n)}")

# Implement a recursive function to calculate factorial.
# def fac(n,mul):
#     if n <= 1:
#         return mul
#     return fac(n-1, mul*n)
#
# n = int(input("Enter the number: "))
# mul = 1
# print(f"The factorial of number {n} is {fac(n,mul)}")


# Implement a recursive function to reverse a number.

# def rec(n, rev=0):
#     if n <= 0:
#         return rev
#     else:
#         rev = rev * 10 + n % 10
#         return rec(n // 10, rev)
#
# n = int(input("Enter the number: "))
# print(f"The reverse of number {n} is {rec(n)}")

# Implement a recursive function to print numbers from 1 to N.
# def rec(n, i=1):
#     if i <= n:
#         print(i)
#         rec(n,i+1)
#
# n = int(input("Enter the number: "))
#
# print(f"The number has printed from 1 upto {n} as follows:")
# rec(n)

# Write a function that returns a lambda function to calculate the square of a number.

# n = int(input("Enter the number: "))
# s = lambda n: n ** 2
# print(f"The square of {n} is : {s(n)}")

# Use a lambda function to sort a list of tuples based on the second element.

# import random
#
# data = [(random.randint(1, 10), random.randint(1, 10)) for i in range(4)]
# print(data)
# sorted_list = sorted(data, key=lambda x: x[1])
# print(sorted_list)

# Implement a recursive function to find the sum of digits of a number.
# def rec(n, s=0):
#     if n <= 0:
#         return s
#     else:
#         s += n % 10
#         return rec(n//10, s)
#
# n = int(input("Enter the number: "))
#
# print(f"The sum of digits of {n} is {rec(n)}")

# Implement a recursive function to check if a string is a palindrome.
# def rec(n,rev=0):
#     if n <= 0:
#         return rev
#     else:
#         rev = rev * 10 + n % 10
#         return rec(n // 10, rev)
# def pro(n):
#     return "Yes" if rec(n) == n else "No"
#
# s = input("Enter the string : ")
# n = int(s)
# y = pro(n)
# if y == "Yes":
#     print(f"The string {s} is palindrome ")
# else:
#     print(f"The string {s} is not palindrome.")

# Implement a recursive function to compute the nth Fibonacci number.
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# n = int(input("Enter the number: "))
#
# print(f"The {n}th number in fibonacci sequence is : {fib(n)}")

# Create a list of 5 numbers and print the first, last, and middle elements.

# l = []
# n= int(input("How many elements do you want in your list: "))
#
# for i in range(n):
#     o = int(input(f"Enter the element at index {i}: "))
#     l.append(o)
#
# print(f"The first element of list is : {l[0]}")
# print(f"The middle elements of list are : {l[1:(n-1)]}")
# print(f"The last element of list is: {l[n-1]}")


# Create a list of mixed data types (int, string, float, bool).
# Change the third element of a list to "Python" and print the list.

# li = [18, "hello", 3.13, True, "Hey", 6, 3.14]
# print("Original List: ")
# for _ in li:
#     print(_, end=" ")
# print("\n")
# li[2] = "Python"
# print("Modified list: ")
# for _ in li:
#     print(_, end=" ")

# Write a Python program that does the following:
#
# 1️⃣ Take an integer n as input (the number of elements in a list).
# 2️⃣ Accept n integer inputs from the user and store them in a list.
# 3️⃣ Print the list after creation.
# 4️⃣ Replace the second element with 100.
#     5️⃣ Add 999 to the end of the list.
# 6️⃣ Remove the third element from the list.
# 7️⃣ Check if 50 exists in the list and print "50 is in the list" if found, else print "50 is not in the list".
# 8️⃣ Print the final list and its length.

# n = int(input("Enter the number of elements you want in the list: "))
# li = []
# for i in range(n):
#     p = int(input(f"The element at {i} index is: "))
#     li.append(p)
# print("Original list: ")
# print(li, end=" ")
# li[2] = 100
# li.append(999)
# li.pop(2)
# print("\n")
# if 50 in li:
#     print("50 is the list")
# else:
#     print("50 is not in the list")
# print("Final list is : ")
# print(li, end=" ")
# print("\n")
# print(f"The length of list is: {len(li)}")

# Write a program that:
# 1️⃣ Takes a list of numbers as input.
# 2️⃣ Prints only the **even numbers** using **list comprehension**.

# n = int(input("Enter the number of elements you want in the list: "))
# li = []
# for i in range(n):
#     p = int(input(f"The element at {i} index is: "))
#     li.append(p)
# print("Original list: ")
# print(li, end=" ")
# print("\n")
# even = [x for x in li if x % 2 == 0]
# print("Even number list is : ")
# print(even, end=" ")

# Write a program that:
# Takes n elements as input to create a list.
# Appends 100 to the list.
# Inserts 50 at index 2.
# Removes the last element.
# Sorts the list in ascending order.
# Reverses the sorted list.
# Copies the list to a new variable.
# Prints both lists.

# n = int(input("Enter the number of elements you want in the list: "))
# li = []
# for i in range(n):
#     p = int(input(f"The element at {i} index is: "))
#     li.append(p)
# print("Original list: ")
# print(li, end=" ")
# print("\n")
# li.append(100)
# li.insert(2,50)
# li.pop()
#
# li.sort()
# print("\nSorted list:")
# print(li)
#
# print("Sorted list is: ")
# print(li, end=" ")
# print("\n")
# rev = li[::-1]
# print("Reversed list is: ")
# print(rev, end=" ")
# print("\n")
#
# Problem:
# Take a list of numbers from the user.
# Remove all duplicate values from the list.
# Print the final list with only unique elements.

# n = int(input("Enter the number of elements you want in the list: "))
# li = []
# for i in range(n):
#     p = int(input(f"The element at {i} index is: "))
#     li.append(p)
# print("Original list: ")
# print(li, end=" ")
#
# unique_li = []
# for x in li:
#     if x not in unique_li:
#         unique_li.append(x)
# li = unique_li
#
# print("\n New list: ")
# print(li, end=" ")

# Practice Task:
# 🔹 Create a tuple with numbers from 1 to 5 and print it.
# 🔹 Try creating a single-element tuple.
#
# t1 = (1, 2, 3, 4, 5)    #TUPLE FOR 1 To 5
# t2 = (1,)  #Tuple for single element
# print("Tuple for 1 to 5: ")
# print(t1, end="")
# print("\nSingle element tuple is : ")
# print(t2)

# Given a tuple (10, 20, 30, 40, 50), print the first and last elements.
# 🔹 Extract and print the middle three elements using slicing.

# t1 = (10, 20, 30, 40, 50)
# print(t1[1:4])

# 🔹 Concatenate two tuples (1, 2, 3) and (4, 5, 6) and print the result.
# 🔹 Repeat the tuple (7, 8, 9) 3 times and print it.
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# t3 = (7, 8, 9)
#
# result = t1 + t2
# print(result)
#
# print(t3 * 3)

# Pack three colors into a tuple and unpack them into separate variables.

# color = ("red", "green", "blue")
#
# c1, c2, c3 = color
# print(c1)
# print(c2)
# print(c3)

# Given the tuple (5, 10, 15, 10, 20, 10), count the occurrences of 10 and find its index.
# t1 = (5, 10, 15, 10, 20, 10)
# print(t1.count(10))
# print(t1.index(10))

# Problem 1: Write a Python program to create a set, add multiple elements to it, and remove an element.

# s = {1, 2, 4, 1, 5, 7, 47, 3}
# print(s)
# s.update([2, 56, 5, 3])
# print(s)
# s.remove(2)  #Here 2 is present if it was not present we would get error
# print(s)
#
# s.discard(8)  # With discard we will not get error irrespective we have that element in list or not
# print(s)

# Set Operations
# s1 = {1, 2, 3, 4, 5, 7, 47}
# s2 = {2, 4, 6, 7, 5, 9}
#
# print(f"Set 1 is : {s1}")
# print(f"Set 2 is : {s2}")
# # Union  # Union display all the elements that are in either a or b
# un = s1.union(s2)
# print(f"Union of set 1 and set 2 is : {un}")
# # Intersection # Intersection display the element that belong in both sets
# inter = s1.intersection(s2)
# print(f"Intersection of set 1 and set 2 is : {inter}")
# # difference # Difference remove all the element that are present in another set
# diff = s1.difference(s2)
# print(f"Difference of set 1 and set 2 is : {diff}")
# # symmetric difference # in a or b but not in both
# sym = s2.symmetric_difference(s1)
# print(f"Symmetric difference of set2  and set 1 is : {sym}")

# 1️⃣ Creates a dictionary with 5 key-value pairs.
# 2️⃣ Adds a new key-value pair to it.
# 3️⃣ Updates one existing key.
# 4️⃣ Deletes one key.
# 5️⃣ Prints all keys and values separately.

# d = {"name": "Xman", "Age": 26, "Email": "xman@gmail.com", "City": "London"}
# print("Original Dictionary")
# print(d.items())
# print("Added key to the dict: ")
# d["Placed"] = "No"
# print(d.items())
# d["Age"]= 28
# print("Updated dictionary: ")
# print(d)
# print("Dictionary after deletion")
# del d["City"]
# print(d)
# print("All keys:", d.keys())
# print("All values:", d.values())

# In Python, you can merge dictionaries in multiple ways:

# ✅ Method 1: Using update()

# d1 = {"name": "Alice", "age": 25}
# d2 = {"city": "New York", "job": "Engineer"}
#
# d1.update(d2)  # Merges d2 into d1
# print(d1)
# ✅ Method 2: Using {**d1, **d2} (Python 3.5+)
# d1 = {"name": "Alice", "age": 25}
# d2 = {"city": "New York", "job": "Engineer"}
#
# merged_dict = {**d1, **d2}
# print(merged_dict)

# Create a dictionary using dictionary comprehension where the keys are numbers
# from 1 to 10, and the values are their cubes.

# d = {x: x**3 for x in range(1, 11)}
# print("The dictionary is as follows: ")
# print(d)

# Modify a nested dictionary:
# Given this dictionary:
# employee = {
#     "John": {"age": 30, "salary": 50000},
#     "Alice": {"age": 28, "salary": 55000},
#     "Bob": {"age": 35, "salary": 60000}
# }
# Increase Bob’s salary by 10%.
# Add a new employee "Mike" with age 26 and salary 48000.

# employee = {
#     "John": {"age": 30, "salary": 50000},
#     "Alice": {"age": 28, "salary": 55000},
#     "Bob": {"age": 35, "salary": 60000}
# }
# y = employee["Bob"]["salary"]
# y = y + y * 0.1
# employee["Bob"]["salary"] = y
# employee["Mike"] = {"age": 24, "salary": 48000}
# print(employee)

# Count word frequency in a sentence using a dictionary.
# Given a string: "apple banana apple orange banana apple", create a dictionary where the keys are words, and the values are their occurrences.

# s = "apple banana apple orange banana apple"
# words = s.split()
# d = {}
# for i in words:
#     d[i] = d.get(i, 0)+1
# print(d)

# Write a function that takes a list of numbers as input and
# returns a new list containing only the unique elements (removing duplicates)
# while maintaining the original order.
# def li(l):
#     l_new = []
#     x = 0
#     for x in range(len(l)):
#         if l[x] not in l_new:
#             l_new.append(l[x])
#     return l_new
#
# n = int(input("Enter how many number you would like to add in list: "))
# l = []
# for i in range(n):
#     p = int(input(f"Enter the number at {i} in the list : "))
#     l.append(p)
# print(f"The original list is as follows:\n{l}")
# print(f"The unique elements after removing in the list:\n{li(l)}")

# Write a function that takes a list of numbers as input
# and returns a dictionary where keys are the unique numbers,
# and values are their frequencies (how many times they appear in the list).
# def d(l):
#     d = {}
#     for _ in l:
#         if _ not in d:
#             d[_] = 1
#         else:
#             d[_] += 1
#     return d
# n = int(input("Enter how many number you would like to add in list: "))
# l = []
# for i in range(n):
#     p = int(input(f"Enter the number at {i} in the list : "))
#     l.append(p)
# print(f"The original list is as follows:\n{l}")
# print(f"The dictionary is as follows:\n{d(l)}")

# Write a function that takes two lists as input and returns
# a new list containing the elements that are common to both lists (without duplicates).

# def inter(l1,l2):
#     l11 = set(l1)
#     l22 = set(l2)
#     l33 = l11.intersection(l22)
#     l44 = list(l33)
#     return l44
#
# n1 = int(input("Enter how many number you would like to add in list: "))
# l1 = []
# for i1 in range(n1):
#     p1 = int(input(f"Enter the number at {i1} in the list : "))
#     l1.append(p1)
#     n1 = int(input("Enter how many number you would like to add in list: "))
# l2 = []
# n2 = int(input("Enter how many number you would like to add in list: "))
# for i2 in range(n2):
#     p2 = int(input(f"Enter the number at {i2} in the list : "))
#     l2.append(p2)
# print(f"The original list l1 is:\n {l1}")
# print(f"The original list l2 is:\n {l2}")
# print(f"The intersection of {l1} & {l2} is :\n {inter(l1,l2)}")

# Write a function that takes a list of numbers as input and
# returns the second largest number in the list.
# def m(l):
#     large1 = l[0]
#     large2 = "No second largest number exist"
#     for x in l:
#         if x > large1:
#             large2 = large1
#             large1 = x
#
#     return large2
#
# n = int(input("Enter how many number you would like to add in list: "))
# l = []
# for i in range(n):
#     p = int(input(f"Enter the number at {i} in the list : "))
#     l.append(p)
# print(f"The second largest number in {l} is: {m(l)}")

# Write a function that takes a list of numbers as input
# and returns the element that appears the most times in the list.
# def m(l):
#     d = {}
#     max_freq = 0
#     most_freq = 0
#     for x in l:
#         if x not in d:
#             d[x] = 1
#         else:
#             d[x] += 1
#     for key, value in d.items():
#         if value > max_freq:
#             max_freq = value
#             most_freq = key
#     return most_freq, max_freq
#
# n = int(input("Enter how many number you would like to add in list: "))
# l = []
# for i in range(n):
#     p = int(input(f"Enter the number at {i} in the list : "))
#     l.append(p)
# mx, mf = m(l)
# print(f"The most frequent number in the list {l} is:{mx} with appearing {mf} times ")

# Write a function that takes two dictionaries as input and merges them into one.
# If a key exists in both dictionaries, sum their values.
# If a key exists in only one dictionary, keep it as is.
# def get_dict():
#     d = {}
#     n = int(input("How many key value pairs would you like to add in dictionary: "))
#     for i in range(n):
#         p = input(f"Enter the {i+1} key : ")
#         z = int(input(f"Enter the {i+1} value: "))
#         d[p] = z
#     return d
# def merge_dict(d1,d2):
#     merged = d1.copy()
#     for key, value in d2.items():
#         if key in merged:
#             merged[key] += value
#         else:
#             merged[key] = value
#     return merged
#
# print("Enter the 1st dictionary:")
# d1 = get_dict()
# print("Enter the 2nd dictionary:")
# d2 = get_dict()
# print(f"First dictionary is : {d1}")
# print(f"Second dictionary is: {d2}")
# print(f"The merged dictionary is : {merge_dict(d1,d2)}")

# Find the Missing Number in a List
# Given a list of n-1 unique numbers from 1 to n, find the missing number.
# Example: [1, 2, 4, 5] → Output: 3
# def mis(n,l):
#     s = 0
#     for i in l:
#         s += i
#     e_sum = (n*(n+1))/2
#     return e_sum - s
# n = int(input("Enter upto how many number you would like to add in list: "))
# l = []
# for i in range(n-1):
#     p = int(input(f"Enter the number in the list : "))
#     l.append(p)
# print(f"The list is as follows: {l}")
# print(f"The missing element in the list is :{mis(n,l)} ")

# Find the Key with the Maximum Value
# Given a dictionary {‘a’: 10, ‘b’: 25, ‘c’: 15}, return the key with the highest value.
# Output: 'b'
# def maxim(d):
#     maxed = 0
#     max_key = None
#     for key, value in d.items():
#         if maxed < value:
#             maxed = value
#             max_key = key
#     return max_key,maxed
# n = int(input("How many key value pairs would you like to add in dictionary: "))
# d = {}
# for i in range(n):
#     p = input(f"Enter the {i+1} key : ")
#     z = int(input(f"Enter the {i+1} value: "))
#     d[p] = z
# print(f"The dictionary is as follows:\n{d}")
# k, v = maxim(d)
# print(f"The maximum element key is: {k}\nThe maximum value is: {v}")

# Invert a Dictionary
# Swap keys and values in a dictionary.
# Example: {1: 'a', 2: 'b', 3: 'c'} → {‘a’: 1, ‘b’: 2, ‘c’: 3}
# def rev(d):
#     d_new = {}
    for key, value in d.items():
#         if value in d_new:
#             d_new[value].append(key)  # Store multiple keys in a list
#         else:
#             d_new[value] = [key]  # Initialize list with first key
#     return d_new
# n = int(input("How many key value pairs would you like to add in dictionary: "))
# d = {}
# for i in range(n):
#     p = input(f"Enter the {i+1} key : ")
#     z = int(input(f"Enter the {i+1} value: "))
#     d[p] = z
# print(f"The dictionary is as follows:\n{d}")
# print(f"The reversed key value-pairs in dictionary are as follows:\n{rev(d)}")
