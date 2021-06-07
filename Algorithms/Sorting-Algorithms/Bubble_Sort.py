# Fn to sort a array by using Bubble Sort
# Time Complexity = O(n^2) and Space Complexity = O(1)

def bubble_Sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                # print(arr) To verify Iterations
    return arr

# Driver's' Code
arr = [5,4,3,11,9,22,0]
print(bubble_Sort(arr))