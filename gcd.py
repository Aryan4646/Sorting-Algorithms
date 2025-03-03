# WAP to calculate GCD without using any inbuilt function

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
gcd = 1
i = 2
if num1 > num2:
    while num2 >= i :
        if num1 % i == 0 and num2 % i == 0 :
            gcd *= i
            num1 //= i
            num2 //= i
        else:
            i += 1
else:
    while num1 >= i :
        if num1 % i == 0 and num2 % i == 0 :
            gcd *= i
            num1 //= i
            num2 //= i
        else:
            i += 1
print(f"GCD of {num1*gcd} & {num2*gcd} is: {gcd}")