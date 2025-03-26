def my_max(arr):
    max = arr[0]
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
        else:
            pass
    return max
arr = []
num = int(input("How many number you want to insert in your array : "))
for x in range(num):
    num = int(input(f"Enter the {x+1} number :"))
    arr.append(num)
for i in range(len(arr)):
    print(f"The {i+1} element is : {arr[i]}")
print("The max element in this array is :",my_max(arr))