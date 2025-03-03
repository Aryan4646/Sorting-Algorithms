def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = int(input("Enter the larger number: "))
num2 = int(input("Enter the smaller number: "))

print(f"GCD of {num1} & {num2} is : {gcd(num1,num2)}")