# Fn to sort a array using Quick Sort
# Time complexity = O(n^2) and Space Complexity = O(1)

def quick_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    pivot = arr[0]
    current = 0
    for i in range(1,n):
        if arr[i] < pivot:
            current += 1
            arr[i],arr[current] = arr[current],arr[i]
    arr[current],arr[0] = arr[0],arr[current]
    left = quick_sort(arr[:current])
    right = quick_sort(arr[current+1:])
    return left + [arr[current]] + right

# Driver's Code
arr = [10,3,16,1,2,11,19,0]
print(quick_sort(arr))