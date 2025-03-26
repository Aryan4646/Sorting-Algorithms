def my_max(p):
    m = p[0]
    for i in range(len(p)):
        if m < p[i]:
           m = p[i]
    return m
p = [3, 1, 8, 2, 5]
print(my_max(p))
