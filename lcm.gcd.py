def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, (num1 % num2)
        gcd = num1
    return gcd
num1 = int(input("Enter the first number :"))  #Take input 1 from the user
num2 = int(input("Enter the second number :"))  #Take input 2 from the user
gcd_value = gcd(num1, num2)
Lcm = (num1 *num2)/gcd_value
print(f"The gcd of {num1} & {num2} is : {gcd_value}")
print(f"The Lcm of {num1} & {num2} is : {Lcm}")
