# Find the maximum and minimum element in an array

def min_max(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return(f"The Minimum number is: {arr[0]}\n"
           f"The Maximum number is: {arr[len(arr)-1]}")

# driver's Code
arr = [1,6,8,4,21,3]
print(min_max(arr))

