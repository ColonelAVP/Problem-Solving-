# Fn for reversal algorithm of array rotation

def reversearray(array, low, high):
    while low < high:
        temp = array[low]    # storing first element to  var. temp
        array[low] = array[high]  #  storing hth element to positon array [l]
        array[high] = temp   #  storing temp  to positon array [h]
        low += 1
        high -= 1

def leftrotate(array, shift):
    if shift == 0:    #incase, shift = 0, original array should be returned
        return
    n = len(array)
    shift = shift % n   # incase, shift > n ; shift = shift % len(array)

    reversearray(array, 0, shift-1)
    reversearray(array, shift, n-1)
    reversearray(array, 0, n-1)

# to print the changed array
def printarray(array):
    for i in range(0,len(array)):
        print(array[i], end=" ")

# Driver's code
array = [1, 2, 3, 4]
n = len(array)
shift = 1

leftrotate(array, shift)
printarray(array)
