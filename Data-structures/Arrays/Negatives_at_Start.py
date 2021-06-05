# print all negatives at beginning and positives at end

def negatives_at_start(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    print(arr)

# Driver's Code
arr = [-1,-5,-6,8,2,4,3]
negatives_at_start(arr)
