# WAP to calculate GCD without using any inbuilt function

num1 = int(input("Enter the first number :"))  #Take input 1 from the user
num2 = int(input("Enter the second number :"))  #Take input 2 from the user
gcd = 1
if num1 >num2:  # Condition check if number is greater because we need to run loop only until then
    num3 = num2
else:
    num3 = num1
for i in range(1, num3+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i  # modify the gcd
print(f"GCD of {num1} & {num2} is: {gcd}")