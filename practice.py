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

def s(n):
    odd = 0
    even = 0
    while n > 0:
        p = n % 10
        n //= 10
        if p % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd

n = int(input("Enter the number whose number of odd and ven you want to find : "))

print(f"The product of {n} digits : {s(n)}")