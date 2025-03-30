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

def rec(n, rev=0):
    if n <= 0:
        return rev
    else:
        rev = rev * 10 + n % 10
        return rec(n // 10, rev)

n = int(input("Enter the number: "))
print(f"The reverse of number {n} is {rec(n)}")
