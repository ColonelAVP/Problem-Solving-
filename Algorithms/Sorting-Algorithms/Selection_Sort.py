# Fn to sort array using Selection Sort
# Time Complexity = O(n^2), Space Complexity = O(1)

def selection_sort(arr):
    for i in range(0, len(arr)):
        minimum_index = i
        for j in range(i+1, len(arr)):
            if arr[minimum_index] > arr[j]:
                minimum_index = j
        arr[i],arr[minimum_index] = arr[minimum_index],arr[i]
        # print(arr) To verify each iteration
    return arr

# Driver's Code
arr = [10,6,15,23,11,78,2]
print(selection_sort(arr))