# Find longest sum in contiguous sub array (Kadane's Algorithm)

def maxSubarraySum(arr):
    max_sum = float("-inf")
    cur_sum = 0
    for i in range(0,len(arr)-1):
        cur_sum += arr[i]
        if max_sum < cur_sum:
            max_sum = cur_sum
        if cur_sum < 0:
            cur_sum = 0
    return max_sum

# Driver's Code
arr = [-1,-2,4,-2,-2,1,5,-3]
print(maxSubarraySum(arr))

