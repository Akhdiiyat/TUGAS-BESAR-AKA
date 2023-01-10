import time
array = list(range(1,100000001))
x = 2
start_time = time.time()
print("rekursif")
def binary_search(array, low, high, x):
    if high < low:
        return -1
    mid = (low+high)//2
    if array[mid] > x:
        return binary_search(array, low, mid - 1, x)
    elif array[mid] < x:
        return binary_search(array, mid + 1, high, x)
    else:
        return mid
result2 = binary_search(array, 0, len(array)-1, x)
 
if result2 != -1:
    print("The index of the Element is", str(result2))
else:
    print("This element is not present in your Array.")
    
end_time = time.time()
elapsed_time = end_time - start_time
print(f'The program took {elapsed_time} seconds to run.')
print("")

start2_time = time.time()

print("iteratif")
def binary_search(array, x):
    low = 0
    high = len(array) - 1 
    while low <= high:
        mid = (high + low) // 2
        if array[mid] < x:
            low = mid + 1
        elif array[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

result = binary_search(array, x)
if result != -1:
    print("The index of the element is", str(result))
else:
    print("We do not have this element in the Array.")
    
end2_time = time.time()
elapsed2_time = end2_time - start2_time
print(f'The program took {elapsed2_time} seconds to run.')