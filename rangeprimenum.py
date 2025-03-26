def print_primes(n):
    for i in range(1, n+1):
        count = 0
        if n % i == 0:
            count += 1
        if count == 2:
                print("Number is prime", i)
    pass


print_primes(17)  # Output: 2, 3, 5, 7