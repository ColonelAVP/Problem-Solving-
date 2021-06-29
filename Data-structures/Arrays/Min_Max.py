# fn to find maximum num in unsorted array

def max_number(arr):
    n = len(arr)
    largest_number = arr[0]
    for i in range(1,n):
        if arr[i] > largest_number:
            largest_number = arr[i]
    return largest_number

# fn to find minimum num in unsorted array
def min_number(arr):
    n = len(arr)
    smallest_number = arr[0]
    for i in range(1,n):
        if arr[i] < smallest_number:
            smallest_number = arr[i]
    return smallest_number

# Driver's Code
arr = [10,7,1,13,8,32]
print(max_number(arr))
print(min_number(arr))




