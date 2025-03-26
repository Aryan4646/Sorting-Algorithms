def gcd(a,b):
    y = 1
    x = a if a < b else b
    for i in range(2,x+1):
        if a % i == 0 and b % i == 0:
            y *= i
            a //= i
            b //= i
    return y
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd_value = gcd(num1, num2)
print(f"The GCD of {num1} & {num2} is : {gcd_value}")


