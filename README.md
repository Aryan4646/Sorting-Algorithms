# Gcd-python
# In the recursive approach applied euclidean algorithm:
If a % b == 0, then b is the GCD because it completely divides a.
If a % b ≠ 0, the remainder r = a % b becomes the new divisor.
Repeat with (b, r) until the remainder is 0.
The last divisor before hitting 0 is the GCD.

#In the iterative approach 
Instead of recursion, used a while loop to implement the Euclidean algorithm iteratively.
