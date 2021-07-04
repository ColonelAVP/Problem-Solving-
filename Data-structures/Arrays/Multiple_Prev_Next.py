# fn to Replace every array element by multiplication of previous and next
# Time Complexity = O(n) & Space Complexity = O(1)

def multiple(arr,n):
    prev = arr[0]
    arr[0] = arr[0] * arr[1]
    for i in range(1,n-1):
        cur = arr[i]
        arr[i] = prev * arr[i+1]
        prev = cur
    arr[n-1] = prev * arr[n-1]
    return arr

# Driver's Code
arr = [2,3,4,5,6]
n = len(arr)
print(multiple(arr,n))
