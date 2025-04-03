def gcd(a, b, count = 0):
    count += 1
    if b == 0:
        print(f"Step {count}: {a,b}")
        return a, count
    print(f"Step {count}: {a,b}")
    return gcd(b, a % b, count)
num1 = int(input("Enter the larger number: "))
num2 = int(input("Enter the smaller number: "))
gcd_value, calls = gcd(num1,num2)
print(f"GCD of {num1} & {num2} is : {gcd_value}")
print(f"Number of recursive call is: {calls}")